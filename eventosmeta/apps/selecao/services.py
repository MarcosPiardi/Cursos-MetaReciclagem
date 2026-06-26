"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Finalidade: Serviços de classificação para o app seleção.

Histórico de Alterações:
- 20/02/2026: Implementação inicial do ClassificadorService
- 08/04/2026: Adicionado desempate por data_inscricao (ordem de chegada)
- 15/05/2026: Inclusão de cabeçalho
- 18/05/2026: Refatoração Opção 3 com criação automática de Classificacao
- 19/05/2026: Adicionada validação automática de critérios
             - Método _atende_criterio() para validar inscrição por categoria
             - _calcular_pontos() agora soma apenas pontos de critérios atendidos
             - Desempate por idade (JOVEM/IDOSO) ou timestamp
- 19/05/2026: Refatoração de retorno em classificar_evento()
             - Adicionados campos: total_classificadas, total_lista_espera
             - Compatível com admin action

Funcionalidades:
- Validação automática de inscrição contra critérios (por categoria)
- Cálculo de pontuação com critérios atendidos apenas
- Processamento de inscrição com persistência
- Classificação automática (pontuação + desempate + quotas)
- Atribuição de posições e flags (classificado/lista_espera)
- Retorno estruturado com métricas detalhadas
"""

# Linha 28
from decimal import Decimal
from datetime import date

from django.db import transaction
from django.utils import timezone

from apps.selecao.models import (
    Inscricao,
    Classificacao,
    StatusInscricao,
    InscricaoCriterioAtendido,
)
from apps.eventos.models import Evento


class ClassificadorService:
    """
    Serviço para classificação de inscrições em eventos.
    """

    @staticmethod
    def _atende_criterio(inscricao, criterio):
        interessado = inscricao.interessado
        categoria = criterio.categoria

        hoje = timezone.localdate()

        if categoria == "PCD":
            return bool(interessado.necessidades_especiais)

        if categoria == "NIS":
            return bool(interessado.programa_social)

        if categoria == "JOVEM":
            if interessado.data_nascimento:
                idade = (hoje - interessado.data_nascimento).days // 365
                return 16 <= idade <= 24
            return False

        if categoria == "IDOSO":
            if interessado.data_nascimento:
                idade = (hoje - interessado.data_nascimento).days // 365
                return idade >= 50
            return False

        if categoria == "COTA_RACIAL":
            if interessado.fototipo:
                return interessado.fototipo.id in [2, 3, 5]
            return False

        if categoria == "ESC_FUND_INC":
            return interessado.escolaridade == "FUNDAMENTAL_INCOMPLETO"

        if categoria == "ESC_FUND_COMP":
            return interessado.escolaridade == "FUNDAMENTAL_COMPLETO"

        if categoria == "ESC_MEDIO_INC":
            return interessado.escolaridade == "MEDIO_INCOMPLETO"

        if categoria == "ESC_MEDIO_COMP":
            return interessado.escolaridade == "MEDIO_COMPLETO"

        # Categoria desconhecida: mantém permissivo
        return True

    @staticmethod
    def _calcular_pontos(inscricao):
        pontuacao_total = Decimal("0.00")

        evento_criterios = (
            inscricao.evento.evento_criterios.filter(ativo=True).order_by("prioridade")
        )

        for evento_criterio in evento_criterios:
            criterio = evento_criterio.criterio

            if criterio.tipo_criterio == "PONTUACAO" and criterio.pontos is not None:
                if ClassificadorService._atende_criterio(inscricao, criterio):
                    pontuacao_total += Decimal(str(criterio.pontos))

        return pontuacao_total

    @staticmethod
    def calcular_pontuacao_inscricao(inscricao):
        return ClassificadorService._calcular_pontos(inscricao)

    @staticmethod
    @transaction.atomic
    def processar_inscricao(inscricao):
        pontuacao_total = Decimal("0.00")

        InscricaoCriterioAtendido.objects.filter(inscricao=inscricao).delete()

        evento_criterios = (
            inscricao.evento.evento_criterios.filter(ativo=True).order_by("prioridade")
        )

        for evento_criterio in evento_criterios:
            criterio = evento_criterio.criterio

            if criterio.tipo_criterio != "PONTUACAO":
                continue

            atende = ClassificadorService._atende_criterio(inscricao, criterio)

            pontos = Decimal(str(criterio.pontos)) if criterio.pontos is not None else Decimal("0.00")

            if atende and criterio.pontos is not None:
                pontuacao_total += pontos

            # Auditoria sempre registra quando é PONTUACAO (atendido ou não)
            InscricaoCriterioAtendido.objects.create(
                inscricao=inscricao,
                criterio=criterio,
                pontos_atribuidos=pontos if atende else Decimal("0.00"),
                validado=bool(atende),
            )

        classificacao, criada = Classificacao.objects.get_or_create(
            inscricao=inscricao,
            defaults={"pontuacao_total": pontuacao_total},
        )

        if not criada:
            classificacao.pontuacao_total = pontuacao_total
            classificacao.save(update_fields=["pontuacao_total"])

        return pontuacao_total

    @staticmethod
    @transaction.atomic
    def classificar_evento(evento):
        try:
            inscricoes = Inscricao.objects.filter(evento=evento)

            if not inscricoes.exists():
                return {
                    "sucesso": False,
                    "mensagem": f"Nenhuma inscrição encontrada para o evento {evento.nome}",
                    "total_processadas": 0,
                    "total_classificadas": 0,
                    "total_lista_espera": 0,
                }

            for inscricao in inscricoes:
                ClassificadorService.processar_inscricao(inscricao)

            classificacoes_qs = (
                Classificacao.objects.filter(inscricao__evento=evento)
                .select_related("inscricao__interessado")
                .all()
            )

            # Definir desempate
            tem_criterio_idade = evento.evento_criterios.filter(
                criterio__categoria__in=["IDADE", "FAIXA_ETARIA", "JOVEM", "IDOSO"],
                ativo=True,
            ).exists()

            if tem_criterio_idade:
                classificacoes = sorted(
                    classificacoes_qs,
                    key=lambda x: (
                        -(x.pontuacao_total or Decimal("0.00")),
                        x.inscricao.interessado.data_nascimento or date.today(),
                        x.inscricao.id,
                    ),
                )
            else:
                classificacoes = sorted(
                    classificacoes_qs,
                    key=lambda x: (
                        -(x.pontuacao_total or Decimal("0.00")),
                        x.inscricao.data_inscricao,
                        x.inscricao.id,
                    ),
                )

            # Quotas
            tem_criterio_pcd = evento.evento_criterios.filter(
                criterio__categoria="PCD", ativo=True
            ).exists()
            tem_criterio_social = evento.evento_criterios.filter(
                criterio__categoria="NIS", ativo=True
            ).exists()

            total_vagas = evento.total_vagas
            vagas_pcd = int(total_vagas * 0.30) if tem_criterio_pcd else 0
            vagas_social = int(total_vagas * 0.40) if tem_criterio_social else 0
            vagas_aberta = total_vagas - vagas_pcd - vagas_social  # mantido

            # Reset
            Classificacao.objects.filter(inscricao__evento=evento).update(
                classificado=False, lista_espera=False, posicao=None
            )

            status_lista_espera_obj = StatusInscricao.objects.get(nome="Lista de Espera")
            Inscricao.objects.filter(evento=evento).update(status=status_lista_espera_obj)

            status_classificado_obj = StatusInscricao.objects.get(nome="Classificado")

            posicao = 1
            for classificacao in classificacoes:
                classificacao.posicao = posicao

                if posicao <= total_vagas:
                    classificacao.classificado = True
                    classificacao.lista_espera = False
                    classificacao.inscricao.status = status_classificado_obj
                else:
                    classificacao.classificado = False
                    classificacao.lista_espera = True
                    classificacao.inscricao.status = status_lista_espera_obj

                classificacao.save()
                classificacao.inscricao.save(update_fields=["status"])

                posicao += 1

            total_classificadas = Classificacao.objects.filter(
                inscricao__evento=evento, classificado=True
            ).count()

            total_lista_espera = Classificacao.objects.filter(
                inscricao__evento=evento, lista_espera=True
            ).count()

            return {
                "sucesso": True,
                "mensagem": f"Evento {evento.nome} classificado com sucesso. {total_vagas} vagas preenchidas.",
                "total_processadas": len(classificacoes),
                "total_classificadas": total_classificadas,
                "total_lista_espera": total_lista_espera,
            }

        except StatusInscricao.DoesNotExist:
            return {
                "sucesso": False,
                "mensagem": 'Status "Classificado" não encontrado. Verifique StatusInscricao no admin.',
                "total_processadas": 0,
                "total_classificadas": 0,
                "total_lista_espera": 0,
            }
        except Exception as erro:
            return {
                "sucesso": False,
                "mensagem": f"Erro ao classificar evento: {str(erro)}",
                "total_processadas": 0,
                "total_classificadas": 0,
                "total_lista_espera": 0,
            }

    @staticmethod
    @transaction.atomic
    def desfazer_classificacao_evento(evento):
        try:
            total_desfeitas = Classificacao.objects.filter(inscricao__evento=evento).count()
            Classificacao.objects.filter(inscricao__evento=evento).delete()

            status_pendente = StatusInscricao.objects.get(nome="Pendente")
            Inscricao.objects.filter(evento=evento).update(status=status_pendente)

            return {
                "sucesso": True,
                "mensagem": f"Classificação do evento {evento.nome} desfeita com sucesso.",
                "total_desfeitas": total_desfeitas,
            }
        except StatusInscricao.DoesNotExist:
            return {
                "sucesso": False,
                "mensagem": 'Status "Pendente" não encontrado em StatusInscricao.',
                "total_desfeitas": 0,
            }
        except Exception as erro:
            return {
                "sucesso": False,
                "mensagem": f"Erro ao desfazer classificação: {str(erro)}",
                "total_desfeitas": 0,
            }
        
        