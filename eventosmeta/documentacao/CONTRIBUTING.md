# CONTRIBUTING.md

# Guia de Contribuição

**Versão 3.0** - *13/05/2026*

## Padrões de Código

- Models: PascalCase
- Variáveis: snake_case
- Constantes: SCREAMING_SNAKE_CASE

## Fluxo de Trabalho

1. Faça fork do repositório.
2. Crie branch `feature/nome-descritivo`.
3. Commit com formato `[TIPO] Descrição` (TIPO: FEATURE, FIX, DOCS, REFACTOR, TEST).
4. Push para sua fork.
5. Abra Pull Request (PR).
6. Aguarde Code Review.
7. Merge após aprovação.

## Checklist de Code Review

- Testes pytest passando.
- Cobertura de testes >80%.
- Sem hardcoding de valores.
- Docstrings em funções e classes.
- Nomenclatura consistente.
- Sem N+1 queries (use select_related/prefetch_related).
- Sem secrets no código.
- Verificações de segurança (CSRF/XSS/SQL Injection).

## Boas Práticas de Segurança

- Rate-limit com django-axes.
- CSP com django-csp.
- Criptografia de CPF/NIS com Fernet.
- Otimização de queries com select_related/prefetch_related.

---
