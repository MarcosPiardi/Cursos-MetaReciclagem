from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")


eventosmeta/
├── apps/
│   └── academico/
│       ├── views.py          ← CRIAR/ATUALIZAR
│       ├── urls.py           ← CRIAR NOVO
│       ├── services.py       ← CRIAR NOVO
│       ├── admin.py          ← ATUALIZAR
│       └── templates/
│           └── academico/
│               └── gestao_matricula.html  ← CRIAR NOVO
└── eventosmeta/
    └── urls.py               ← ATUALIZAR