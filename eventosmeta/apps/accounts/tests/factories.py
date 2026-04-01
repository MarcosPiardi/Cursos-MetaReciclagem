import factory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker('pt_BR')


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username', 'email', 'cpf',)

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.Sequence(lambda n: f'user_{n}@example.com')
    
    # CPF sequencial para garantir unicidade nos testes
    cpf = factory.Sequence(lambda n: f'{n:011d}')
    
    is_staff = False
    is_active = True
    
    setor_trabalho = factory.Faker('job', locale='pt_BR')
    local_trabalho = factory.Faker('company', locale='pt_BR')
    telefone = factory.Faker('phone_number', locale='pt_BR')
    celular = factory.Faker('phone_number', locale='pt_BR')

    # Define a senha após a criação do objeto
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    