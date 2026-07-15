"""
Arquivo: admin.py
Caminho: apps/interessados/admin.py
Alteração: Corrigido format_html dos ícones e adicionado white-space nowrap nos telefones
Data: 11/12/2025
Alteração: Registrados todos os models no admin_site customizado (melhor prática)
Data: 20/01/2026
Alteração: Adicionado PasswordResetTokenAdmin com actions de limpeza
Data: 20/02/2026
Alteração: Adicionada ação 'Gerar Senha Provisória' para Interessados
           Senha de 8 caracteres exibida uma única vez na tela
           Campo must_change_password marcado como True automaticamente
           Adicionado must_change_password em list_display, list_filter e fieldsets
Data: 25/02/2026
"""

import secrets
import string
from datetime import date

from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.http import HttpResponse
import csv

from .models import Interessado, Sexo, Fototipo, PasswordResetToken


# 
# ADMIN: SEXO
# 

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display  = ['nome']
    search_fields = ['nome']


@admin.register(Fototipo)
class FototipoAdmin(admin.ModelAdmin):
    list_display  = ['nome', 'descricao']
    search_fields = ['nome', 'descricao']


# 
# ADMIN: INTERESSADO
# 

@admin.register(Interessado)
class InteressadoAdmin(admin.ModelAdmin):
    """Administração de Interessados"""

    list_display = [
        'cpf',
        'nome',
        'data_nascimento_formatada',
        'sexo_display',
        'fototipo_display',
        'programa_social_display',
        'necessidades_especiais_display',
        'celular_formatado',
        'telefone_formatado',
        'email',
        'must_change_password',          # ← adicionado 25/02/2026
    ]

    list_filter = [
        'is_active',
        'must_change_password',          # ← adicionado 25/02/2026
        'sexo',
        'uf_residencia',
        'necessidades_especiais',
        'programa_social',
        'fototipo',
        'criado_em',
    ]

    search_fields = [
        'cpf', 'nome', 'email', 'celular',
        'cidade_residencia', 'bairro',
    ]

    readonly_fields = ['criado_em', 'atualizado_em', 'last_login']

    fieldsets = (
        ('Dados Pessoais', {
            'fields': (
                'cpf', 'nome', 'rg', 'sexo',
                'data_nascimento', 'cidade_nascimento',
                'uf_nascimento', 'nacionalidade',
                'fototipo', 'escolaridade',
            )
        }),
        ('Endereço', {
            'fields': (
                'endereco_residencial', 'num_endereco',
                'complemento', 'bairro',
                'cidade_residencia', 'uf_residencia',
            )
        }),
        ('Contatos', {
            'fields': ('telefone', 'celular', 'email')
        }),
        ('Programa Social', {
            'fields': ('programa_social', 'num_nis'),
            'classes': ('collapse',),
        }),
        ('Necessidades Especiais / PCD', {
            'fields': (
                'necessidades_especiais',
                'pcd_fisica', 'pcd_visual', 'pcd_auditiva',
                'pcd_intelectual', 'pcd_psicossocial', 'pcd_multiplas',
            ),
            'classes': ('collapse',),
            'description': 'Marque as deficiências que o interessado possui',
        }),
        ('Responsável (Para menores de idade)', {
            'fields': (
                'nome_responsavel', 'telefone_responsavel',
                'celular_responsavel', 'email_responsavel',
            ),
            'classes': ('collapse',),
        }),
        ('🔐 Autenticação e Permissões', {
            'fields': (
                'senha', 'last_login',
                'is_active', 'is_staff', 'is_superuser',
            ),
            'classes': ('collapse',),
            'description': (
                '<div style="background-color: #f8f9fa; padding: 15px; '
                'border-left: 4px solid #007bff; margin-bottom: 15px;">'
                '<strong>📋 CONTROLE DE ACESSO AO SISTEMA:</strong><br><br>'
                '<strong>🔑 Senha:</strong> Digite a senha (será criptografada automaticamente)<br>'
                '<strong>✅ Ativo:</strong> Permite que o interessado faça login<br>'
                '<strong>👔 Membro da Equipe:</strong> Acesso ao painel administrativo<br>'
                '<strong>⚡ Superusuário:</strong> Todas as permissões do sistema'
                '</div>'
            ),
        }),
        # ── Adicionado: 25/02/2026 ──
        ('🔑 Senha Provisória', {
            'fields': ('must_change_password',),
            'classes': ('collapse',),
            'description': (
                'Use a ação "Gerar Senha Provisória" na listagem para gerar '
                'uma senha aleatória e marcar este campo automaticamente. '
                'Quando marcado, o interessado será obrigado a trocar a senha no próximo login.'
            ),
        }),
        ('Observações', {
            'fields': ('observacao',),
        }),
        ('Informações do Sistema', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )

    ordering      = ['nome']
    list_per_page = 25
    actions       = [
        'gerar_senha_provisoria',            # ← adicionado 25/02/2026
        'ativar_interessados',
        'desativar_interessados',
        'exportar_interessados_detalhado',
    ]

    # 
    # MÉTODOS LIST_DISPLAY
    # 

    def data_nascimento_formatada(self, obj):
        if obj.data_nascimento:
            return format_html(
                '<div style="text-align: center;">{}</div>',
                obj.data_nascimento.strftime('%d/%m/%Y')
            )
        return format_html('<div style="text-align: center;">—</div>')
    data_nascimento_formatada.short_description = 'Data Nascimento'
    data_nascimento_formatada.admin_order_field = 'data_nascimento'

    def sexo_display(self, obj):
        return obj.sexo.nome if obj.sexo else '—'
    sexo_display.short_description = 'Sexo'
    sexo_display.admin_order_field = 'sexo__nome'

    def fototipo_display(self, obj):
        fototipo = obj.fototipo.nome if obj.fototipo else '—'
        return format_html(
            '<div style="text-align: center;">{}</div>', fototipo
        )
    fototipo_display.short_description = 'Fototipo'
    fototipo_display.admin_order_field = 'fototipo__nome'

    def programa_social_display(self, obj):
        if obj.programa_social:
            return format_html(
                '<div style="text-align: center;">'
                '<span style="color: #28a745; font-weight: bold;">✅</span>'
                '</div>'
            )
        return format_html(
            '<div style="text-align: center;">'
            '<span style="color: #6c757d;">—</span>'
            '</div>'
        )
    programa_social_display.short_description = 'Programa Social'
    programa_social_display.admin_order_field = 'programa_social'

    def necessidades_especiais_display(self, obj):
        if obj.necessidades_especiais or obj.tem_deficiencia:
            return format_html(
                '<div style="text-align: center;">'
                '<span style="color: #007bff; font-weight: bold;">♿</span>'
                '</div>'
            )
        return format_html(
            '<div style="text-align: center;">'
            '<span style="color: #6c757d;">—</span>'
            '</div>'
        )
    necessidades_especiais_display.short_description = 'Necessidades Especiais'
    necessidades_especiais_display.admin_order_field = 'necessidades_especiais'

    def celular_formatado(self, obj):
        if obj.celular:
            numeros = ''.join(filter(str.isdigit, obj.celular))
            if len(numeros) == 11:
                formatado = f'({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}'
            elif len(numeros) == 10:
                formatado = f'({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}'
            else:
                formatado = obj.celular
            return format_html(
                '<div style="text-align: center; white-space: nowrap;">{}</div>',
                formatado
            )
        return format_html('<div style="text-align: center;">—</div>')
    celular_formatado.short_description = 'Celular'
    celular_formatado.admin_order_field = 'celular'

    def telefone_formatado(self, obj):
        if obj.telefone:
            numeros = ''.join(filter(str.isdigit, obj.telefone))
            if len(numeros) == 11:
                formatado = f'({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}'
            elif len(numeros) == 10:
                formatado = f'({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}'
            else:
                formatado = obj.telefone
            return format_html(
                '<div style="text-align: center; white-space: nowrap;">{}</div>',
                formatado
            )
        return format_html('<div style="text-align: center;">—</div>')
    telefone_formatado.short_description = 'Telefone'
    telefone_formatado.admin_order_field = 'telefone'

    def is_active_display(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="color: green; font-weight: bold;">✅ Ativo</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">❌ Inativo</span>'
        )
    is_active_display.short_description = 'Status'
    is_active_display.admin_order_field = 'is_active'

    # 
    # SAVE MODEL
    # 

    def save_model(self, request, obj, form, change):
        if 'senha' in form.changed_data:
            obj.set_password(form.cleaned_data['senha'])
        super().save_model(request, obj, form, change)

    # 
    # ACTIONS
    # 

    # ── Adicionado: 25/02/2026 ──
    @admin.action(description='🔑 Gerar Senha Provisória')
    def gerar_senha_provisoria(self, request, queryset):
        """
        Gera senha aleatória de 8 caracteres para o interessado selecionado.
        Exibe a senha UMA ÚNICA VEZ na tela para o Staff anotar e entregar
        presencialmente. Marca must_change_password = True automaticamente.
        """
        if queryset.count() != 1:
            self.message_user(
                request,
                '⚠️ Selecione exatamente 1 interessado para gerar a senha provisória.',
                level=messages.WARNING,
            )
            return

        interessado = queryset.first()

        # Gera senha com letras maiúsculas, minúsculas e dígitos
        alfabeto = string.ascii_letters + string.digits
        senha    = ''.join(secrets.choice(alfabeto) for _ in range(8))

        # Aplica a senha e marca troca obrigatória
        interessado.set_password(senha)
        interessado.must_change_password = True
        interessado.save()

        # Exibe a senha UMA ÚNICA VEZ no topo da página
        self.message_user(
            request,
            format_html(
                '<strong>✅ Senha provisória gerada para {}:</strong> '
                '<code style="font-size:1.2em; background:#f0f0f0; padding:4px 10px;">{}</code>'
                ' — Anote e entregue presencialmente. Esta senha não será exibida novamente.',
                interessado.nome,
                senha,
            ),
            level=messages.SUCCESS,
        )

    def ativar_interessados(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(
            request,
            f'✅ {count} interessado(s) ativado(s) com sucesso!'
        )
    ativar_interessados.short_description = '✅ Ativar interessados selecionados'

    def desativar_interessados(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(
            request,
            f'❌ {count} interessado(s) desativado(s)! Login bloqueado.',
            level='WARNING',
        )
    desativar_interessados.short_description = '❌ Desativar interessados selecionados'

    def exportar_interessados_detalhado(self, request, queryset):
        """Exporta interessados com análise detalhada de critérios"""
        from apps.eventos.models import Criterio

        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = (
            'attachment; filename="interessados_analise_criterios.csv"'
        )
        response.write('\ufeff')

        writer = csv.writer(response, delimiter=';')
        criterios_pontuacao = Criterio.objects.filter(
            ativo=True, tipo_criterio='PONTUACAO'
        ).order_by('nome')

        cabecalho = [
            'CPF', 'Nome', 'Data Nascimento', 'Idade', 'Sexo',
            'Fototipo', 'Escolaridade', 'Cidade/UF', 'Telefone',
            'Celular', 'Email', 'Tem Deficiência', 'Tipos PCD',
            'Programa Social', 'NIS', 'Status',
        ]
        for criterio in criterios_pontuacao:
            cabecalho.append(f'{criterio.nome} ({criterio.pontos} pts)')
        cabecalho.extend(['Critérios Atendidos', 'Pontuação Total Potencial'])
        writer.writerow(cabecalho)

        hoje = date.today()

        for interessado in queryset.select_related('sexo', 'fototipo'):
            if interessado.data_nascimento:
                idade = hoje.year - interessado.data_nascimento.year - (
                    (hoje.month, hoje.day) <
                    (interessado.data_nascimento.month, interessado.data_nascimento.day)
                )
            else:
                idade = 'N/A'

            tipos_pcd = []
            if interessado.pcd_fisica:       tipos_pcd.append('Física')
            if interessado.pcd_visual:       tipos_pcd.append('Visual')
            if interessado.pcd_auditiva:     tipos_pcd.append('Auditiva')
            if interessado.pcd_intelectual:  tipos_pcd.append('Intelectual')
            if interessado.pcd_psicossocial: tipos_pcd.append('Psicossocial')
            if interessado.pcd_multiplas:    tipos_pcd.append('Múltiplas')

            linha = [
                interessado.cpf,
                interessado.nome,
                interessado.data_nascimento.strftime('%d/%m/%Y') if interessado.data_nascimento else 'N/A',
                idade,
                interessado.sexo.nome if interessado.sexo else 'N/A',
                interessado.fototipo.nome if interessado.fototipo else 'N/A',
                interessado.get_escolaridade_display() if interessado.escolaridade else 'N/A',
                f"{interessado.cidade_residencia}/{interessado.uf_residencia}" if interessado.cidade_residencia else 'N/A',
                interessado.telefone or 'N/A',
                interessado.celular or 'N/A',
                interessado.email or 'N/A',
                'Sim' if interessado.tem_deficiencia else 'Não',
                ', '.join(tipos_pcd) if tipos_pcd else 'Nenhuma',
                'Sim' if interessado.programa_social else 'Não',
                interessado.num_nis or 'N/A',
                'Ativo' if interessado.is_active else 'Inativo',
            ]

            criterios_atendidos = []
            pontuacao_total     = 0

            for criterio in criterios_pontuacao:
                atende = False
                if criterio.codigo == 'PCD':
                    atende = interessado.tem_deficiencia
                elif criterio.codigo in ('NIS', 'PROGRAMA_SOCIAL'):
                    atende = interessado.programa_social and bool(interessado.num_nis)
                linha.append('SIM' if atende else 'NÃO')
                if atende:
                    criterios_atendidos.append(criterio.nome)
                    pontuacao_total += criterio.pontos or 0

            linha.append(', '.join(criterios_atendidos) if criterios_atendidos else 'Nenhum')
            linha.append(f'{pontuacao_total:.2f}')
            writer.writerow(linha)

        messages.success(
            request,
            f'✅ {queryset.count()} interessado(s) exportado(s) com sucesso!'
        )
        return response
    exportar_interessados_detalhado.short_description = (
        '📊 Exportar interessados com análise de critérios (Excel)'
    )


# 
# ADMIN: PASSWORD RESET TOKEN
# Alteração: 20/02/2026
# 

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    """
    Administração dos tokens de recuperação de senha.
    Permite visualizar e limpar tokens expirados ou usados.
    """

    list_display = [
        'get_interessado',
        'get_cpf',
        'get_status',
        'criado_em_formatado',
        'expira_em_formatado',
        'usado',
    ]

    list_filter   = ['usado', 'criado_em']
    search_fields = ['interessado__nome', 'interessado__cpf', 'token']
    ordering      = ['-criado_em']
    readonly_fields = ['token', 'interessado', 'criado_em', 'expira_em', 'usado']
    list_per_page = 25

    actions = [
        'limpar_tokens_expirados',
        'limpar_tokens_usados',
        'limpar_todos_invalidos',
    ]

    # 
    # MÉTODOS LIST_DISPLAY
    # 

    def get_interessado(self, obj):
        return obj.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'interessado__nome'

    def get_cpf(self, obj):
        cpf = obj.interessado.cpf
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    get_cpf.short_description = 'CPF'

    def get_status(self, obj):
        agora = timezone.now()
        if obj.usado:
            return format_html(
                '<span style="display:inline-block;padding:3px 8px;'
                'background:#6c757d;color:white;border-radius:12px;font-size:11px;">'
                '✔️ Usado</span>'
            )
        elif agora > obj.expira_em:
            return format_html(
                '<span style="display:inline-block;padding:3px 8px;'
                'background:#dc3545;color:white;border-radius:12px;font-size:11px;">'
                '⏰ Expirado</span>'
            )
        else:
            minutos = int((obj.expira_em - agora).total_seconds() // 60)
            return format_html(
                '<span style="display:inline-block;padding:3px 8px;'
                'background:#28a745;color:white;border-radius:12px;font-size:11px;">'
                '✅ Válido (~{}min)</span>',
                minutos,
            )
    get_status.short_description = 'Status'

    def criado_em_formatado(self, obj):
        return obj.criado_em.strftime('%d/%m/%Y %H:%M')
    criado_em_formatado.short_description = 'Criado em'
    criado_em_formatado.admin_order_field = 'criado_em'

    def expira_em_formatado(self, obj):
        return obj.expira_em.strftime('%d/%m/%Y %H:%M')
    expira_em_formatado.short_description = 'Expira em'
    expira_em_formatado.admin_order_field = 'expira_em'

    # 
    # ACTIONS DE LIMPEZA
    # 

    def limpar_tokens_expirados(self, request, queryset):
        agora     = timezone.now()
        expirados = queryset.filter(expira_em__lt=agora)
        total     = expirados.count()
        expirados.delete()
        self.message_user(
            request,
            f'🗑️ {total} token(s) expirado(s) removido(s) com sucesso!',
            level=messages.SUCCESS,
        )
    limpar_tokens_expirados.short_description = '🗑️ Remover tokens EXPIRADOS selecionados'

    def limpar_tokens_usados(self, request, queryset):
        usados = queryset.filter(usado=True)
        total  = usados.count()
        usados.delete()
        self.message_user(
            request,
            f'🗑️ {total} token(s) já utilizado(s) removido(s) com sucesso!',
            level=messages.SUCCESS,
        )
    limpar_tokens_usados.short_description = '🗑️ Remover tokens JÁ USADOS selecionados'

    def limpar_todos_invalidos(self, request, queryset):
        agora    = timezone.now()
        invalidos = PasswordResetToken.objects.filter(
            models.Q(expira_em__lt=agora) | models.Q(usado=True)
        )
        total = invalidos.count()
        invalidos.delete()
        self.message_user(
            request,
            f'🧹 Limpeza completa: {total} token(s) inválido(s) removido(s) do banco!',
            level=messages.SUCCESS,
        )
    limpar_todos_invalidos.short_description = '🧹 Limpar TODOS os tokens inválidos do banco'

    # 
    # PERMISSÕES — SOMENTE LEITURA + LIMPEZA
    # 

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser




