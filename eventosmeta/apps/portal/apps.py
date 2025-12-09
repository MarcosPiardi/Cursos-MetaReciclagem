"""
Configuração do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/apps.py
Data: 05/12/2025
"""
from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.portal'
    verbose_name = '🌐 Portal do Interessado'