"""
Arquivo: services.py
Caminho: apps/academico/services.py
Alteração: Adicionado métodos para gestão de matrícula em lote e alteração de status
Data: 12/01/2026
"""

"""
Services do app ACADÊMICO
Responsável por: Lógica de matrículas e avaliações
"""
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Matricula, StatusMatricula, Avaliacao
from apps.selecao.models import Classificacao, Inscricao, StatusInscricao
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
    
    # 
    # 🆕 NOVOS MÉTODOS PARA GESTÃO DE MATRÍCULA
    # Adicionados em 12/01/2026
    # 
    
    @staticmethod
    @transaction.atomic
    def matricular_alunos(inscricoes_ids, usuario=None):
        """
        Realiza matrícula de múltiplos alunos (NOVA IMPLEMENTAÇÃO)
        
        Args:
            inscricoes_ids: Lista de IDs de inscrições
            usuario: Usuário que está realizando a ação (opcional)
            
        Returns:
            dict: Resultado com estatísticas
        """
        # Buscar status necessários
        try:
            status_matricula_ativa = StatusMatricula.objects.get(nome='Ativa')
        except StatusMatricula.DoesNotExist:
            raise ValueError("Status 'Ativa' não encontrado em StatusMatricula")
        
        try:
            status_inscricao_confirmado = StatusInscricao.objects.get(nome='Confirmado')
        except StatusInscricao.DoesNotExist:
            raise ValueError("Status 'Confirmado' não encontrado em StatusInscricao")
        
        # Buscar inscrições
        inscricoes = Inscricao.objects.filter(
            id__in=inscricoes_ids,
            evento__isnull=False
        ).select_related('interessado', 'evento')
        
        total_processadas = 0
        total_sucesso = 0
        total_ja_matriculados = 0
        erros = []
        
        for inscricao in inscricoes:
            try:
                # Verificar se já existe matrícula ativa
                matricula_existente = Matricula.objects.filter(
                    interessado=inscricao.interessado,
                    turma__evento=inscricao.evento
                ).first()
                
                if matricula_existente:
                    total_ja_matriculados += 1
                    logger.info(f"Aluno {inscricao.interessado.nome} já possui matrícula no evento {inscricao.evento.nome}")
                    continue
                
                # Buscar turma padrão do evento (primeira turma ativa)
                turma = Turma.objects.filter(evento=inscricao.evento).first()
                
                if not turma:
                    erros.append(f"Evento {inscricao.evento.nome} não possui turmas cadastradas")
                    continue
                
                # Criar matrícula
                matricula = Matricula.objects.create(
                    interessado=inscricao.interessado,
                    turma=turma,
                    status=status_matricula_ativa,
                    data_matricula=timezone.now()
                )
                
                # Atualizar status da inscrição
                inscricao.status = status_inscricao_confirmado
                inscricao.save()
                
                total_sucesso += 1
                total_processadas += 1
                
                logger.info(
                    f"Matrícula criada com sucesso: "
                    f"Aluno: {inscricao.interessado.nome} | "
                    f"Evento: {inscricao.evento.nome} | "
                    f"Turma: {turma.nome}"
                )
                
            except Exception as e:
                erros.append(f"Erro ao matricular {inscricao.interessado.nome}: {str(e)}")
                logger.error(f"Erro ao matricular aluno {inscricao.interessado.nome}: {e}")
        
        return {
            'sucesso': True,
            'total_processadas': total_processadas,
            'total_sucesso': total_sucesso,
            'total_ja_matriculados': total_ja_matriculados,
            'erros': erros
        }
    
    @staticmethod
    @transaction.atomic
    def alterar_status_inscricao(inscricoes_ids, novo_status_nome, usuario=None):
        """
        Altera status de múltiplas inscrições
        
        Args:
            inscricoes_ids: Lista de IDs de inscrições
            novo_status_nome: Nome do novo status
            usuario: Usuário que está realizando a ação (opcional)
            
        Returns:
            dict: Resultado com estatísticas
        """
        # Buscar status
        try:
            novo_status = StatusInscricao.objects.get(nome=novo_status_nome)
        except StatusInscricao.DoesNotExist:
            raise ValueError(f"Status '{novo_status_nome}' não encontrado em StatusInscricao")
        
        # Buscar inscrições
        inscricoes = Inscricao.objects.filter(id__in=inscricoes_ids)
        
        total_atualizadas = 0
        erros = []
        
        for inscricao in inscricoes:
            try:
                inscricao.status = novo_status
                inscricao.save()
                
                total_atualizadas += 1
                
                logger.info(
                    f"Status da inscrição alterado: "
                    f"Aluno: {inscricao.interessado.nome} | "
                    f"Novo Status: {novo_status_nome}"
                )
                
            except Exception as e:
                erros.append(f"Erro ao alterar status de {inscricao.interessado.nome}: {str(e)}")
                logger.error(f"Erro ao alterar status: {e}")
        
        return {
            'sucesso': True,
            'total_atualizadas': total_atualizadas,
            'erros': erros
        }
    
    # 
    # MÉTODOS EXISTENTES (mantidos)
    # 
    
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


# Importação adicional necessária
from django.utils import timezone


