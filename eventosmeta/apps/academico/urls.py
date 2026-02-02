"""
Arquivo: urls.py
Caminho: apps/academico/urls.py
Descrição: URLs do módulo acadêmico
Data: 12/01/2026
"""

"""
URLs do app ACADÊMICO
Arquivo: apps/academico/urls.py
Data: 02/02/2026
"""

from django.urls import path
from . import views

app_name = 'academico'

urlpatterns = [
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

