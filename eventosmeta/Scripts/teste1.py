from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")

eventosmeta/
├── config/
│   ├── settings.py ✅ (ATIVO)
│   ├── urls.py ✅ (ATIVO)
│   └── wsgi.py ✅ (presumido)
│
├── apps/
│   ├── academico/
│   │   ├── models.py ✅ (ATIVO - Matricula, Turma, StatusMatricula)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO)
│   │   ├── apps.py ✅ (ATIVO)
│   │   ├── services.py ✅ (ATIVO - MatriculaService)
│   │   ├── urls.py ✅ (ATIVO)
│   │   └── templates/
│   │       └── academico/
│   │           └── gestao_matricula.html ✅ (ATIVO)
│   │
│   ├── accounts/
│   │   ├── models.py ✅ (ATIVO - Usuario customizado)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO)
│   │   ├── apps.py ✅ (ATIVO)
│   │   ├── forms.py ✅ (ATIVO - LoginStaffForm)
│   │   ├── urls.py ✅ (ATIVO)
│   │   └── templates/
│   │       └── accounts/
│   │           ├── dashboard_staff.html ✅ (ATIVO)
│   │           └── login_staff.html ✅ (ATIVO)
│   │
│   ├── eventos/
│   │   ├── models.py ✅ (ATIVO - Evento, Criterio, EventoCriterio, Status)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO)
│   │   ├── apps.py ✅ (ATIVO)
│   │   └── urls.py ✅ (ATIVO - vazio mas configurado)
│   │
│   ├── interessados/
│   │   ├── models.py ✅ (ATIVO - Interessado, Sexo, Fototipo)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO)
│   │   ├── apps.py ✅ (ATIVO)
│   │   ├── authentication.py ✅ (ATIVO - InteressadoBackend)
│   │   ├── forms.py ✅ (ATIVO - CadastroInteressadoForm, LoginInteressadoForm)
│   │   ├── urls.py ✅ (ATIVO)
│   │   ├── templates/
│   │   │   └── interessados/
│   │   │       ├── base.html ✅ (ATIVO)
│   │   │       ├── cadastro.html ✅ (ATIVO)
│   │   │       ├── dashboard.html ✅ (ATIVO)
│   │   │       ├── detalhes.html ✅ (ATIVO)
│   │   │       ├── sucesso.html ✅ (ATIVO)
│   │   │       ├── login_interessado.html ✅ (ATIVO)
│   │   │       ├── form_interessados.html ❌ (NÃO USADO?)
│   │   │       └── lista_interessados.html ❌ (NÃO USADO?)
│   │   └── static/
│   │       └── interessados/
│   │           └── formStyles.css ✅ (ATIVO)
│   │
│   ├── portal/
│   │   ├── models.py ✅ (ATIVO - vazio mas existente)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO - vazio)
│   │   ├── apps.py ✅ (ATIVO)
│   │   ├── forms.py ✅ (ATIVO)
│   │   ├── urls.py ✅ (ATIVO)
│   │   └── templates/
│   │       └── portal/
│   │           ├── base.html ✅ (ATIVO)
│   │           ├── index.html ✅ (ATIVO - página inicial pública)
│   │           ├── consulta_publica.html ✅ (ATIVO)
│   │           ├── resultado_evento.html ✅ (ATIVO)
│   │           ├── dashboard.html ❌ (NÃO USADO?)
│   │           └── login.html ❌ (NÃO USADO?)
│   │
│   ├── selecao/
│   │   ├── models.py ✅ (ATIVO - Inscricao, Classificacao, StatusInscricao)
│   │   ├── views.py ✅ (ATIVO)
│   │   ├── admin.py ✅ (ATIVO)
│   │   ├── apps.py ✅ (ATIVO)
│   │   ├── services.py ✅ (ATIVO - ClassificadorService)
│   │   └── templates/
│   │       └── selecao/
│   │           ├── relatorio_aprovados_mural.html ✅ (ATIVO)
│   │           └── relatorio_aprovados_staff.html ✅ (ATIVO)
│   │
│   └── scripts_admin/
│       └── (management commands) ✅ (ATIVO)
│
├── template/ (templates globais)
│   ├── admin/
│   │   └── base_site.html ✅ (ATIVO - customização admin)
│   ├── base.html ⚠️ (VERIFICAR SE USADO)
│   └── index.html ❌ (DUPLICADO - NÃO USADO)
│
└── static/
    └── css/
        └── style.css ✅ (ATIVO)



        template/
├── base.html              ← Base global (duplicada?)
└── index.html             ← Index duplicado

apps/interessados/templates/interessados/
└── base.html              ← Base só para interessados

apps/portal/templates/portal/
├── base.html              ← Base só para portal
├── index.html             ← Index do portal
├── login.html             ← Login não usado
└── dashboard.html         ← Dashboard não usado

apps/accounts/templates/accounts/
├── login_staff.html       ← Login específico
└── dashboard_staff.html   ← Dashboard específico





templates/                          ← Templates GLOBAIS (usados por todos)
├── base.html                       ← Base principal (header, footer, menu)
├── components/                     ← Componentes reutilizáveis
│   ├── navbar.html                 ← Menu de navegação
│   ├── footer.html                 ← Rodapé
│   ├── messages.html               ← Mensagens de alerta
│   └── pagination.html             ← Paginação
│
apps/portal/templates/portal/       ← Templates PÚBLICOS (visitantes)
├── index.html                      ← Página inicial pública
├── consulta_publica.html           ← Consulta de resultados
└── resultado_evento.html           ← Detalhes do resultado

apps/interessados/templates/interessados/  ← Área do INTERESSADO
├── base_interessado.html           ← Base específica (herda de base.html)
├── cadastro.html                   ← Formulário de cadastro
├── login.html                      ← Login do interessado
├── dashboard.html                  ← Painel do interessado
├── detalhes.html                   ← Detalhes da inscrição
└── sucesso.html                    ← Confirmação de cadastro

apps/accounts/templates/accounts/   ← Área da EQUIPE (staff)
├── base_staff.html                 ← Base específica (herda de base.html)
├── login_staff.html                ← Login da equipe
└── dashboard_staff.html            ← Painel da equipe

apps/selecao/templates/selecao/     ← Relatórios
├── relatorio_aprovados_mural.html  ← Mural público
└── relatorio_aprovados_staff.html  ← Relatório staff

apps/academico/templates/academico/ ← Gestão acadêmica
└── gestao_matricula.html           ← Gestão de matrículas


apps/accounts/
└── templates/
    ├── accounts/
    │   ├── login_staff.html
    │   └── dashboard_staff.html (pode manter vazio ou excluir)
    └── admin/                    ← NOVO
        ├── dashboard.html        ← CRIAR ESTE
        └── base_site.html        ← CRIAR ESTE (opcional)