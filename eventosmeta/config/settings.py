"""
Arquivo: settings.py
Caminho: config/settings.py
Descrição: Configurações principais do projeto Eventos MetaReciclagem.
Histórico de Alterações:
 - 20/02/2026 - Adicionada configuração de e-mail para desenvolvimento
 - 20/02/2026 - EMAIL_BACKEND migrado para SMTP real via .env
 - 23/02/2026 - Migrado para CustomEmailBackend do servidor interno da prefeitura
                IP 10.28.10.54 porta 587 — aceita destinatários externos
 - 12/03/2026 - Adicionadas configurações de rate limiting (django-axes) e CSP headers
 - 12/03/2026 - Atualizado AXES para django-axes 6.1.1 e CSP para django-csp 4.0+
 - 03/07/2026 - Refatoração estrutural do arquivo
                • organização por blocos
                • inclusão condicional do debug_toolbar
                • ajuste de LOGIN_URL para prefixo /eventosmeta/
                • adição de INTERNAL_IPS para desenvolvimento
"""

from datetime import timedelta
from pathlib import Path

from decouple import Csv, config


BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# CONFIGURAÇÕES BÁSICAS
# ==========================================
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='localhost,127.0.0.1',
    cast=Csv(),
)


# ==========================================
# APLICAÇÕES INSTALADAS
# ==========================================
INSTALLED_APPS = [
    # Apps nativos do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Segurança
    'axes',
    'csp',

    # Apps do projeto
    'apps.accounts',
    'apps.interessados',
    'apps.eventos',
    'apps.selecao',
    'apps.academico',
    'apps.portal',
    'apps.dashboard',

    # Ferramentas
    'django_extensions',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]


# ==========================================
# MIDDLEWARE
# ==========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.accounts.middleware.TrocarSenhaObrigatorioMiddleware',
    'csp.middleware.CSPMiddleware',
]

if DEBUG:
    MIDDLEWARE.insert(2, 'debug_toolbar.middleware.DebugToolbarMiddleware')


# ==========================================
# URLS / WSGI
# ==========================================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# ==========================================
# TEMPLATES
# ==========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apps' / 'accounts' / 'templates', 
                 BASE_DIR / 'apps' / 'accounts' / 'templates' / 'accounts', 
                 BASE_DIR / 'apps' / 'portal' / 'templates' / 'portal', 
                 BASE_DIR / 'apps' / 'portal' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.eventos.context_processors.notificacoes_eventos',
            ],
        },
    },
]


# ==========================================
# BANCO DE DADOS
# ==========================================
DATABASES = {
    'default': {
        'ENGINE': config(
            'DATABASE_ENGINE',
            default='django.db.backends.sqlite3',
        ),
        'NAME': config(
            'DATABASE_NAME',
            default=str(BASE_DIR / 'db.sqlite3'),
        ),
        'USER': config('DATABASE_USER', default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'HOST': config('DATABASE_HOST', default=''),
        'PORT': config('DATABASE_PORT', default=''),
    }
}


# ==========================================
# VALIDAÇÃO DE SENHA
# ==========================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==========================================
# INTERNACIONALIZAÇÃO
# ==========================================
LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt-br')
TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')
USE_I18N = True
USE_TZ = True


# ==========================================
# ARQUIVOS ESTÁTICOS E MÍDIA
# ==========================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles_collected'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================
# MODELOS E AUTENTICAÇÃO
# ==========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.Usuario'

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
    'apps.interessados.authentication.InteressadoBackend',
]

LOGIN_URL = config('LOGIN_URL', default='/eventosmeta/staff/login/')
# LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL', default='/staff/dashboard/')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL', default='/eventosmeta/admin/')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL', default='/')


# ==========================================
# E-MAIL
# ==========================================
EMAIL_BACKEND = config(
    'EMAIL_BACKEND',
    default='apps.interessados.utils.CustomEmailBackend',
)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


# ==========================================
# DJANGO AXES - RATE LIMITING
# ==========================================
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=30)
AXES_LOCK_OUT_AT_FAILURE = True
AXES_RESET_ON_SUCCESS = True


# ==========================================
# CONTENT SECURITY POLICY
# ==========================================
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src': ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"),
        'style-src': ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"),
        'img-src': ("'self'", "data:", "https:"),
        'font-src': ("'self'", "https://cdn.jsdelivr.net"),
        'connect-src': ("'self'",),
        'frame-ancestors': ("'none'",),
    }
}


# ==========================================
# CRIPTOGRAFIA
# ==========================================
FIELD_ENCRYPTION_KEY = config('FERNET_KEY')


# ==========================================
# DEBUG TOOLBAR
# ==========================================
INTERNAL_IPS = [
    '127.0.0.1',
]


# ==========================================
# CONFIGURAÇÕES DE SEGURANÇA - PRODUÇÃO
# ==========================================
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


