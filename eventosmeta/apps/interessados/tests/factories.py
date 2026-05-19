"""
factories.py - Factory Boy para app interessados

Gera Interessado com dados realistas (CPFs válidos, nomes PT-BR).
Baseado em models.py: EncryptedCharField para CPF/NIS, choices para escolaridade/status.

Instale: pip install factory-boy faker
"""

import factory
from factory.fuzzy import FuzzyChoice
from faker import Faker
from django.utils import timezone

from datetime import timedelta
from ..models import Interessado, Sexo, Fototipo, PasswordResetToken, gerar_hash_cpf

fake = Faker('pt_BR')


class SexoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sexo
        django_get_or_create = ('nome',)  # ← ADICIONADO 18/05/2026: evita duplicatas

    nome = factory.Iterator(['Masculino', 'Feminino', 'Outro'])


class FototipoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fototipo
        django_get_or_create = ('nome',)  # ← ADICIONADO 18/05/2026: evita duplicatas

    nome = factory.Iterator(['Tipo I', 'Tipo II', 'Tipo III', 'Tipo IV', 'Tipo V', 'Tipo VI'])
    descricao = factory.Faker('sentence', nb_words=5)


class InteressadoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interessado
        skip_postgeneration_save = True

    nome = factory.LazyAttribute(lambda obj: fake.first_name() + ' ' + fake.last_name())
    
    # ✅ FIX: CPF DINÂMICO (único por factory)
    cpf = factory.LazyAttribute(lambda obj: f"{fake.numerify('###.###.###-##')}")
    
    # ✅ FIX: cpf_hash gerado do CPF dinâmico
    cpf_hash = factory.LazyAttribute(lambda obj: gerar_hash_cpf(obj.cpf.replace('.', '').replace('-', '')))

    rg = factory.LazyAttribute(lambda obj: f"{fake.numerify('##.###.###-#')}")
    data_nascimento = factory.LazyAttribute(lambda obj: fake.date_of_birth(minimum_age=18, maximum_age=65))
    
    sexo = factory.SubFactory(SexoFactory)
    cidade_nascimento = 'São Paulo'
    uf_nascimento = 'SP'
    nacionalidade = 'Brasileira'
    fototipo = factory.SubFactory(FototipoFactory)
    
    escolaridade = FuzzyChoice([
        'FUNDAMENTAL_COMPLETO', 'MEDIO_COMPLETO',
        'SUPERIOR_INCOMPLETO', 'SUPERIOR_COMPLETO'
    ])

    # Endereço
    cep = factory.LazyAttribute(lambda obj: fake.numerify('########'))  # 8 dígitos
    endereco_residencial = factory.LazyAttribute(lambda obj: fake.street_name())
    num_endereco = factory.LazyAttribute(lambda obj: fake.numerify('###'))
    bairro = factory.LazyAttribute(lambda obj: fake.city())
    complemento = ''
    cidade_residencia = 'São Paulo'
    uf_residencia = 'SP'

    # Contato
    telefone = factory.LazyAttribute(lambda obj: fake.numerify('##########'))  # 10 dígitos
    celular = factory.LazyAttribute(lambda obj: fake.numerify('###########'))  # 11 dígitos
    email = factory.LazyAttribute(lambda obj: f'{fake.user_name()}@teste.com')

    # Programa social
    programa_social = False
    num_nis = factory.LazyAttribute(lambda obj: fake.numerify('###.#####.##-#'))

    # PCD
    necessidades_especiais = False
    pcd_fisica = False
    pcd_visual = False
    pcd_auditiva = False
    pcd_intelectual = False
    pcd_psicossocial = False
    pcd_multiplas = False

    # Responsável
    nome_responsavel = factory.LazyAttribute(lambda obj: fake.first_name() + ' ' + fake.last_name())
    telefone_responsavel = factory.LazyAttribute(lambda obj: fake.numerify('##########'))
    celular_responsavel = factory.LazyAttribute(lambda obj: fake.numerify('###########'))
    email_responsavel = factory.LazyAttribute(lambda obj: f'{fake.user_name()}@teste.com')

    observacao = ''

    # Autenticação e LGPD
    is_active = True
    consentimento_lgpd = True
    consentimento_lgpd_em = factory.LazyAttribute(lambda obj: timezone.now())

    @factory.post_generation
    def set_password(self, create, extracted, **kwargs):
        """Criptografa senha padrão 'senha123'."""
        self.set_password('senha123')
        if create:
            self.save()

class PasswordResetTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PasswordResetToken
    
    interessado = factory.SubFactory(InteressadoFactory)
    token = factory.LazyAttribute(lambda obj: fake.sha256())
    criado_em = factory.LazyAttribute(lambda obj: timezone.now())
    expira_em = factory.LazyAttribute(lambda obj: timezone.now() + timedelta(hours=2))
    usado = False



    
