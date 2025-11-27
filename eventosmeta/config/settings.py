"""
ARQUIVO: config/settings.py - ETAPA 2
AÇÃO: SUBSTITUIR o arquivo config/settings.py
MUDANÇA 1: Linha 147 - Backend de autenticação do Interessado ATIVADO
MUDANÇA 2: Configurações sensíveis movidas para .env (python-decouple)
MUDANÇA 3: Segurança aprimorada (ALLOWED_HOSTS, configurações dinâmicas)
"""

from pathlib import Path
from decouple import config, Csv  # ← NOVO: Importação do decouple

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# SEGURANÇA - MOVIDO PARA .env
# ==============================================================================

# ANTES (hardcoded - INSEGURO):
# SECRET_KEY = 'django-insecure-%wg6e&its5+pj=sy_!3yiy*b)5dek4)&nf@9zl$3$zhtjx-!a%'

# DEPOIS (lê do .env - SEGURO):
SECRET_KEY = config('SECRET_KEY')


# ANTES (sempre True - PERIGOSO em produção):
# DEBUG = True

# DEPOIS (configurável por ambiente):
DEBUG = config('DEBUG', default=False, cast=bool)


# ANTES (vazio - aceita qualquer host):
# ALLOWED_HOSTS = []

# DEPOIS (lista de hosts permitidos do .env):
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())


# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Apps do projeto
    'apps.accounts',
    'apps.interessados',

    # App antigo (MANTER por enquanto - remover depois)
    # 'apps.cursoseoutros',  

    # Apps refatorados (ADICIONAR ESTAS 3 LINHAS) 
    'apps.eventos',
    'apps.selecao',
    'apps.academico',

    # Ferramentas
    'django_extensions', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],  # Templates globais
        'APP_DIRS': True,  # Busca também em apps/nomedoapp/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# ==============================================================================
# DATABASE - CONFIGURÁVEL POR AMBIENTE
# ==============================================================================

# ANTES (sempre SQLite):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DEPOIS (lê do .env - permite trocar banco em produção):
# DATABASES = {
#     'default': {
#         'ENGINE': config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
#         'NAME': config('DATABASE_NAME', default=str(BASE_DIR / 'db.sqlite3')),
#         # Para PostgreSQL em produção, adicionar no .env:
#         # DATABASE_ENGINE=django.db.backends.postgresql
#         # DATABASE_NAME=nome_do_banco
#         # DATABASE_USER=usuario
#         # DATABASE_PASSWORD=senha
#         # DATABASE_HOST=localhost
#         # DATABASE_PORT=5432
#     }
# }

# DATABASES com suporte completo ao .env -------- após mudar efetivamente do sqlite3 para postgresql
DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DATABASE_NAME', default=str(BASE_DIR / 'db.sqlite3')),
        'USER': config('DATABASE_USER', default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'HOST': config('DATABASE_HOST', default=''),
        'PORT': config('DATABASE_PORT', default=''),
    }
}


# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================

# ANTES (hardcoded):
# LANGUAGE_CODE = 'pt-br'
# TIME_ZONE = 'America/Sao_Paulo'

# DEPOIS (configurável):
LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt-br')
TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')

USE_I18N = True
USE_TZ = True


# ==============================================================================
# STATIC FILES (CSS, JavaScript, Images)
# ==============================================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Arquivos estáticos globais
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Para produção (collectstatic)


# ==============================================================================
# MEDIA FILES (uploads)
# ==============================================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==============================================================================
# USER MODEL CUSTOMIZADO
# ==============================================================================

AUTH_USER_MODEL = 'accounts.Usuario'


# ==============================================================================
# AUTHENTICATION BACKENDS
# ==============================================================================

# Backend padrão (Usuario/Staff) + Backend customizado (Interessado com CPF)
# ⚠️ ETAPA 2 - INTERESSADO BACKEND ATIVADO ⚠️
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Autenticação padrão (Usuario)
    'apps.interessados.authentication.InteressadoBackend',  # ← ATIVADO! Autenticação por CPF
]


# ==============================================================================
# LOGIN URLs - CONFIGURÁVEL POR AMBIENTE
# ==============================================================================

# ANTES (hardcoded):
# LOGIN_URL = '/staff/login/'
# LOGIN_REDIRECT_URL = '/staff/dashboard/'
# LOGOUT_REDIRECT_URL = '/'

# DEPOIS (lê do .env):
LOGIN_URL = config('LOGIN_URL', default='/staff/login/')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL', default='/staff/dashboard/')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL', default='/')


# ==============================================================================
# CONFIGURAÇÕES DE SEGURANÇA ADICIONAIS (Questão 4.57)
# ==============================================================================

# Headers de segurança (opção E escolhida)
if not DEBUG:  # Apenas em produção
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True  # Força HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 ano
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True