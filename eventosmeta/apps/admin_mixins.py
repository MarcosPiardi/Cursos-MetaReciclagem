
"""
mixins.py
Arquivo: apps/admin_mixins.py
Finalidade: Mixins para customização do admin 
Atualizações:
    - 28/07/2026 - Criação do arquivo e implementação do CustomTitleMixin
"""


class CustomTitleMixin:
    custom_title = None

    def _set_title(self, extra_context):
        extra_context = extra_context or {}
        if self.custom_title:
            extra_context['title'] = self.custom_title
        return extra_context

    def changelist_view(self, request, extra_context=None):
        return super().changelist_view(request, extra_context=self._set_title(extra_context))

    def add_view(self, request, extra_context=None):
        return super().add_view(request, extra_context=self._set_title(extra_context))

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=self._set_title(extra_context))