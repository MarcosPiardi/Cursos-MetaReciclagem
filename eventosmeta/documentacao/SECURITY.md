# SECURITY.md

# Política de Segurança

**Versão 3.0** - *13/05/2026*

## Relatório de Vulnerabilidades

Contato confidencial com a equipe de segurança.

## Autenticação

- InteressadoBackend + AxesStandaloneBackend.
- Rate-limit: 5 tentativas = 30min de bloqueio.
- Primeiro acesso obriga troca de senha.

## Autorização

- Permissões granulares por role (interessado/staff/admin).
- Django Permission framework.

## Criptografia

- FIELD_ENCRYPTION_KEY para CPF/NIS (Fernet).
- bcrypt para senhas.
- TLS/SSL obrigatório em produção.

## Headers de Segurança

- CSP via django-csp.
- CSRF token.
- Proteção XSS.
- HSTS.

## Validação

- Validação de input nos models.
- Encoding de output nos templates.
- ORM Django previne SQL Injection.
- Upload de arquivos: MIME type e limite de tamanho.

## LGPD

- Consentimento obrigatório.
- Anonimização irreversível.
- Logs de auditoria.
- Políticas de retenção de dados.
- Criptografia de dados sensíveis.

## Email

- CustomEmailBackend DataCenter 10.28.10.54:587.
- TLS.
- Rate-limiting.
- Validação de destinatário.

## Backup

- Automático diário às 02:00.
- Retenção de 30 dias.
- Testes periódicos de restore.
- Rollback documentado.

## Monitoramento

- Alertas para 90% de disco, CPU/Memória.
- Agregação de logs.
- Eventos de segurança.

## Atualizações

- Patch management para vulnerabilidades críticas.
- Deploy em staging antes de produção.
- Plano de rollback documentado.
