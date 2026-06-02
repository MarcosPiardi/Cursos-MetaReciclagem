"""
Arquivo: apps.py
Caminho: apps/selecao/apps.py
Finalidade: Definir os modelos do app seleção.
"""

from django.apps import AppConfig


class SelecaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.selecao'
    verbose_name = 'Processo Seletivo'

    