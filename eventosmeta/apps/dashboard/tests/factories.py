"""
Arquivo: factories.py
Caminho: apps/dashboard/tests/factories.py
Finalidade: Factory para criação de dados de teste.
Atualizações:
 - 10/06/2026: Criação do arquivo - Implementação inicial da factory para os modelos de dashboard
"""

import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from apps.interessados.models import Interessado

faker = Faker('pt_BR')

class InteressadoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interessado

    nome = factory.LazyAttribute(lambda _: faker.name())
    cpf = factory.LazyAttribute(lambda _: faker.cpf())
    email = factory.LazyAttribute(lambda _: faker.email())
    senha = factory.LazyAttribute(lambda _: make_password(faker.password()))
    data_cadastro = factory.LazyAttribute(lambda _: faker.date_time_this_year())


