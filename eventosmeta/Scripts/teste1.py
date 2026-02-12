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