from factory import SubFactory
from ..models import Usuario  # Custom user
from apps.interessados.tests.factories import InteressadoFactory  # Relacionado se necessário

class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.Usuario'  # Ajuste app_label
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@teste.com')
    password = factory.PostGenerationMethodCall('set_password', 'senha123')
    is_staff = False
    is_superuser = False
    is_active = True

    