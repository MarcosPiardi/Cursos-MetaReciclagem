# RESUMO TÉCNICO - Sistema de Classificação de Inscrições

**Data:** 06/03/2026  
**Projeto:** Sistema MetaReciclagem - Gestão de Eventos e Inscrições  
**Tecnologia:** Django + Python  
**Gerado automaticamente em:** 06/03/2026 18:39

---

## OBJETIVO DO SISTEMA

Classificar inscrições de eventos usando **critérios de pontuação e ordenação**
com **prioridades configuráveis**, permitindo flexibilidade total na definição
de regras de seleção por evento.

---

## ARQUITETURA IMPLEMENTADA

```
┌─────────────────────────────────────────────────────────┐
│                   FLUXO DE CLASSIFICAÇÃO                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. EVENTO                                              │
│     └─> EventoCriterio (prioridade 1, 2, 3...)          │
│         └─> Criterio (PONTUACAO ou ORDENACAO)           │
│                                                         │
│  2. INSCRIÇÃO                                           │
│     └─> Interessado (dados pessoais)                    │
│                                                         │
│  3. CLASSIFICAÇÃO (via ClassificadorService            )│
│     ├─> Calcula pontuação (critérios PONTUACAO)         │
│     ├─> Aplica ordenação (critérios ORDENACAO)          │
│     └─> Define posição final                            │
│                                                         │
│  4. RESULTADO                                           │
│     └─> Classificacao (posição, pontos, status)         │
│         └─> InscricaoCriterioAtendido (detalhes)        │
└─────────────────────────────────────────────────────────┘
```

---

## ESTRUTURA DE APPS

### **dashboard/**
- admin configurado

---

## ARQUIVOS PRINCIPAIS

### **1. eventos/admin.py** (0 linhas)

**Actions disponíveis:**
- (nenhuma action detectada)

### **2. selecao/services.py** (0 linhas)

**Classe principal:** `ClassificadorService`

```python
ClassificadorService
├─> calcular_pontuacao_inscricao()
├─> verificar_criterios_automaticos()
├─> processar_inscricao()
└─> classificar_evento()
```

### **3. interessados/admin.py** (0 linhas)

**Actions disponíveis:**
- (nenhuma action detectada)

### **4. selecao/management/commands/classificar_evento.py**

**Descrição:** Classifica as inscrições de um evento baseado em critérios fixos

**Uso:**
```bash
python manage.py classificar_evento --evento_id=1
```

---

## CRITÉRIOS IMPLEMENTADOS

### Tipos de Critério

**PONTUACAO** — Soma pontos ao candidato. Usado para classificação por mérito.

**ORDENACAO** — Não soma pontos. Define ordem de desempate.

### Critérios de PONTUACAO

(nenhum critério de pontuação encontrado nas fixtures)

### Critérios de ORDENACAO

(nenhum critério de ordenação encontrado nas fixtures)

---

## CONCEITOS IMPORTANTES

### Prioridade dos Critérios

Os critérios são aplicados na ordem de prioridade definida no evento.
A lógica de ordenação é:

1. Maior pontuação primeiro (`-pontuacao_total`)
2. Critérios de ORDENACAO na ordem de prioridade
3. Data de inscrição como desempate final

**Exemplo:**
```
Prioridade 1: PCD (10 pts)        → soma pontos
Prioridade 2: IDADE_CRESCENTE     → desempate por idade
Prioridade 3: ORDEM_INSCRICAO     → desempate final

Resultado:
1º - João  (10 pts, 19 anos, inscrito 01/01/2025)
2º - Maria (10 pts, 20 anos, inscrito 01/01/2025)
3º - Pedro (10 pts, 20 anos, inscrito 02/01/2025)
4º - Ana   ( 5 pts, 18 anos, inscrito 01/01/2025)
```

### Pontuação Potencial vs Pontuação Real

| Tipo | Onde | O que calcula |
|------|------|---------------|
| **Potencial Máxima** | Exportação de Interessados | TODOS os critérios do sistema |
| **Real do Evento** | Classificação de Evento | APENAS critérios configurados no evento |

O mesmo interessado terá pontuações diferentes em cada evento,
pois cada evento usa um subconjunto de critérios.

---

## ERROS CORRIGIDOS (detectados no código)

### Erro 1: `'Fototipo' object has no attribute 'upper'`

**Causa:** fototipo é ForeignKey, não string

```python
# Errado
interessado.fototipo.upper()

# Correto
interessado.fototipo.nome
```

### Erro 2: `'Interessado' object has no attribute 'tipo_deficiencia'`

**Causa:** Campo tipo_deficiencia não existe no model Interessado

```python
# Errado
interessado.tipo_deficiencia

# Correto
Usar pcd_fisica, pcd_visual, etc. ou tem_deficiencia
```

### Erro 3: `Classificação com 0 pontos mesmo com critérios configurados`

**Causa:** Código usava criterio.tipo (não existe), correto é criterio.tipo_criterio

```python
# Errado
criterio.tipo

# Correto
criterio.tipo_criterio
```

---

## EXPORTADORES

### 1. Exportação de Classificação de Evento

**Arquivo:** `eventos/admin.py`  
**Formato:** CSV (UTF-8 com BOM, separador `;`)

**Colunas principais:** Evento, Posição, Nome, CPF, Pontuação Calculada,
Pontuação Salva, Diferença, Classificado, Critérios Atendidos

**Como usar:**
1. Acesse: `http://127.0.0.1:8000/admin/eventos/evento/`
2. Selecione o(s) evento(s)
3. Escolha a action de exportação
4. Clique em **Ir**

**Análise de erros:**
- Coluna `Diferença` = `0.00` → Correto
- Coluna `Diferença` ≠ `0.00` → Erro de cálculo

### 2. Exportação de Interessados com Análise de Critérios

**Arquivo:** `interessados/admin.py`  
**Formato:** CSV (UTF-8 com BOM, separador `;`)

**Colunas principais:** CPF, Nome, Idade, Sexo, Fototipo, Escolaridade,
Tem Deficiência, Tipos PCD, Programa Social, NIS,
uma coluna por critério (SIM/NÃO), Pontuação Total Potencial

**Como usar:**
1. Acesse: `http://127.0.0.1:8000/admin/interessados/interessado/`
2. Selecione os interessados (ou todos)
3. Escolha a action de exportação
4. Clique em **Ir**

---

## CAMPOS PCD DO MODEL INTERESSADO

Campos booleanos encontrados no model:

- `pcd_fisica`
- `pcd_visual`
- `pcd_auditiva`
- `pcd_intelectual`
- `pcd_psicossocial`
- `pcd_multiplas`

Properties calculadas:
- `is_anonymous` (property)
- `is_authenticated` (property)
- `username` (property)
- `tem_deficiencia` (property)

---

## MODELOS DE DADOS PRINCIPAIS

### Criterio (`eventos`)

_Define um critério de classificação_

- `tipo_criterio` — `CharField`
- `codigo` — `CharField`
- `nome` — `CharField`
- `descricao` — `TextField`
- `pontos` — `IntegerField`
- `categoria` — `CharField`
- `ativo` — `BooleanField`
- `criado_em` — `DateTimeField`
- `atualizado_em` — `DateTimeField`

### EventoCriterio (`eventos`)

_Associa critério a um evento com prioridade_

- `evento` — `ForeignKey`
- `criterio` — `ForeignKey`
- `prioridade` — `IntegerField`
- `ativo` — `BooleanField`
- `criado_em` — `DateTimeField`

### Inscricao (`selecao`)

_Inscrição de um interessado em um evento_

- `interessado` — `ForeignKey`
- `evento` — `ForeignKey`
- `status` — `ForeignKey`
- `data_inscricao` — `DateTimeField`
- `data_atualizacao` — `DateTimeField`
- `observacoes` — `TextField`

### Classificacao (`selecao`)

_Resultado da classificação de uma inscrição_

- `inscricao` — `OneToOneField`
- `posicao` — `PositiveIntegerField`
- `pontuacao_total` — `DecimalField`
- `classificado` — `BooleanField`
- `lista_espera` — `BooleanField`
- `processado_em` — `DateTimeField`
- `atualizado_em` — `DateTimeField`

### InscricaoCriterioAtendido (`selecao`)

_Critérios atendidos por uma inscrição_

- `inscricao` — `ForeignKey`
- `criterio` — `ForeignKey`
- `pontos_atribuidos` — `PositiveIntegerField`
- `validado` — `BooleanField`
- `observacao_validacao` — `TextField`

---

## COMANDOS ÚTEIS NO SHELL

### Classificar evento
```python
from apps.selecao.services import ClassificadorService
from apps.eventos.models import Evento

evento = Evento.objects.get(nome='Nome do Evento')
ClassificadorService.classificar_evento(evento)
```

### Ver critérios de um evento
```python
from apps.eventos.models import Evento, EventoCriterio

evento = Evento.objects.get(nome='Nome do Evento')
criterios = EventoCriterio.objects.filter(
    evento=evento, ativo=True
).select_related('criterio').order_by('prioridade')

for ec in criterios:
    print(f"{ec.prioridade}. {ec.criterio.nome} ({ec.criterio.tipo_criterio}) - {ec.criterio.pontos} pts")
```

### Ver classificação de um evento
```python
from apps.selecao.models import Classificacao
from apps.eventos.models import Evento
from datetime import date

evento = Evento.objects.get(nome='Nome do Evento')
classificacoes = Classificacao.objects.filter(
    inscricao__evento=evento
).select_related('inscricao__interessado').order_by('posicao')

hoje = date.today()
for c in classificacoes[:10]:
    dn = c.inscricao.interessado.data_nascimento
    idade = hoje.year - dn.year - ((hoje.month, hoje.day) < (dn.month, dn.day))
    status = 'Classificado' if c.classificado else 'Lista Espera'
    print(f"{c.posicao}. {c.inscricao.interessado.nome} ({idade} anos) - {c.pontuacao_total} pts - {status}")
```

### Ver critérios atendidos por uma inscrição
```python
from apps.selecao.models import InscricaoCriterioAtendido, Inscricao

inscricao = Inscricao.objects.get(id=1)
criterios = InscricaoCriterioAtendido.objects.filter(
    inscricao=inscricao
).select_related('criterio')

for ca in criterios:
    print(f"  - {ca.criterio.nome}: {ca.pontos_atribuidos} pts")
    print(f"    Observação: {ca.observacao_validacao}")
```

---

## PROXIMOS PASSOS

### Melhorias Futuras
- [ ] Exportação de interessados por evento específico
- [ ] Dashboard de análise de classificações
- [ ] Validação automática de pontuações
- [ ] Histórico de classificações (auditoria)
- [ ] Notificações automáticas para classificados
- [ ] Geração de listas de chamada em PDF

### Testes
- [ ] Testes unitários do ClassificadorService
- [ ] Testes de integração da classificação
- [ ] Validação de casos extremos (empates, sem critérios)
- [ ] Testes de performance com muitas inscrições

### Segurança
- [ ] Log de alterações em classificações
- [ ] Permissões granulares por tipo de usuário
- [ ] Backup automático antes de reclassificar

---

**Documento gerado em:** 06/03/2026 18:39  
**Script:** gerar_markdown.py  
**Status:** Funcional