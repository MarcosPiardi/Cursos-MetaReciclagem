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
from ..models import Interessado, Sexo, Fototipo, gerar_hash_cpf

fake = Faker('pt_BR')

class SexoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sexo

    nome = factory.Iterator(['Masculino', 'Feminino', 'Outro'])

class FototipoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fototipo

    nome = factory.Iterator(['Tipo I', 'Tipo II', 'Tipo III', 'Tipo IV', 'Tipo V', 'Tipo VI'])
    descricao = factory.Faker('sentence', nb_words=5)

class InteressadoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interessado
        skip_postgeneration_save = True

    nome = factory.LazyAttribute(lambda obj: fake.first_name() + ' ' + fake.last_name())
    cpf = '123.456.789-00'  # max_length=14 (com formatação)
    cpf_hash = factory.LazyAttribute(lambda obj: gerar_hash_cpf(obj.cpf.replace('.', '').replace('-', '')))
    rg = '12.345.678-9'  # max_length=20
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
    cep = '12345678'  # max_length=8 (8 dígitos puros)
    endereco_residencial = 'Rua Teste'
    num_endereco = 123
    bairro = 'Centro'
    complemento = ''
    cidade_residencia = 'São Paulo'
    uf_residencia = 'SP'
    
    # Contato
    telefone = '11234567890'  # 11 dígitos puros (sem formatação)
    celular = '11987654321'   # 11 dígitos puros (sem formatação)
    email = factory.LazyAttribute(lambda obj: f'{fake.user_name()}@teste.com')
    
    # Programa social
    programa_social = False
    num_nis = '123.45678.90-1'  # max_length=15 (com formatação)
    
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
    telefone_responsavel = '11234567890'
    celular_responsavel = '11987654321'
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

