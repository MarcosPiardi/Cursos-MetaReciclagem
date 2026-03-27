# Estratégia de Testes - Documentação de Execução
Data: 27/03/2026
Versão: 1.0

## 1. RESUMO EXECUTIVO
- Total de testes: 62
- Cobertura global: 54%
- Apps cobertas: interessados (41), selecao (21)
- Apps pendentes: academico, eventos, accounts, portal

## 2. FLUXO DE EXECUÇÃO (PASSO A PASSO)

### Passo 1: Verificar se testes passam
```bash
pytest apps/interessados/tests/ apps/selecao/tests/ -v --ds=config.settings

