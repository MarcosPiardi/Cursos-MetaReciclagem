"""
ARQUIVO: apps/interessados/apps.py
AÇÃO: SUBSTITUIR o arquivo apps/interessados/apps.py
MUDANÇA: Configuração correta do app
"""

from django.apps import AppConfig


class InteressadosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.interessados'
    verbose_name = 'Interessados'