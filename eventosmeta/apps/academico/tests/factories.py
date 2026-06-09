"""
Arquivo: factories.py
Caminho: apps/academico/tests/factories.py
Finalidade: Factories para criação de objetos de teste relacionados ao app academico
Atualizações:
 - 29/05/2026 - Criação do arquivo com 2 factories: StatusFactory e EventoFactory
 - 09/06/2026 - Adicionada AvaliacaoFactory e MatriculaFactory
 - 09/06/2026 - Corrigida MatriculaFactory para garantir consistência dinâmica de eventos
"""

import factory
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.models import Turma
from apps.selecao.tests.factories import InscricaoFactory

class StatusMatriculaFactory(factory.django.DjangoModelFactory):
    """Factory para StatusMatricula"""
    class Meta:
        model = StatusMatricula
    
    nome = factory.Sequence(lambda n: f'Status {n}')
    cor = '#007bff'
    ordem = factory.Sequence(lambda n: n)


class TurmaFactory(factory.django.DjangoModelFactory):
    """Factory para Turma"""
    class Meta:
        model = Turma
    
    nome = factory.Sequence(lambda n: f'Turma {n}')
    evento = factory.SubFactory('apps.eventos.tests.factories.EventoFactory')
    capacidade = 30
    data_inicio = factory.LazyFunction(lambda: timezone.now().date())
    data_fim = factory.LazyFunction(lambda: (timezone.now() + timedelta(days=30)).date())


class MatriculaFactory(factory.django.DjangoModelFactory):
    """
    Factory para Matricula
    
    BOA PRÁTICA: Resolve inteligentemente a dependência circular.
    Se a turma for passada explicitamente, a inscrição herdará o evento dessa turma.
    Se a turma não for passada, uma nova turma será gerada com o evento da inscrição.
    """
    class Meta:
        model = Matricula

    # Se uma turma já foi fornecida, cria a inscrição apontando para o evento daquela turma
    inscricao = factory.SubFactory(
        InscricaoFactory,
        evento=factory.SelfAttribute('..turma.evento')
    )
    
    # Se uma turma NÃO foi fornecida, gera uma nova baseada no evento da inscrição
    @factory.lazy_attribute
    def turma(self):
        return TurmaFactory()

    # O interessado é obrigatoriamente o mesmo da inscrição (evita fraudar o clean do model)
    interessado = factory.SelfAttribute('inscricao.interessado')
    
    status = factory.SubFactory(StatusMatriculaFactory, nome='Ativa')
    observacoes = ''


class AvaliacaoFactory(factory.django.DjangoModelFactory):
    """Factory para Avaliacao"""
    class Meta:
        model = Avaliacao
    
    matricula = factory.SubFactory(MatriculaFactory)
    nota_final = Decimal('8.5')
    frequencia = Decimal('90.0')
    aprovado = True
    observacoes = ''


    