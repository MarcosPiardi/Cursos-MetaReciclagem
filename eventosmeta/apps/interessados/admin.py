"""
Arquivo: apps/interessados/admin.py
Caminho: apps/interessados/admin.py
Alteração: Adicionado exportador de interessados com análise de critérios
Data: 10/12/2025
"""

"""
Admin do app INTERESSADOS - Sistema MetaReciclagem
Arquivo: apps/interessados/admin.py
Alteração: Adicionar campos is_active, is_staff, is_superuser para autenticação completa
Data: 05/12/2025
"""

"""
Admin do app INTERESSADOS - Sistema MetaReciclagem
Arquivo: apps/interessados/admin.py
Alteração: Corrigir nomes dos campos de PCD (adicionar prefixo pcd_) e remover campo inexistente
Data: 04/12/2025
"""

from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponse
from datetime import date
from decimal import Decimal
import csv

from .models import Interessado, Sexo, Fototipo


@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    """Administração de Sexo"""
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Fototipo)
class FototipoAdmin(admin.ModelAdmin):
    """Administração de Fototipo"""
    list_display = ['nome', 'descricao']
    search_fields = ['nome', 'descricao']


@admin.register(Interessado)
class InteressadoAdmin(admin.ModelAdmin):
    """Administração de Interessados"""
    
    # Listagem
    list_display = [
        'cpf',
        'nome',
        'data_nascimento',
        'cidade_residencia',
        'uf_residencia',
        'celular',
        'necessidades_especiais',
        'is_active_display',  # Adicionado em 05/12/2025
        'criado_em'
    ]
    
    # Filtros
    list_filter = [
        'is_active',  # Adicionado em 05/12/2025
        'sexo',
        'uf_residencia',
        'necessidades_especiais',
        'programa_social',
        'fototipo',
        'criado_em'
    ]
    
    # Busca
    search_fields = [
        'cpf',
        'nome',
        'email',
        'celular',
        'cidade_residencia',
        'bairro'
    ]
    
    # Campos somente leitura
    readonly_fields = ['criado_em', 'atualizado_em', 'last_login']
    
    # Organização do formulário
    fieldsets = (
        ('Dados Pessoais', {
            'fields': (
                'cpf',
                'nome',
                'rg',
                'sexo',
                'data_nascimento',
                'cidade_nascimento',
                'uf_nascimento',
                'nacionalidade',
                'fototipo',
                'escolaridade'
            )
        }),
        ('Endereço', {
            'fields': (
                'endereco_residencial',
                'num_endereco',
                'complemento',
                'bairro',
                'cidade_residencia',
                'uf_residencia'
            )
        }),
        ('Contatos', {
            'fields': (
                'telefone',
                'celular',
                'email'
            )
        }),
        ('Programa Social', {
            'fields': (
                'programa_social',
                'num_nis'
            ),
            'classes': ('collapse',)
        }),
        ('Necessidades Especiais / PCD', {
            'fields': (
                'necessidades_especiais',
                'pcd_fisica',
                'pcd_visual',
                'pcd_auditiva',
                'pcd_intelectual',
                'pcd_psicossocial',
                'pcd_multiplas'
            ),
            'classes': ('collapse',),
            'description': 'Marque as deficiências que o interessado possui'
        }),
        ('Responsável (Para menores de idade)', {
            'fields': (
                'nome_responsavel',
                'telefone_responsavel',
                'celular_responsavel',
                'email_responsavel'
            ),
            'classes': ('collapse',)
        }),
        ('🔐 Autenticação e Permissões', {
            'fields': (
                'senha',
                'last_login',
                'is_active',
                'is_staff',
                'is_superuser'
            ),
            'classes': ('collapse',),
            'description': (
                '<div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin-bottom: 15px;">'
                '<strong>📋 CONTROLE DE ACESSO AO SISTEMA:</strong><br><br>'
                '<strong>🔑 Senha:</strong> Digite a senha do interessado (será criptografada automaticamente)<br>'
                '<strong>🕒 Último Login:</strong> Data/hora do último acesso (preenchido automaticamente)<br><br>'
                '<strong>✅ Ativo:</strong> Permite que o interessado faça login no sistema<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcado = Pode fazer login<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Desmarcado = Login bloqueado<br><br>'
                '<strong>👔 Membro da Equipe:</strong> Permite acesso ao painel administrativo<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Normalmente DESMARCADO para interessados comuns<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcar apenas para funcionários/colaboradores<br><br>'
                '<strong>⚡ Superusuário:</strong> Concede todas as permissões do sistema<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Normalmente DESMARCADO<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcar apenas para administradores do sistema<br>'
                '</div>'
            )
        }),
        ('Observações', {
            'fields': ('observacao',)
        }),
        ('Informações do Sistema', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        })
    )
    
    # Ordenação
    ordering = ['nome']
    
    # Quantidade de itens por página
    list_per_page = 25
    
    # Actions
    actions = ['ativar_interessados', 'desativar_interessados', 'exportar_interessados_detalhado']
    
    def is_active_display(self, obj):
        """
        Exibe o status ativo/inativo com ícone colorido
        Adicionado em 05/12/2025
        """
        if obj.is_active:
            return format_html(
                '<span style="color: green; font-weight: bold;">✅ Ativo</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">❌ Inativo</span>'
        )
    is_active_display.short_description = 'Status'
    is_active_display.admin_order_field = 'is_active'
    
    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para garantir que a senha seja criptografada
        """
        if 'senha' in form.changed_data:
            # Se o campo senha foi alterado, criptografa
            obj.set_password(form.cleaned_data['senha'])
        super().save_model(request, obj, form, change)
    
    def ativar_interessados(self, request, queryset):
        """
        Action para ativar interessados selecionados
        Adicionado em 05/12/2025
        """
        count = queryset.update(is_active=True)
        self.message_user(
            request,
            f'✅ {count} interessado(s) ativado(s) com sucesso! Agora podem fazer login.'
        )
    ativar_interessados.short_description = '✅ Ativar interessados selecionados'
    
    def desativar_interessados(self, request, queryset):
        """
        Action para desativar interessados selecionados
        Adicionado em 05/12/2025
        """
        count = queryset.update(is_active=False)
        self.message_user(
            request,
            f'❌ {count} interessado(s) desativado(s)! Login bloqueado.',
            level='WARNING'
        )
    desativar_interessados.short_description = '❌ Desativar interessados selecionados'
    
    def exportar_interessados_detalhado(self, request, queryset):
        """
        Exporta interessados com análise detalhada de critérios que atendem
        Adicionado em 10/12/2025
        """
        from apps.eventos.models import Criterio
        
        # Criar resposta HTTP com CSV
        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = 'attachment; filename="interessados_analise_criterios.csv"'
        
        # Adicionar BOM para Excel reconhecer UTF-8
        response.write('\ufeff')
        
        writer = csv.writer(response, delimiter=';')
        
        # Buscar todos os critérios de PONTUACAO ativos
        criterios_pontuacao = Criterio.objects.filter(
            ativo=True,
            tipo_criterio='PONTUACAO'
        ).order_by('nome')
        
        # Cabeçalho base
        cabecalho = [
            'CPF',
            'Nome',
            'Data Nascimento',
            'Idade',
            'Sexo',
            'Fototipo',
            'Escolaridade',
            'Cidade/UF',
            'Telefone',
            'Celular',
            'Email',
            'Tem Deficiência',
            'Tipos PCD',
            'Programa Social',
            'NIS',
            'Status',
        ]
        
        # Adicionar colunas para cada critério
        for criterio in criterios_pontuacao:
            cabecalho.append(f'{criterio.nome} ({criterio.pontos} pts)')
        
        # Adicionar colunas finais
        cabecalho.extend([
            'Critérios Atendidos',
            'Pontuação Total Potencial'
        ])
        
        writer.writerow(cabecalho)
        
        # Processar cada interessado
        hoje = date.today()
        
        for interessado in queryset.select_related('sexo', 'fototipo'):
            # Calcular idade
            if interessado.data_nascimento:
                idade = hoje.year - interessado.data_nascimento.year - (
                    (hoje.month, hoje.day) < (interessado.data_nascimento.month, interessado.data_nascimento.day)
                )
            else:
                idade = 'N/A'
            
            # Tipos de PCD
            tipos_pcd = []
            if interessado.pcd_fisica:
                tipos_pcd.append('Física')
            if interessado.pcd_visual:
                tipos_pcd.append('Visual')
            if interessado.pcd_auditiva:
                tipos_pcd.append('Auditiva')
            if interessado.pcd_intelectual:
                tipos_pcd.append('Intelectual')
            if interessado.pcd_psicossocial:
                tipos_pcd.append('Psicossocial')
            if interessado.pcd_multiplas:
                tipos_pcd.append('Múltiplas')
            
            tipos_pcd_str = ', '.join(tipos_pcd) if tipos_pcd else 'Nenhuma'
            
            # Linha base
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
                tipos_pcd_str,
                'Sim' if interessado.programa_social else 'Não',
                interessado.num_nis or 'N/A',
                'Ativo' if interessado.is_active else 'Inativo',
            ]
            
            # Analisar cada critério
            criterios_atendidos = []
            pontuacao_total = 0
            
            for criterio in criterios_pontuacao:
                atende = False
                
                # PCD
                if criterio.codigo == 'PCD':
                    if interessado.tem_deficiencia:
                        atende = True
                
                # NIS
                elif criterio.codigo == 'NIS' or criterio.codigo == 'PROGRAMA_SOCIAL':
                    if interessado.programa_social and interessado.num_nis:
                        atende = True
                
                # JOVEM (16 a 24 anos)
                elif criterio.codigo == 'JOVEM' or (criterio.categoria == 'FAIXA_ETARIA' and '16' in criterio.nome and '24' in criterio.nome):
                    if isinstance(idade, int) and 16 <= idade <= 24:
                        atende = True
                
                # IDOSO (50+ anos)
                elif criterio.codigo == 'IDOSO' or (criterio.categoria == 'FAIXA_ETARIA' and ('50' in criterio.nome or 'Idoso' in criterio.nome)):
                    if isinstance(idade, int) and idade >= 50:
                        atende = True
                
                # IDOSO 60+
                elif criterio.categoria == 'FAIXA_ETARIA' and '60' in criterio.nome:
                    if isinstance(idade, int) and idade >= 60:
                        atende = True
                
                # COTA RACIAL
                elif criterio.categoria == 'COTA_RACIAL':
                    racas_cotistas = ['Preta', 'Parda', 'Indígena', 'Preto', 'Pardo', 'Indigena']
                    if interessado.fototipo and interessado.fototipo.nome in racas_cotistas:
                        atende = True
                
                # ESCOLARIDADE
                elif criterio.categoria == 'ESCOLARIDADE':
                    niveis_ordem = [
                        'FUNDAMENTAL_INCOMPLETO',
                        'FUNDAMENTAL_COMPLETO',
                        'MEDIO_INCOMPLETO',
                        'MEDIO_COMPLETO',
                        'SUPERIOR_INCOMPLETO',
                        'SUPERIOR_COMPLETO',
                        'POS_GRADUACAO'
                    ]
                    
                    # Identificar critério específico
                    if criterio.codigo == 'ESC_FUND_INC':
                        if interessado.escolaridade == 'FUNDAMENTAL_INCOMPLETO':
                            atende = True
                    elif criterio.codigo == 'ESC_FUND_COMP':
                        if interessado.escolaridade == 'FUNDAMENTAL_COMPLETO':
                            atende = True
                    elif criterio.codigo == 'ESC_MEDIO_INC':
                        if interessado.escolaridade == 'MEDIO_INCOMPLETO':
                            atende = True
                    elif criterio.codigo == 'ESC_MEDIO_COMP':
                        if interessado.escolaridade == 'MEDIO_COMPLETO':
                            atende = True
                    # Verificação por nível hierárquico
                    elif interessado.escolaridade and interessado.escolaridade in niveis_ordem:
                        nivel_minimo = None
                        if 'Fundamental Completo' in criterio.nome:
                            nivel_minimo = 'FUNDAMENTAL_COMPLETO'
                        elif 'Médio Completo' in criterio.nome or 'Medio Completo' in criterio.nome:
                            nivel_minimo = 'MEDIO_COMPLETO'
                        elif 'Superior' in criterio.nome:
                            nivel_minimo = 'SUPERIOR_COMPLETO'
                        
                        if nivel_minimo:
                            idx_interessado = niveis_ordem.index(interessado.escolaridade)
                            idx_minimo = niveis_ordem.index(nivel_minimo)
                            if idx_interessado >= idx_minimo:
                                atende = True
                
                # Adicionar resultado
                if atende:
                    linha.append('SIM')
                    criterios_atendidos.append(criterio.nome)
                    pontuacao_total += criterio.pontos or 0
                else:
                    linha.append('NÃO')
            
            # Adicionar totalizadores
            linha.append(', '.join(criterios_atendidos) if criterios_atendidos else 'Nenhum')
            linha.append(f'{pontuacao_total:.2f}')
            
            writer.writerow(linha)
        
        messages.success(request, f'✅ {queryset.count()} interessado(s) exportado(s) com sucesso!')
        return response
    
    exportar_interessados_detalhado.short_description = '📊 Exportar interessados com análise de critérios (Excel)'

