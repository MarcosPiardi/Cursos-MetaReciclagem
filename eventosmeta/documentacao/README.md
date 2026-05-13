# README.md

# MetaReciclagem - Sistema de Gestão de Inscrições Municipais

**Versão 3.0** - *13/05/2026*

## Visão Geral

O MetaReciclagem é um sistema completo de gestão de inscrições municipais para programas de reciclagem. Ele gerencia desde o cadastro de interessados até a emissão de certificados, com foco em conformidade LGPD, segurança e relatórios.

## Stack Tecnológica

- Django 5.2.4
- Python 3.13.2
- PostgreSQL 15+
- django-axes (controle de rate-limit)
- django-csp (Content Security Policy)
- django-encrypted-model-fields (campos criptografados)

## Funcionalidades Principais

- Cadastro de interessados via CPF
- Inscrição em turmas e cursos
- Classificação e seleção automática
- Matrícula e controle de vagas
- Lançamento de notas e frequência
- Emissão de certificados digitais
- Conformidade com LGPD (consentimento e anonimização)
- Relatórios exportáveis em Excel
- Auditoria completa com logs

## Quick Start

1. `git clone <repositório>`
2. `python -m venv venv`
3. Ative o ambiente: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. `pip install -r requirements.txt`
5. Copie `.env.example` para `.env` e configure variáveis (DATABASE_URL, FIELD_ENCRYPTION_KEY, etc.)
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. `python manage.py runserver`

---

