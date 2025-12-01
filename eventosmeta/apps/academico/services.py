
"""
Services do app ACADÊMICO
Responsável por: Lógica de matrículas e avaliações
"""
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Matricula, StatusMatricula, Avaliacao
from apps.selecao.models import Classificacao
from apps.eventos.models import Turma
import logging

logger = logging.getLogger(__name__)


class MatriculaService:
    """
    Service responsável por gerenciar matrículas
    """
    
    @staticmethod
    def verificar_disponibilidade_turma(turma):
        """
        Verifica se há vagas disponíveis na turma
        
        Args:
            turma: Objeto Turma
            
        Returns:
            tuple: (disponivel: bool, vagas_restantes: int)
        """
        matriculas_ativas = Matricula.objects.filter(
            turma=turma,
            status__nome__in=['Ativa', 'Pendente']
        ).count()
        
        vagas_restantes = turma.capacidade - matriculas_ativas
        disponivel = vagas_restantes > 0
        
        return (disponivel, vagas_restantes)
    
    @staticmethod
    @transaction.atomic
    def matricular_classificado(classificacao, turma):
        """
        Matricula um classificado em uma turma
        
        Args:
            classificacao: Objeto Classificacao
            turma: Objeto Turma
            
        Returns:
            Matricula: Objeto Matricula criado
            
        Raises:
            ValidationError: Se não houver vagas ou candidato não classificado
        """
        # 1. Verificar se está classificado
        if not classificacao.classificado:
            raise ValidationError(
                f"Candidato {classificacao.inscricao.interessado.nome} não está classificado"
            )
        
        # 2. Verificar disponibilidade de vagas
        disponivel, vagas_restantes = MatriculaService.verificar_disponibilidade_turma(turma)
        
        if not disponivel:
            raise ValidationError(
                f"Turma {turma.nome} não possui vagas disponíveis"
            )
        
        # 3. Verificar se já está matriculado
        matricula_existente = Matricula.objects.filter(
            interessado=classificacao.inscricao.interessado,
            turma=turma
        ).exists()
        
        if matricula_existente:
            raise ValidationError(
                f"Candidato {classificacao.inscricao.interessado.nome} já está matriculado nesta turma"
            )
        
        # 4. Buscar status "Ativa"
        status_ativa = StatusMatricula.objects.get(nome='Ativa')
        
        # 5. Criar matrícula
        matricula = Matricula.objects.create(
            turma=turma,
            interessado=classificacao.inscricao.interessado,
            inscricao=classificacao.inscricao,
            status=status_ativa,
            observacoes=f"Matriculado automaticamente. Classificação: {classificacao.posicao}ª posição"
        )
        
        logger.info(
            f"Matrícula {matricula.id} criada para {classificacao.inscricao.interessado.nome} "
            f"na turma {turma.nome}"
        )
        
        return matricula
    
    @staticmethod
    @transaction.atomic
    def matricular_lote(classificacoes, turma):
        """
        Matricula múltiplos classificados em uma turma
        
        Args:
            classificacoes: QuerySet de Classificacao
            turma: Objeto Turma
            
        Returns:
            dict: Resultado com sucessos e erros
        """
        resultados = {
            'sucesso': [],
            'erros': []
        }
        
        for classificacao in classificacoes:
            try:
                matricula = MatriculaService.matricular_classificado(classificacao, turma)
                resultados['sucesso'].append({
                    'matricula': matricula,
                    'interessado': classificacao.inscricao.interessado.nome
                })
            except ValidationError as e:
                resultados['erros'].append({
                    'interessado': classificacao.inscricao.interessado.nome,
                    'erro': str(e)
                })
        
        logger.info(
            f"Matrícula em lote concluída. Sucessos: {len(resultados['sucesso'])}, "
            f"Erros: {len(resultados['erros'])}"
        )
        
        return resultados
    
    @staticmethod
    @transaction.atomic
    def avaliar_aluno(matricula, nota_final, frequencia, observacoes=''):
        """
        Registra avaliação de um aluno
        
        Args:
            matricula: Objeto Matricula
            nota_final: Decimal (0-10)
            frequencia: Decimal (0-100)
            observacoes: str (opcional)
            
        Returns:
            Avaliacao: Objeto Avaliacao criado/atualizado
            
        Raises:
            ValidationError: Se nota ou frequência fora dos limites
        """
        # 1. Validar nota
        if nota_final < 0 or nota_final > 10:
            raise ValidationError("Nota final deve estar entre 0 e 10")
        
        # 2. Validar frequência
        if frequencia < 0 or frequencia > 100:
            raise ValidationError("Frequência deve estar entre 0 e 100")
        
        # 3. Determinar aprovação (nota >= 7.0 E frequência >= 75%)
        aprovado = (nota_final >= 7.0 and frequencia >= 75.0)
        
        # 4. Criar ou atualizar avaliação
        avaliacao, created = Avaliacao.objects.update_or_create(
            matricula=matricula,
            defaults={
                'nota_final': nota_final,
                'frequencia': frequencia,
                'aprovado': aprovado,
                'observacoes': observacoes
            }
        )
        
        # 5. Atualizar status da matrícula
        if aprovado:
            status_concluida = StatusMatricula.objects.get(nome='Concluída')
            matricula.status = status_concluida
        else:
            status_reprovada = StatusMatricula.objects.get(nome='Cancelada')
            matricula.status = status_reprovada
        
        matricula.save()
        
        logger.info(
            f"Avaliação registrada para matrícula {matricula.id}. "
            f"Nota: {nota_final}, Frequência: {frequencia}%, Aprovado: {aprovado}"
        )
        
        return avaliacao
    
    @staticmethod
    def gerar_relatorio_turma(turma):
        """
        Gera relatório de desempenho de uma turma
        
        Args:
            turma: Objeto Turma
            
        Returns:
            dict: Estatísticas da turma
        """
        matriculas = Matricula.objects.filter(turma=turma)
        avaliacoes = Avaliacao.objects.filter(matricula__turma=turma)
        
        total_matriculas = matriculas.count()
        total_avaliacoes = avaliacoes.count()
        aprovados = avaliacoes.filter(aprovado=True).count()
        reprovados = avaliacoes.filter(aprovado=False).count()
        
        # Calcular médias
        if total_avaliacoes > 0:
            media_nota = sum(a.nota_final for a in avaliacoes) / total_avaliacoes
            media_frequencia = sum(a.frequencia for a in avaliacoes) / total_avaliacoes
            taxa_aprovacao = (aprovados / total_avaliacoes) * 100
        else:
            media_nota = 0
            media_frequencia = 0
            taxa_aprovacao = 0
        
        relatorio = {
            'turma': turma.nome,
            'evento': turma.evento.nome,
            'total_matriculas': total_matriculas,
            'total_avaliacoes': total_avaliacoes,
            'aprovados': aprovados,
            'reprovados': reprovados,
            'pendentes': total_matriculas - total_avaliacoes,
            'media_nota': round(media_nota, 2),
            'media_frequencia': round(media_frequencia, 2),
            'taxa_aprovacao': round(taxa_aprovacao, 2)
        }
        
        return relatorio
    
    