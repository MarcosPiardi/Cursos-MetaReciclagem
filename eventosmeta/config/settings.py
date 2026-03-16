# Arquivo: settings.py
# Caminho: config/settings.py
# Alteração: Adicionada configuração de e-mail (console backend para desenvolvimento)
# Data: 20/02/2026
# Alteração: EMAIL_BACKEND migrado para SMTP real via .env
# Data: 20/02/2026
# Alteração: Migrado para CustomEmailBackend do servidor interno da prefeitura
#            IP 10.28.10.54 porta 587 — aceita destinatários externos
# Data: 23/02/2026
# Alteração: Adicionadas configurações de rate limiting (django-axes) e CSP headers
# Data: 12/03/2026
# Alteração: Atualizado AXES para django-axes 6.1.1 e CSP para django-csp 4.0+
# Data: 12/03/2026

import os
from pathlib import Path
from decouple import config, Csv
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY    = config('SECRET_KEY')
DEBUG         = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de segurança (axes deve vir antes de django.contrib.auth)
    'axes',  # Adicionado para rate limiting - 12/03/2026
    'csp',   # Adicionado para CSP headers - 12/03/2026

    # Apps do projeto
    'apps.accounts',
    'apps.interessados',
    'apps.eventos',
    'apps.selecao',
    'apps.academico',
    'apps.portal',
    'apps.scripts_admin',
    'dashboard',

    # Ferramentas
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'axes.middleware.AxesMiddleware',  # Adicionado para rate limiting - 12/03/2026
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.accounts.middleware.TrocarSenhaObrigatorioMiddleware',
    'csp.middleware.CSPMiddleware',  # Adicionado para CSP headers - 12/03/2026
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':   config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME':     config('DATABASE_NAME',   default=str(BASE_DIR / 'db.sqlite3')),
        'USER':     config('DATABASE_USER',     default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'HOST':     config('DATABASE_HOST',     default=''),
        'PORT':     config('DATABASE_PORT',     default=''),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE  = config('LANGUAGE_CODE', default='pt-br')
TIME_ZONE      = config('TIME_ZONE',     default='America/Sao_Paulo')
USE_I18N       = True
USE_TZ         = True

STATIC_URL       = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT      = BASE_DIR / 'staticfiles_collected'

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD  = 'django.db.models.BigAutoField'
AUTH_USER_MODEL     = 'accounts.Usuario'

# 
# AUTHENTICATION BACKENDS - Atualizado 12/03/2026
# AxesStandaloneBackend para django-axes 6.1.1
# 
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # Adicionado para django-axes 6.1.1
    'django.contrib.auth.backends.ModelBackend',
    'apps.interessados.authentication.InteressadoBackend',
]

LOGIN_URL           = config('LOGIN_URL',           default='/staff/login/')
LOGIN_REDIRECT_URL  = config('LOGIN_REDIRECT_URL',  default='/staff/dashboard/')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL', default='/')

# 
# CONFIGURAÇÃO DE E-MAIL
# Alteração: 23/02/2026
# Backend customizado para servidor interno da prefeitura (10.28.10.54:587)
# 
EMAIL_BACKEND   = 'apps.interessados.utils.CustomEmailBackend'
EMAIL_HOST      = config('EMAIL_HOST')
EMAIL_PORT      = config('EMAIL_PORT',    cast=int)
EMAIL_USE_TLS   = config('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL   = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_HOST_USER     = config('EMAIL_HOST_USER',     default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL  = config('DEFAULT_FROM_EMAIL')

# 
# CONFIGURAÇÃO AXES - RATE LIMITING (django-axes 6.1.1)
# Atualizado: 12/03/2026
# Máximo 5 tentativas falhas → bloqueio 30 minutos
# 
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=30)
AXES_LOCK_OUT_AT_FAILURE = True
AXES_RESET_ON_SUCCESS = True

# 
# CONFIGURAÇÃO CSP - CONTENT SECURITY POLICY (django-csp 4.0+)
# Atualizado: 12/03/2026
# Formato novo: CONTENT_SECURITY_POLICY com DIRECTIVES
# Política PERMISSIVA para desenvolvimento
# 
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src':  ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"),
        'style-src':   ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"),
        'img-src':     ("'self'", "data:", "https:"),
        'font-src':    ("'self'", "https://cdn.jsdelivr.net"),
        'connect-src': ("'self'",),
        'frame-ancestors': ("'none'",),
    }
}

# 
# CONFIGURAÇÃO FERNET KEY - CRIPTOGRAFIA (django-encrypted-model-fields)
# Adicionado: 12/03/2026
# Necessária para CPF e NIS criptografados
# 
FIELD_ENCRYPTION_KEY = config('FERNET_KEY')

# 
# CONFIGURAÇÕES DE SEGURANÇA - PRODUÇÃO
# 
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER     = True
    X_FRAME_OPTIONS                = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF    = True
    SECURE_SSL_REDIRECT            = True
    SESSION_COOKIE_SECURE          = True
    CSRF_COOKIE_SECURE             = True
    SECURE_HSTS_SECONDS            = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD            = True

