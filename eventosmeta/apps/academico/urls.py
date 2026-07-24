"""
Arquivo: urls.py
Caminho: apps/academico/urls.py
Descrição: URLs do módulo acadêmico
Atualizações:
 - 12/01/2026 - Adicionadas URLs de download e preview de certificados
 - 02/02/2026 - Refatoração para incluir views de gestão de matrícula
 - 24/07/2026 - Adicionadas URLs de gestao_matricula, processar_matricula e alterar_status_inscricao
"""

from django.urls import path
from . import views

app_name = 'academico'

urlpatterns = [
    # Gestão de Matrículas
    path('gestao-matricula/',
         views.gestao_matricula_view,
         name='gestao_matricula'),

    path('processar-matricula/',
         views.processar_matricula_view,
         name='processar_matricula'),

    path('alterar-status-inscricao/',
         views.alterar_status_inscricao_view,
         name='alterar_status_inscricao'),

    # Download individual
    path('certificado/<int:avaliacao_id>/download/',
         views.download_certificado_individual,
         name='download_certificado'),

    # Preview
    path('certificado/<int:avaliacao_id>/preview/',
         views.preview_certificado,
         name='preview_certificado'),

    # Download em lote
    path('certificados/download-lote/',
         views.download_certificados_lote,
         name='download_certificados_lote'),
]