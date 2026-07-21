
Aja como um arquiteto de software experiente e analise o arquivo anexo “arquitetura1.pdf”.

Seu objetivo é produzir uma avaliação completa e prática da arquitetura do projeto, com foco em organização, manutenção e refatoração segura.

Entregue a resposta em português, com seções numeradas e objetivas, cobrindo obrigatoriamente:

1. Mapa completo da arquitetura
- Identifique a estrutura geral do projeto
- Descreva os módulos, camadas, diretórios e relações entre componentes
- Sempre que possível, explique a função de cada parte

2. Diagnóstico dos problemas
- Aponte inconsistências, duplicações, acoplamentos excessivos, má organização, arquivos obsoletos e outros problemas arquiteturais
- Explique o impacto de cada problema

3. Proposta de reorganização dos diretórios
- Sugira uma nova estrutura de diretórios mais clara, consistente e escalável
- Justifique as principais mudanças

4. Proposta de padronização dos nomes
- Indique padrões para nomes de arquivos, diretórios, templates, componentes e rotas
- Considere consistência, legibilidade e manutenção

5. Lista de arquivos que podem ser eliminados
- Inclua apenas arquivos que parecem realmente desnecessários, duplicados, obsoletos ou mortos
- Informe o motivo de cada eliminação

6. Lista de arquivos que precisam ser movidos
- Indique quais arquivos devem ser realocados
- Informe a origem, o destino sugerido e a justificativa

7. Rotas quebradas
- Identifique rotas inexistentes, inconsistentes, apontando para arquivos ausentes ou com referência incorreta
- Destaque possíveis causas

8. Templates órfãos
- Liste templates não referenciados ou sem uso aparente
- Explique como concluiu isso

9. Ordem correta para fazer a refatoração sem quebrar o sistema
- Proponha uma sequência de refatoração priorizando segurança, baixo risco e dependências
- Organize a ordem por etapas numeradas
- Explique brevemente o objetivo de cada etapa

Requisitos adicionais:
- Baseie-se exclusivamente no conteúdo do PDF anexo
- Não invente informações que não estejam no arquivo
- Se houver ambiguidade ou falta de dados, sinalize isso explicitamente
- Seja específico e use evidências extraídas do documento sempre que possível
- Se identificar limitações na análise, informe-as no final
- Priorize uma resposta prática, técnica e acionável

Formato de saída esperado:
- Use títulos claros para cada seção
- Use listas quando apropriado
- Seja direto, técnico e organizado


IA:

Vou analisar o arquivo arquitetura1.pdf para fazer uma avaliação completa da arquitetura do projeto.

---

## AVALIAÇÃO ARQUITETURAL — METARECICLAGEM
**Data: 17/07/2026**

---

## 1. MAPA COMPLETO DA ARQUITETURA

### Estrutura Geral
O projeto MetaReciclagem segue o padrão **MVT (Model-View-Template)** do Django com **Service Layer** isolada. A arquitetura é modular, dividida em **8 aplicações (apps)** dentro da pasta `apps/`, complementadas por configuração centralizada em `config/`.

### Módulos e Camadas Detectadas

**Aplicações Principais:**
- **accounts**: Autenticação e permissões do corpo técnico (staff)
- **interessados**: Ciclo de vida do candidato externo (cadastro, login, perfil)
- **eventos**: Gestão de cursos, turmas, editais e vagas
- **selecao**: Core inteligente (motor de pontuação, ranking, classificação)
- **academico**: Pós-seleção (matrícula, notas, frequência, certificados)
- **portal**: Interface pública (consultas, inscrições, contatos)
- **dashboard**: Relatórios analíticos e indicadores (Excel/PDF)
- **scripts_admin**: Utilitários e comandos de manutenção

**Camadas Estruturais Identificadas:**
- Models (ORM Django com UUIDs como PKs)
- Views (FBV — Function-Based Views)
- Templates (HTML com herança Django)
- Services (Lógica complexa isolada)
- Forms (Validação de entrada)
- Middleware (Autenticação, CSP)
- Management Commands (Utilitários)
- Testes (pytest com factory-boy)

**Infraestrutura:**
- PostgreSQL 15+ (banco de dados)
- Django 5.2.4 (framework)
- Python 3.13.2 (linguagem)
- Segurança: django-axes, django-csp, django-encrypted-model-fields
- Email: CustomEmailBackend (SMTP municipal 10.28.10.54:587)

---

## 2. DIAGNÓSTICO DOS PROBLEMAS

### 2.1 Rotas Quebradas (NoReverseMatch)
**Impacto: CRÍTICO** — Falhas em tempo de execução ao renderizar templates.

**Rotas Inexistentes Identificadas:**
1. `academico:gestao_matricula` — chamada em `gestao_matricula.html`
2. `academico:processar_matricula` — chamada em `gestao_matricula.html`
3. `academico:alterar_status_inscricao` — chamada em `gestao_matricula.html`
4. `staff_senha_recuperar` — chamada em múltiplos templates de accounts
5. `staff_senha_redefinir` — chamada em múltiplos templates de accounts
6. `accounts:senha_recuperar` — chamada em `confirmar.html`
7. `admin:dashboard` — chamada em `base_site.html`
8. `admin:eventos_evento_changelist` — chamada em `dashboard.html`
9. `admin:interessados_interessado_changelist` — chamada em `dashboard.html`
10. `admin:selecao_inscricao_changelist` — chamada em `dashboard.html`
11. `admin:selecao_classificacao_changelist` — chamada em `matricular_alunos.html`

**Causa Raiz:** Falta de definição de rotas em `urls.py` ou nomes de rotas não parametrizados com `name=` em `path()`.

---

### 2.2 Templates Órfãos (Não Referenciados)
**Impacto: MÉDIO** — Código morto, confusão de manutenção, desperdício de espaço.

**Templates Órfãos Detectados (19 arquivos):**
- `apps/selecao/templates/selecao/relatorio_aprovados_mural.html`
- `apps/selecao/templates/selecao/relatorio_aprovados_staff.html`
- `apps/interessados/templates/interessados/senha/email_recuperar.html`
- `apps/academico/templates/academico/gestao_matricula.html`
- `apps/accounts/templates/accounts/exclusao/listar.html`
- `apps/accounts/templates/accounts/exclusao/detalhe.html`
- `apps/accounts/templates/accounts/senha/adm_redefinir.html`
- `apps/accounts/templates/accounts/senha/adm_redefinir_concluido.html`
- `apps/accounts/templates/accounts/senha/adm_recuperar.html`
- `apps/accounts/templates/accounts/senha/adm_recuperar_enviado.html`
- `apps/accounts/templates/accounts/senha/adm_email_recuperar.html`
- `apps/accounts/templates/accounts/senha/confirmar.html`
- `apps/interessados/templates/interessados/exclusao/solicitar.html`
- `apps/interessados/templates/interessados/exclusao/solicitada.html`
- `apps/selecao/templates/admin/selecao/matricular_alunos.html`
- `apps/accounts/templates/admin/accounts/cards-admin.html`
- `apps/academico/templates/admin/academico/avaliacao/change_list.html`
- `apps/dashboard/templates/admin/dashboard/base_dashboard.html`
- `apps/accounts/templates/admin/dashboard.html`

**Causa Raiz:** Refatorações anteriores que removeram views sem limpar templates correspondentes.

---

### 2.3 Duplicação de Templates
**Impacto: MÉDIO** — Risco de colisão de namespaces, inconsistência visual.

**Arquivo Duplicado:**
- `dashboard.html` existe em:
  - `apps/accounts/templates/admin/dashboard.html`
  - `apps/interessados/templates/interessados/dashboard.html`

**Causa Raiz:** Falta de convenção de nomenclatura única e organização de templates por contexto.

---

### 2.4 Arquivos Soltos na Raiz
**Impacto: BAIXO** — Desorganização, confusão visual, dificulta limpeza.

**Arquivos Identificados:**
- `15-07-2026-estrutura-html.txt`
- `16-07-2026-estrutura-html.txt`
- `16-07-2026-estrutura-html2.txt`
- `backup.sql`
- `analise_arquitetura.md`
- `analisar_arquitetura.py`
- `investigar_templates.ps1`
- `limpar_tokens.bat`
- `desktop.ini`

**Causa Raiz:** Ausência de pasta temporária ou estrutura de arquivamento de artefatos de análise.

---

### 2.5 Lacunas de Documentação e Mapeamento
**Impacto: MÉDIO** — Dificulta manutenção e onboarding.

- Falta mapeamento completo de campos das tabelas (apenas 3 de 8 apps documentadas)
- Ausência de rotas explícitas para `eventos` e `scripts_admin` no relatório
- Configurações em `settings.py` não expostas (TEMPLATES, LANGUAGE_CODE, TIME_ZONE, STATICFILES_DIRS)
- Nomes de rotas acoplados a nomes de arquivos em alguns registros

---

### 2.6 Acoplamento Excessivo em Nomes de Rotas
**Impacto: BAIXO** — Dificulta refatoração de templates.

Alguns registros de rotas mapeiam o nome do arquivo de template como identificador da rota, em vez de usar `name=` parametrizado em `path()`.

---

## 3. PROPOSTA DE REORGANIZAÇÃO DOS DIRETÓRIOS

### Estrutura Proposta

```text
eventosmeta/
├── .env
├── .env.example
├── .env.prod
├── .coveragerc
├── .dockerignore
├── conftest.py
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
├── manage.py
├── docker-compose.yml
├── docker-compose-prod.yml
├── Dockerfile
├── entrypoint.sh
├── nginx.conf
│
├── .vscode/
│   └── settings.json
│
├── apps/
│   ├── __init__.py
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── middleware.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── views_exclusao.py
│   │   ├── migrations/
│   │   ├── services/
│   │   ├── templates/
│   │   │   └── accounts/
│   │   │       ├── login_staff.html
│   │   │       ├── base_auth.html
│   │   │       └── senha/
│   │   │           ├── recuperar.html
│   │   │           ├── recuperar_enviado.html
│   │   │           ├── redefinir.html
│   │   │           ├── redefinir_concluido.html
│   │   │           ├── trocar_obrigatorio.html
│   │   │           └── email_assunto.txt
│   │   └── tests/
│   │
│   ├── interessados/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── authentication.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   ├── views_exclusao.py
│   │   ├── migrations/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       ├── criptografar_cpfs.py
│   │   │       └── limpar_tokens.py
│   │   ├── services/
│   │   ├── static/
│   │   │   └── interessados/
│   │   │       ├── formStyles.css
│   │   │       └── imagens/
│   │   ├── templates/
│   │   │   └── interessados/
│   │   │       ├── cadastro.html
│   │   │       ├── login.html
│   │   │       ├── meus_dados.html
│   │   │       ├── dashboard.html
│   │   │       ├── exclusao/
│   │   │       │   ├── solicitar.html
│   │   │       │   └── solicitada.html
│   │   │       └── senha/
│   │   │           ├── recuperar.html
│   │   │           ├── recuperar_enviado.html
│   │   │           ├── redefinir.html
│   │   │           ├── redefinir_concluido.html
│   │   │           ├── trocar_obrigatorio.html
│   │   │           └── sem_email.html
│   │   └── tests/
│   │
│   ├── eventos/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── context_processors.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   ├── management/
│   │   │   └── commands/
│   │   ├── services/
│   │   └── tests/
│   │
│   ├── selecao/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── reports.py
│   │   ├── services.py
│   │   ├── validators.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   ├── services/
│   │   ├── templates/
│   │   │   └── selecao/
│   │   │       ├── relatorio_aprovados_staff.html
│   │   │       └── relatorio_aprovados_mural.html
│   │   └── tests/
│   │
│   ├── academico/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── certificado.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── migrations/
│   │   ├── services/
│   │   ├── templates/
│   │   │   └── academico/
│   │   │       └── gestao_matricula.html
│   │   └── tests/
│   │
│   ├── portal/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── portal/
│   │   │       ├── base.html
│   │   │       ├── index.html
│   │   │       ├── consulta_publica.html
│   │   │       ├── contato.html
│   │   │       ├── detalhes_evento.html
│   │   │       ├── resultado_evento.html
│   │   │       └── politica_privacidade.html
│   │   └── tests/
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── utils_pdf.py
│   │   ├── views.py
│   │   ├── migrations/
│   │   ├── services/
│   │   ├── templates/
│   │   │   └── dashboard/
│   │   │       ├── academico.html
│   │   │       ├── eventos.html
│   │   │       ├── interessados.html
│   │   │       ├── lgpd.html
│   │   │       └── processo_seletivo.html
│   │   └── tests/
│   │
│   └── scripts_admin/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── management/
│       │   └── commands/
│       └── tests/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── cpf-formatter.js
│   │   └── script.js
│   └── images/
│       ├── brasao-2.png
│       ├── brasao-horizontal.png
│       ├── favicon-metareciclagem.png
│       └── logo-pms-header.png
│
├── templates/
│   ├── admin/
│   │   ├── base_site.html
│   │   ├── dashboard.html
│   │   ├── accounts/
│   │   │   └── cards-admin.html
│   │   ├── academico/
│   │   │   └── avaliacao/
│   │   │       └── change_list.html
│   │   ├── dashboard/
│   │   │   └── base_dashboard.html
│   │   └── selecao/
│   │       └── matricular_alunos.html
│   └── base.html
│
├── logs/
│   └── .gitkeep
│
├── nginx/
│   ├── conf.d/
│   └── nginx.conf
│
├── documentacao/
│   ├── 00-INDICE-MASTER-Documentacao-MetaReciclagem.docx
│   ├── 01-Fundacoes-Estatica.docx
│   ├── 02-Estado-Atual-Dinamica.docx
│   ├── 03-Prompts-Contextos-IA.docx
│   ├── 04-Desenvolvimento-Manutencao.docx
│   ├── 05-Manuais-Usuarios.docx
│   ├── 06-Repositorio-Git.docx
│   ├── 07-Visao-Executiva-Diagramas.docx
│   ├── AUDIT_REPORT.md
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── DOCKER_SECURITY.md
│   ├── README-ScriptsAdminCommands.md
│   ├── README-Testes.md
│   ├── README-Visao Geral.md
│   ├── ROADMAP.md
│   ├── SECURITY.md
│   ├── Diagrama ER - bdmetareciclagem - 27-04-2026.png
│   ├── doc_sistema.json
│   └── doc_sistema.yaml
│
├── temp/
│   └── .gitkeep
│
├── QUICKSTART.md
└── README.md
```

### Justificativas das Mudanças

1. **Pasta `temp/`**: Centraliza artefatos temporários (dumps, análises, scripts de investigação)
2. **Pasta `templates/` na raiz**: Templates compartilhadas (admin, base) ficam centralizadas
3. **Pasta `static/` na raiz**: Assets globais (CSS, JS, imagens) em um único lugar
4. **Organização de `apps/`**: Cada app segue padrão consistente (models, views, services, templates, tests)
5. **Documentação centralizada**: Todos os docs em `documentacao/`, não espalhados na raiz
6. **Logs isolados**: Pasta `logs/` para registros de execução

---

## 4. PROPOSTA DE PADRONIZAÇÃO DE NOMES

### 4.1 Convenções de Nomenclatura

**Models:**
- PascalCase: `Interessado`, `EventoVaga`, `Classificacao`, `Matricula`
- Docstrings obrigatórias
- Validações no método `clean()`

**Variáveis e Funções:**
- snake_case: `processar_lote()`, `calcular_score()`, `validar_cpf()`

**Constantes:**
- SCREAMING_SNAKE_CASE: `LIMITE_TENTATIVAS = 5`, `TEMPO_BLOQUEIO = 1800`

**Arquivos Python:**
- snake_case: `services.py`, `validators.py`, `utils.py`, `forms.py`

**Templates HTML:**
- snake_case com contexto: `login_staff.html`, `cadastro_interessado.html`, `relatorio_aprovados_staff.html`
- Estrutura: `{app}/templates/{app}/{feature}/{template}.html`

**Rotas (URLs):**
- Sempre parametrizar com `name=`: `path('login/', views.login, name='login')`
- Namespace por app: `app_name = 'accounts'`
- Padrão: `{app}:{view_name}` (ex: `accounts:login_staff`)

**Diretórios:**
- snake_case: `apps/`, `config/`, `static/`, `templates/`, `documentacao/`, `logs/`, `nginx/`

**Arquivos de Configuração:**
- Prefixo com ponto: `.env`, `.env.example`, `.env.prod`, `.dockerignore`, `.coveragerc`

---

### 4.2 Padrão de Nomes de Rotas

**Convenção Proposta:**

| Contexto             | Padrão                           | Exemplo                               |
|----------------------|----------------------------------|---------------------------------------|
| Login                | `{app}:login`                    | `accounts:login`, `interessados:login`|
| Logout               | `{app}:logout`                   | `accounts:logout`                     |
| Recuperação de Senha | `{app}:senha_recuperar`          | `accounts:senha_recuperar`            |
| Redefinição de Senha | `{app}:senha_redefinir`          | `accounts:senha_redefinir`            |
| Troca Obrigatória    | `{app}:senha_trocar_obrigatorio` | `accounts:senha_trocar_obrigatorio`   |
| Listagem             | `{app}:listar_{entidade}`        | `academico:listar_matriculas`         |
| Detalhes             | `{app}:detalhe_{entidade}`       | `academico:detalhe_matricula`         |
| Criação              | `{app}:criar_{entidade}`         | `selecao:criar_inscricao`             |
| Edição               | `{app}:editar_{entidade}`        | `selecao:editar_classificacao`        |
| Exclusão             | `{app}:excluir_{entidade}`       | `interessados:excluir_perfil`         |
| Relatório            | `{app}:relatorio_{tipo}`         | `selecao:relatorio_aprovados_staff`   |
| Dashboard            | `{app}:dashboard`                | `dashboard:dashboard`                 |

---

## 5. LISTA DE ARQUIVOS QUE PODEM SER ELIMINADOS

### Arquivos Recomendados para Exclusão

| Arquivo | Motivo | Risco |
|---------|--------|-------|
| `15-07-2026-estrutura-html.txt` | Artefato temporário de análise | Baixo |
| `16-07-2026-estrutura-html.txt` | Artefato temporário de análise | Baixo |
| `16-07-2026-estrutura-html2.txt` | Artefato temporário de análise | Baixo |
| `backup.sql` | Dump de banco de dados solto (deve estar em pasta de backups) | Baixo |
| `analise_arquitetura.md` | Relatório antigo (substituído por este) | Baixo |
| `analisar_arquitetura.py` | Script de análise temporário | Baixo |
| `investigar_templates.ps1` | Script PowerShell de investigação (Windows) | Baixo |
| `limpar_tokens.bat` | Script batch obsoleto (usar management command) | Baixo |
| `desktop.ini` | Arquivo de sistema Windows (não deve estar no Git) | Baixo |

**Ação Recomendada:** Mover para `temp/` antes de deletar, manter por 30 dias como backup.

---

## 6. LISTA DE ARQUIVOS QUE PRECISAM SER MOVIDOS

### Reorganização de Arquivos

| Arquivo Atual | Destino Proposto | Justificativa |
|---------------|------------------|---------------|
| `15-07-2026-estrutura-html.txt` | `temp/analise-2026-07-15.txt` | Artefato temporário |
| `16-07-2026-estrutura-html.txt` | `temp/analise-2026-07-16-v1.txt` | Artefato temporário |
| `16-07-2026-estrutura-html2.txt` | `temp/analise-2026-07-16-v2.txt` | Artefato temporário |
| `backup.sql` | `temp/backups/backup-2026-07-16.sql` | Backup de banco |
| `analise_arquitetura.md` | `temp/analise-arquitetura-anterior.md` | Relatório antigo |
| `analisar_arquitetura.py` | `temp/scripts/analisar_arquitetura.py` | Script de análise |
| `investigar_templates.ps1` | `temp/scripts/investigar_templates.ps1` | Script Windows |
| `limpar_tokens.bat` | `temp/scripts/limpar_tokens.bat` | Script obsoleto |
| `Instrucoes-IA-containerizacao.txt` | `documentacao/Instrucoes-IA-containerizacao.txt` | Documentação |
| `Instrucoes-IA.txt` | `documentacao/Instrucoes-IA.txt` | Documentação |

---

## 7. ROTAS QUEBRADAS

### 7.1 Rotas Inexistentes (Crítico)

**Problema:** Templates chamam rotas que não existem em `urls.py`, causando erro `NoReverseMatch`.

**Rotas Faltantes por App:**

#### **accounts**
```
Rota Faltante: staff_senha_recuperar
Chamada em:
  - apps/accounts/templates/accounts/login_staff.html
  - apps/accounts/templates/accounts/senha/adm_recuperar_enviado.html
  - apps/accounts/templates/accounts/senha/adm_redefinir.html

Rota Faltante: staff_senha_redefinir
Chamada em:
  - apps/accounts/templates/accounts/senha/adm_email_recuperar.html (3 ocorrências)

Rota Faltante: accounts:senha_recuperar
Chamada em:
  - apps/accounts/templates/accounts/senha/confirmar.html

Rota Faltante: admin:dashboard
Chamada em:
  - apps/accounts/templates/admin/base_site.html
```

#### **academico**
```
Rota Faltante: academico:gestao_matricula
Chamada em:
  - apps/academico/templates/academico/gestao_matricula.html

Rota Faltante: academico:processar_matricula
Chamada em:
  - apps/academico/templates/academico/gestao_matricula.html

Rota Faltante: academico:alterar_status_inscricao
Chamada em:
  - apps/academico/templates/academico/gestao_matricula.html
```

#### **admin (Django Admin)**
```
Rota Faltante: admin:eventos_evento_changelist
Chamada em:
  - apps/accounts/templates/admin/dashboard.html

Rota Faltante: admin:interessados_interessado_changelist
Chamada em:
  - apps/accounts/templates/admin/dashboard.html

Rota Faltante: admin:selecao_inscricao_changelist
Chamada em:
  - apps/accounts/templates/admin/dashboard.html

Rota Faltante: admin:selecao_classificacao_changelist
Chamada em:
  - apps/selecao/templates/admin/selecao/matricular_alunos.html (2 ocorrências)
```

### 7.2 Causas Raiz

1. **Falta de parametrização `name=` em `path()`**: Rotas definidas sem identificador único
2. **Namespace não registrado**: Apps sem `app_name` em `urls.py`
3. **Views não criadas**: Rotas referenciadas mas views não implementadas
4. **Refatoração incompleta**: Rotas removidas mas templates não atualizados

---

## 8. TEMPLATES ÓRFÃOS

### 8.1 Templates Não Referenciados (19 arquivos)

**Definição:** Arquivos HTML que não são chamados por nenhuma view, não são herdados (`{% extends %}`) e não são incluídos (`{% include %}`) por nenhum outro template.

**Lista Completa:**

```
1. apps/selecao/templates/selecao/relatorio_aprovados_mural.html
2. apps/selecao/templates/selecao/relatorio_aprovados_staff.html
3. apps/interessados/templates/interessados/senha/email_recuperar.html
4. apps/academico/templates/academico/gestao_matricula.html
5. apps/accounts/templates/accounts/exclusao/listar.html
6. apps/accounts/templates/accounts/exclusao/detalhe.html
7. apps/accounts/templates/accounts/senha/adm_redefinir.html
8. apps/accounts/templates/accounts/senha/adm_redefinir_concluido.html
9. apps/accounts/templates/accounts/senha/adm_recuperar.html
10. apps/accounts/templates/accounts/senha/adm_recuperar_enviado.html
11. apps/accounts/templates/accounts/senha/adm_email_recuperar.html
12. apps/accounts/templates/accounts/senha/confirmar.html
13. apps/interessados/templates/interessados/exclusao/solicitar.html
14. apps/interessados/templates/interessados/exclusao/solicitada.html
15. apps/selecao/templates/admin/selecao/matricular_alunos.html
16. apps/accounts/templates/admin/accounts/cards-admin.html
17. apps/academico/templates/admin/academico/avaliacao/change_list.html
18. apps/dashboard/templates/admin/dashboard/base_dashboard.html
19. apps/accounts/templates/admin/dashboard.html
```

### 8.2 Análise de Causa

**Padrão Detectado:**
- Muitos templates de **senha** (recuperar, redefinir, trocar) estão órfãos, sugerindo que as views foram refatoradas mas os templates não foram deletados
- Templates de **exclusão** (accounts e interessados) estão órfãos, indicando feature descontinuada ou em desenvolvimento
- Templates de **admin customizado** estão órfãos, sugerindo que o Django Admin padrão é usado em vez de customizações

### 8.3 Recomendação

**Ação:** Mover para `temp/templates-orfaos/` antes de deletar. Validar com o desenvolvedor se algum é ainda necessário.

---

## 9. ORDEM CORRETA PARA REFATORAÇÃO SEM QUEBRAR O SISTEMA

### Sequência de Refatoração (9 Etapas)

---

### **ETAPA 1: Preparação e Backup (Baixo Risco)**
**Objetivo:** Garantir segurança antes de qualquer mudança.

**Ações:**
1. Criar branch Git: `git checkout -b refactor/arquitetura-2026-07`
2. Executar backup completo do banco: `python manage.py dumpdata  temp/backups/backup-pre-refactor.json`
3. Executar testes atuais: `pytest --cov=apps --cov-report=html`
4. Documentar cobertura de testes atual (baseline)

**Tempo Estimado:** 30 min
**Risco:** Nenhum (apenas leitura e backup)

---

### **ETAPA 2: Limpeza de Arquivos Soltos (Baixo Risco)**
**Objetivo:** Organizar raiz do projeto.

**Ações:**
1. Criar pasta `temp/` na raiz
2. Mover arquivos temporários:
   ```bash
   mv 15-07-2026-estrutura-html.txt temp/
   mv 16-07-2026-estrutura-html.txt temp/
   mv 16-07-2026-estrutura-html2.txt temp/
   mv backup.sql temp/backups/
   mv analise_arquitetura.md temp/
   mv analisar_arquitetura.py temp/scripts/
   mv investigar_templates.ps1 temp/scripts/
   mv limpar_tokens.bat temp/scripts/
   ```
3. Deletar `desktop.ini`
4. Commit: `git add . && git commit -m "[REFACTOR] Organizar arquivos soltos na raiz"`

**Tempo Estimado:** 15 min
**Risco:** Nenhum (apenas reorganização)

---

### **ETAPA 3: Documentação de Rotas Faltantes (Médio Risco)**
**Objetivo:** Mapear todas as rotas que precisam ser criadas.

**Ações:**
1. Criar arquivo `documentacao/ROTAS-FALTANTES.md` listando todas as 11 rotas inexistentes
2. Para cada rota, documentar:
   - Nome da rota
   - Caminho URL esperado
   - View que deve implementar
   - Template que a chama
3. Revisar com desenvolvedor: qual rota é realmente necessária vs. qual é obsoleta?
4. Commit: `git add . && git commit -m "[DOCS] Documentar rotas faltantes"`

**Tempo Estimado:** 1 hora
**Risco:** Baixo (apenas documentação)

---

### **ETAPA 4: Implementação de Rotas Críticas (Médio-Alto Risco)**
**Objetivo:** Criar rotas que causam erros imediatos.

**Ações:**
1. **Rotas de Senha (accounts):**
   - Criar `staff_senha_recuperar` em `apps/accounts/urls.py`
   - Criar `staff_senha_redefinir` em `apps/accounts/urls.py`
   - Criar `accounts:senha_recuperar` em `apps/accounts/urls.py`
   - Implementar views correspondentes ou redirecionar para views existentes

2. **Rotas de Matrícula (academico):**
   - Criar `academico:gestao_matricula` em `apps/academico/urls.py`
   - Criar `academico:processar_matricula` em `apps/academico/urls.py`
   - Criar `academico:alterar_status_inscricao` em `apps/academico/urls.py`

3. **Rotas de Admin:**
   - Adicionar `admin:dashboard` em `config/urls.py` (redirecionar para admin index)
   - Adicionar `admin:eventos_evento_changelist` (usar reverse automático do Django Admin)
   - Adicionar `admin:interessados_interessado_changelist` (usar reverse automático)
   - Adicionar `admin:selecao_inscricao_changelist` (usar reverse automático)
   - Adicionar `admin:selecao_classificacao_changelist` (usar reverse automático)

4. Executar testes: `pytest --cov=apps`
5. Commit: `git add . && git commit -m "[FEATURE] Implementar rotas faltantes"`

**Tempo Estimado:** 3-4 horas
**Risco:** Médio (requer implementação de views)

---

### **ETAPA 5: Reorganização de Diretórios (Alto Risco)**
**Objetivo:** Mover arquivos para nova estrutura.

**Ações:**
1. Criar nova estrutura de diretórios conforme proposto na Seção 3
2. Mover arquivos por app:
   ```bash
   # Exemplo para accounts
   mkdir -p apps/accounts/services
   mkdir -p apps/accounts/templates/accounts/senha
   # ... repetir para cada app
   ```
3. Atualizar imports em `settings.py` se necessário (TEMPLATES, STATICFILES_DIRS)
4. Executar testes: `pytest --cov=apps`
5. Verificar se templates são encontradas: `python manage.py findstatic --list`
6. Commit: `git add . && git commit -m "[REFACTOR] Reorganizar estrutura de diretórios"`

**Tempo Estimado:** 2-3 horas
**Risco:** Alto (pode quebrar imports e template loading)

---

### **ETAPA 6: Consolidação de Templates Duplicadas (Médio Risco)**
**Objetivo:** Eliminar duplicação de `dashboard.html`.

**Ações:**
1. Analisar ambas as versões:
   - `apps/accounts/templates/admin/dashboard.html`
   - `apps/interessados/templates/interessados/dashboard.html`
2. Determinar qual é a versão correta (ou mesclar)
3. Deletar a versão duplicada
4. Atualizar views para apontar para a versão única
5. Executar testes: `pytest --cov=apps`
6. Commit: `git add . && git commit -m "[REFACTOR] Consolidar templates duplicadas"`

**Tempo Estimado:** 1 hora
**Risco:** Médio (pode quebrar views que apontam para template errada)

---

### **ETAPA 7: Limpeza de Templates Órfãs (Baixo Risco)**
**Objetivo:** Remover templates não utilizadas.

**Ações:**
1. Mover templates órfãs para `temp/templates-orfaos/`:
   ```bash
   mkdir -p temp/templates-orfaos
   mv apps/selecao/templates/selecao/relatorio_aprovados_mural.html temp/templates-orfaos/
   # ... repetir para cada template órfã
   ```
2. Executar testes: `pytest --cov=apps`
3. Se tudo passar, deletar pasta `temp/templates-orfaos/` após 30 dias
4. Commit: `git add . && git commit -m "[REFACTOR] Remover templates órfãs"`

**Tempo Estimado:** 1 hora
**Risco:** Baixo (templates não são usadas)

---

### **ETAPA 8: Padronização de Nomes (Médio Risco)**
**Objetivo:** Aplicar convenções de nomenclatura.

**Ações:**
1. Renomear arquivos Python para snake_case (se necessário)
2. Renomear templates para padrão consistente
3. Atualizar imports em views
4. Atualizar referências em templates
5. Executar testes: `pytest --cov=apps`
6. Commit: `git add . && git commit -m "[REFACTOR] Padronizar nomes de arquivos"`

**Tempo Estimado:** 2 horas
**Risco:** Médio (requer atualização de múltiplos imports)

---

### **ETAPA 9: Validação Final e Merge (Baixo Risco)**
**Objetivo:** Garantir que tudo funciona antes de integrar na main.

**Ações:**
1. Executar suite completa de testes: `pytest --cov=apps --cov-report=html`
2. Validar cobertura de testes (mínimo 80%)
3. Executar `python manage.py check` para validar configuração
4. Executar `python manage.py migrate` para validar migrações
5. Executar servidor local: `python manage.py runserver`
6. Testar manualmente as rotas críticas
7. Criar Pull Request com descrição detalhada
8. Code Review por segundo desenvolvedor
9. Merge para `main` após aprovação
10. Deploy em staging para validação final

**Tempo Estimado:** 2-3 horas
**Risco:** Baixo (apenas validação)

---

### **Resumo de Risco por Etapa**

| Etapa | Descrição | Risco | Tempo |
|-------|-----------|-------|-------|
| 1 | Preparação e Backup | Nenhum | 30 min |
| 2 | Limpeza de Arquivos | Nenhum | 15 min |
| 3 | Documentação de Rotas | Baixo | 1 h |
| 4 | Implementação de Rotas | Médio-Alto | 3-4 h |
| 5 | Reorganização de Diretórios | Alto | 2-3 h |
| 6 | Consolidação de Templates | Médio | 1 h |
| 7 | Limpeza de Templates Órfãs | Baixo | 1 h |
| 8 | Padronização de Nomes | Médio | 2 h |
| 9 | Validação Final | Baixo | 2-3 h |
| **TOTAL** | | | **13-16 h** |

---

## LIMITAÇÕES DA ANÁLISE

1. **Arquivo PDF incompleto**: O PDF fornecido contém principalmente conceitos de herança de templates Django e estrutura geral. Não foi possível extrair detalhes completos de todas as 8 aplicações.

2. **Falta de acesso ao código-fonte completo**: Análise baseada na estrutura de diretórios e referências em templates. Não foi possível validar:
   - Conteúdo completo de `settings.py`
   - Implementação de todas as views
   - Lógica de services
   - Testes existentes

3. **Ambiguidade em rotas de admin**: Django Admin gera rotas automaticamente. Algumas rotas podem estar funcionando via reverse automático sem estar explicitamente definidas em `urls.py`.

4. **Templates órfãs**: Análise baseada em varredura de arquivos. Alguns templates podem ser carregados dinamicamente via JavaScript ou AJAX, não detectados nesta análise.

5. **Documentação incompleta**: Falta mapeamento de todas as tabelas do banco de dados e campos específicos de algumas aplicações.

---

## PRÓXIMOS PASSOS RECOMENDADOS

1. **Validar com desenvolvedor**: Confirmar quais rotas são realmente necessárias vs. obsoletas
2. **Executar testes**: Rodar `pytest --cov` para validar cobertura atual
3. **Iniciar Etapa 1**: Criar branch de refatoração e backup
4. **Priorizar Etapa 4**: Implementar rotas críticas primeiro (maior impacto)
5. **Documentar decisões**: Criar ADR-011 para decisões de refatoração

---

