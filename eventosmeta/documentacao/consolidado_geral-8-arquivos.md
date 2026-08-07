# Consolidação Geral de Documentos

**Diretório de Origem:** `C:\DES\doctemp`
**Total de Arquivos Consolidados:** 8

---

## Arquivo: 00-INDICE-MASTER-Documentacao-MetaReciclagem.docx

MetaReciclagem

ÍNDICE MASTER DE DOCUMENTAÇÃO

Guia de Navegação Unificado - Versão Compacta V.3.0

13 de maio de 2026

1. Introdução

Este documento constitui o mapa de navegação central para os 7 volumes que integram a documentação técnica, funcional e estratégica do ecossistema MetaReciclagem, atualizado para a versão V.3.0. O objetivo deste índice é facilitar a localização ágil de informações específicas, garantindo que desenvolvedores, gestores e usuários finais acessem o conteúdo pertinente às suas necessidades de forma estruturada e eficiente.

2. Mapa de Volumes

Volume

Foco Principal

Público-Alvo

Seções Principais

Volume 1: 01-Fundacoes-Estatica-V.3.0.docx

Fundações Técnicas

Arquitetos, Devs

ADRs, Regras de Negócio, Glossário, Dicionário de Dados

Volume 2: 02-Estado-Atual-Dinamica-V.3.0.docx

Arquitetura e Status

Devs, Staff

Arquitetura Geral, Endpoints APIs, Status de Funcionalidades

Volume 3: 03-Prompts-Contextos-IA-V.3.0.docx

Contexto para IA

IA, Devs

Perfil Dev, Contexto Sistema, Instruções IA, Padrões

Volume 4: 04-Desenvolvimento-Manutencao-V.3.0.docx

Desenvolvimento

Devs, DevOps

Setup, Review, Troubleshooting, Fluxo de Dados, Testes, Deploy

Volume 5: 05-Manuais-Usuarios-V.3.0.docx

Manuais por Perfil

Usuários Finais

Manual Interessados, Staff, Admin, Navegação UI, FAQ

Volume 6: 06-Repositorio-Git-V.3.0.docx

Repositório Git

Devs, DevOps

README, CHANGELOG, CONTRIBUTING, ROADMAP, SECURITY

Volume 7: 07-Visao-Executiva-Diagramas-V.3.0.docx

Visão Executiva

Gestores, Arquitetos

O que é, Por quê, Diagrama de Fluxo, Diagrama de Recuperação

3. Índice por Tópico

4. Guia de Leitura por Perfil

Novo Desenvolvedor: Vol 7 (O que é) → Vol 1 (Regras) → Vol 2 (Arquitetura) → Vol 4 (Setup)

Gestor: Vol 7 (O que é + Por quê + Diagramas) → Vol 6 (Roadmap)

Staff: Vol 5 (Manual Staff) → Vol 7 (Diagrama Fluxo) → Vol 2 (Endpoints)

Administrador: Vol 5 (Manual Admin) → Vol 7 (Diagramas) → Vol 4 (Deploy) → Vol 6 (Security)

Candidato: Vol 5 (Manual Interessado) → Vol 7 (Diagrama Fluxo)

Arquiteto: Vol 7 (O que é + Por quê) → Vol 1 (ADRs) → Vol 2 (Arquitetura)

5. Dependências entre Volumes

A estrutura documental segue uma hierarquia lógica de dependência: o Volume 01 estabelece a base técnica para todos os demais. O Volume 07 fornece a visão de negócio necessária para compreender o Volume 02 (Arquitetura). Os padrões definidos no Volume 03 regem a implementação detalhada no Volume 04, que por sua vez sustenta as funcionalidades descritas nos Volumes 05 e 06.

6. Busca Rápida por Problema

Tenho dúvida sobre...

Procure em...

O que é o MetaReciclagem

 Vol 7, Seção 1

Por que o sistema foi criado (Justificativa)

 Vol 7, Seção 1.1

Entender o fluxo de trabalho completo

 Vol 7, Seção 2 (Diagrama de Fluxo)

Lógica de recuperação de senha

 Vol 7, Seção 3 (Diagrama de Recuperação)

Como funciona a classificação

 Vol 7 (Diagrama) + Vol 1 (Regras)

Problemas na geração de certificados

 Vol 4 (Fluxo) + Vol 7 (Diagrama)

Configuração do ambiente local (Setup)

 Vol 4, Seção Setup-Dev

Procedimentos de deploy em produção

 Vol 4, Seção Migrações-Deploy

Conformidade com Segurança e LGPD

 Vol 6 (SECURITY) + Vol 7

Execução de testes automatizados

 Vol 4, Seção Testes-Fixtures

Solução de erros comuns (Troubleshoot)

 Vol 4, Seção Troubleshooting-Dev

Estrutura de UX e Navegação

 Vol 5, Seção Navegação-UI

7. Versão e Manutenção

Data: 13/05/2026Versão: V.3.0Atualizado: 13/05/2026 (Inclusão do Volume 07 - Visão Executiva e Diagramas)Responsável: Marcos PiardiPróxima revisão: Agendada para o lançamento de novos volumes ou alterações críticas de arquitetura.

Documento elaborado em 13 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 01-Fundacoes-Estatica.docx

MetaReciclagem

01-FUNDAÇÕES-ESTÁTICA-V.3.0

Documentação de Fundações, Regras de Negócio e Dicionário de Dados

12 de maio de 2026

01-FUNDAÇÕES-ESTÁTICA-V3.0

Este documento consolida as bases estruturais do sistema MetaReciclagem, abrangendo as decisões arquiteturais críticas, as regras de negócio que regem os processos de seleção, o glossário de termos técnicos e o dicionário de dados das principais entidades. Esta versão 3.0 reflete a maturidade do projeto e serve como alicerce para a manutenibilidade e evolução do código.

1. Registros de Decisões Arquiteturais (ADRs)

A tabela abaixo detalha as decisões técnicas fundamentais tomadas durante o desenvolvimento, fornecendo o contexto necessário para futuras manutenções e auditorias.

ID

Decisão

Contexto

ADR-001

CPF identificador único

Validação segura e integração com sistemas municipais.

ADR-002

Field encryption Fernet

Conformidade com a LGPD para proteção de dados sensíveis (CPF/NIS).

ADR-003

Service Layer

Isolamento de lógica de negócio complexa fora das Views e Models.

ADR-004

PostgreSQL JSONB

Flexibilidade para armazenamento de dados dinâmicos e metadados.

ADR-005

Rate limiting Axes

Proteção contra ataques de força bruta (bloqueio de 30min após 5 tentativas).

ADR-006

CSP headers

Implementação de Content Security Policy para mitigação de ataques XSS.

ADR-007

Django Admin ERP

Utilização do Admin nativo customizado como interface principal de gestão.

ADR-008

pytest

Framework de testes focado em fixtures e legibilidade do código.

ADR-009

LGPD anonymization

Garantia do direito ao esquecimento através da anonimização de registros.

ADR-010

Email DataCenter

Integração direta com o DataCenter municipal para comunicações oficiais.

2. Regras de Negócio

As regras de negócio definem o comportamento esperado do sistema em relação aos processos de elegibilidade, classificação e certificação dos interessados.

Regra

Descrição

Elegibilidade

CPF único por evento; o NIS é obrigatório para candidatos em regime de cotas.

Classificação

Ordenação por Score DESC; desempate por data_inscricao com precisão de milissegundos ASC.

Matrícula

Sujeita à revisão do staff; respeita o limite de vagas e gera notificação automática.

Aprovação

Exige nota final igual ou superior a 7.0 e frequência mínima de 75%.

Certificação

Disponível apenas para aprovados; inclui código de autenticidade verificável.

LGPD

O direito ao esquecimento é atendido via processo de anonimização irreversível.

3. Lógica da Regra de Negócio

• Retornar 0 pontos para inscrição sem critérios.• Apenas inscrições com status: Pendente, Classificado, Lista de Espera participam • Classificação order_fields = pontuacao_total, inscricao__data_inscricao Desc (do maior para o menor)• Após classificação, status da inscrição é atualizado para: Classificado (se posição <= total_vagas) • Lista de Espera (se posição > total_vagas) • Status do evento é alterado para "Resultado Divulgado" (ID=5)

  Percorre todos os critérios do evento 

  Para CADA critério, valida se o interessado atende (pcd_fisica, programa_social, fototipo, etc) 

  Se atende, soma os pontos 

  Depois classifica por pontos DESC + desempate

4. Glossário de Termos

Definições padronizadas para garantir o alinhamento entre desenvolvedores, analistas e usuários do sistema.

Termo

Definição

Interessado

Entidade que representa o usuário externo/candidato. 

Cidadão registrado no sistema para participação em processos seletivos.

CPF

Identificador primário e único do cidadão, armazenado de forma criptografada.

NIS

Número de Inscrição Social, utilizado como critério de prioridade em programas sociais.

Fototipo

Classificação dermatológica que categoriza a pele humana. Neste sistema usamos a definição AutoDeclarada de Cor/Raça do IBGE (Preto, Pardo, Branco, Amarelo, Indígena).

Evento

Entidade que define o curso ou atividade oferecida.

Vaga

Refere-se ao número total de postos disponíveis em um determinado curso ou evento.

Turma

Instância específica de um evento com horários e local definidos.

Lista de Espera

Candidatos que não se enquadram no número de vagas imediatas (total_vagas) são automaticamente movidos para a lista de espera, mantendo sua posição relativa conforme o ranking calculado. A promoção de candidatos da lista de espera para vagas efetivas ocorre mediante desistência ou desclassificação de candidatos superiores.

Inscrição

Vínculo formal estabelecido entre um Interessado e um Evento específico.

Classificação

Processo lógico de ordenação de candidatos gerando um ranking automaticamente com base nos critérios de pontuação e desempate.

Critério de Pontuação

Parâmetro pontuável estabelecido para avaliar, comparar e rankear os candidatos (ex: Programa Social, Fototipo, etc.).

Desempate

Regra aplicada quando dois candidatos possuem a mesma pontuação (prioridade para inscrição mais antiga).

Matrícula

Etapa de confirmação da ocupação da vaga pelo candidato classificado.

Avaliação

Registro do desempenho acadêmico e de frequência durante a execução do curso.

Certificação

Documento digital emitido para os candidatos que atingiram os critérios de aprovação.

Taxa de Aprovação

Percentual de aprovados por evento

LGPD

Conjunto de práticas de privacidade, focadas na anonimização de dados sensíveis.

ClassificadorService

Classe Python que encapsula o algoritmo de ranking.

Service Layer

Camada de abstração para lógicas que não pertencem exclusivamente ao Model ou à View.

Admin Customizado

Extensão do Django Admin para fluxos de trabalho específicos do Staff municipal.

Rate Limiting

Restrição de tentativas de login (5 falhas bloqueiam o IP por 30 minutos).

CSP

Cabeçalhos HTTP que impedem a execução de scripts não autorizados.

Middleware

Componentes que processam a requisição globalmente (ex : TrocarSenhaObrigatorio).

Fixture

Arquivos YAML/JSON ou funções pytest que populam o banco para testes.

ORM

Camada de abstração de banco de dados do Django.

Sinal (Signal)

Gatilhos automáticos disparados após eventos de banco (post_save, post_delete).

5. Dicionário de Dados — interessados_interessado

Mapeamento técnico da entidade principal de armazenamento de dados dos cidadãos.

Campo

Tipo

Obrigatório

Validação

id

UUID

Sim

Chave primária (PK).

cpf

varchar

Sim

Criptografado (Fernet), deve ser único no sistema.

nis

varchar

Não

Indexado para buscas de prioridade.

nome_completo

varchar

Sim

Limite máximo de 150 caracteres.

email

varchar

Sim

Formato de e-mail válido e único.

consentimento_lgpd

bool

Sim

Flag indicativa de aceite dos termos de privacidade.

6. Dicionário de Dados — selecao_inscricao

Estrutura de dados que registra a participação dos interessados nos eventos de seleção.

Campo

Tipo

Obrigatório

FK / Referência

id

UUID

Sim

Chave primária (PK).

interessado_id

UUID

Sim

FK para interessados_interessado.

evento_id

UUID

Sim

FK para eventos_evento.

data_inscricao

timestampz

Sim

Indexado para critérios de desempate.

status

varchar

Sim

Pendente, Classificado, Confirmado ou Desistente.

5. Diagrama de Entidades e Relacionamentos

Diagrama-ER---bdmetareciclagem---27-04-2026.png

6. Dicionário de Dados — selecao_classificacao

Entidade responsável por armazenar o resultado do processamento do ranking.

Campo

Tipo

Obrigatório

id

UUID

Sim

inscricao_id

UUID

Sim

score

numeric

Sim

posicao

int

Sim

data_processamento

timestampz

Sim

Documento elaborado em 12 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 02-Estado-Atual-Dinamica.docx

MetaReciclagem

02-ESTADO-ATUAL-DINAMICA-V.3.0

Documentação Técnica de Arquitetura, APIs e Status Funcional

12 de maio de 2026

1. ARQUITETURA GERAL DO SISTEMA

O sistema é estruturado sobre o framework Django 5.2.4, utilizando uma arquitetura baseada em MVT (Model-View-Template) estendida por uma Service Layer robusta. Esta camada de serviço isola a lógica de negócio complexa, como o processamento de classificações e regras de elegibilidade, das views de apresentação. O ambiente é configurado para execução em Python 3.13.2 com persistência de dados em PostgreSQL 15+. A segurança é reforçada por middlewares de Content Security Policy (django-csp), proteção contra força bruta (django-axes) e criptografia de dados sensíveis em repouso via django-encrypted-model-fields.

1.1. Divisão de Aplicações (Apps)

A modularidade do sistema é garantida pela separação em 8 aplicações distintas, cada uma com responsabilidades bem definidas:

accounts: Gerencia a autenticação e autorização de usuários internos (staff), controlando permissões granulares de acesso ao painel administrativo.

interessados: Responsável pelo ciclo de vida do candidato. Implementa a criptografia Fernet para o campo CPF, garantindo a privacidade dos dados sensíveis.

eventos: Camada de configuração onde são definidos os cursos, turmas, períodos de inscrição e quantitativo de vagas disponíveis.

selecao: Core do sistema que abriga o ClassificadorService, responsável pela execução das regras de ranking e desempate.

academico: Gerencia o fluxo pós-seleção, incluindo o registro de notas, controle de frequência, efetivação de matrículas e emissão de certificados.

portal: Interface pública de interação com o usuário externo, focada em usabilidade e acessibilidade para consulta de editais e inscrições.

dashboard: Provê visualizações analíticas e relatórios gerenciais sobre o status das seleções e ocupação de vagas.

scripts_admin: Conjunto de utilitários para manutenção do banco de dados, migrações complexas e rotinas de limpeza de dados obsoletos.

1.2. Fluxo de Dados (6 Fases)

O ciclo de vida da informação no sistema percorre seis estágios sequenciais:

Cadastro: O interessado registra seus dados básicos, com validação rigorosa de CPF e criptografia imediata.

Inscrição: O candidato manifesta interesse em um evento específico, gerando um registro de participação vinculado ao seu perfil.

Classificação: O sistema processa os critérios de pontuação e desempate, gerando o ranking preliminar e final.

Matrícula: Os candidatos classificados dentro das vagas são convocados para a efetivação do registro acadêmico.

Avaliação: Durante o curso, são registrados os índices de aproveitamento (notas) e a assiduidade (frequência).

Certificação: Após a conclusão com êxito, o sistema gera o certificado digital com código de autenticidade verificável.

2. ENDPOINTS E APIS DOCUMENTADAS

O sistema opera primordialmente em ambiente de intranet, não expondo APIs públicas para consumo externo não autenticado, exceto nos fluxos de prospecção e login. Abaixo, detalham-se os endpoints principais que sustentam a dinâmica da aplicação.

Endpoint URL

Método

Autenticação

Parâmetros

Resposta

Status

/api/interessados/cadastro/

POST

Anônimo

CPF, email, senha

Interessado object

201

/api/interessados/login/

POST

Anônimo

CPF, senha

Token/Session

200

/api/eventos/

GET

Autenticado

query: status

Lista eventos

200

/api/inscricoes/

POST

Autenticado

evento_id

Inscrição object

201

/api/inscricoes/{id}/status

GET

Autenticado

id

Inscrição object

200

/api/classificacoes/processar

POST

Staff

evento_id

Classificação result

202

/api/matriculas/lote

POST

Staff

evento_id, lista_ids

Matrícula objects

201

/api/avaliacao/{id}

GET

Autenticado

id

Avaliação object

200

/api/certificados/gerar

POST

Autenticado

matricula_id

Certificado URL

200

3. STATUS DE FUNCIONALIDADES

Abaixo apresenta-se o inventário atualizado do desenvolvimento, detalhando o nível de maturidade e a cobertura de testes de cada módulo funcional do sistema.

3.1. Funcionalidades Implementadas (✓)

Funcionalidade

Módulo

Status

Cobertura

Notas

Cadastro com validação CPF

interessados

✓ Completo

95%

Criptografia Fernet ativa

Login com rate-limiting

accounts

✓ Completo

90%

django-axes (5 tentativas)

Inscrição em eventos

selecao

✓ Completo

92%

Validação de unicidade

Classificação automática

selecao

✓ Completo

85%

ClassificadorService

Matrícula em lote

academico

✓ Completo

88%

Notificações automáticas

Consulta de desempenho

academico

✓ Completo

80%

Notas/Frequência real-time

Geração de certificados

academico

✓ Completo

82%

Código de autenticidade

LGPD - Direito esquecimento

interessados

✓ Completo

78%

Anonimização irreversível

Relatórios em Excel

dashboard

✓ Completo

75%

Via Django Admin

Auditoria (logs)

accounts

✓ Completo

70%

Rastreamento de ações

3.2. Em Progresso (⏳) e Pendente (⏸️)

Funcionalidade

Módulo

Status

Cobertura

Notas

Containerização Docker

infra

⏳ Planejado

0%

Pós-testes automatizados

Email assíncrono (Celery)

comunicacao

⏳ Planejado

0%

Upgrade futuro de infra

Migrações de dados legados

scripts

⏸️ Hold

0%

Aguardando datacenter

Documento elaborado em 12 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 04-Desenvolvimento-Manutencao.docx

Prefeitura Municipal de Sorocaba

04-DESENVOLVIMENTO E MANUTENÇÃO V.3.0

Guia Técnico de Operação, Qualidade e Sustentabilidade do Sistema MetaReciclagem

12 de maio de 2026

1. GUIA DE DESENVOLVIMENTO RÁPIDO

Este guia estabelece os procedimentos padronizados para a configuração do ambiente de desenvolvimento e o fluxo de trabalho técnico, garantindo que todos os analistas operem sob as mesmas premissas de infraestrutura e versionamento.

1.1 Setup Local Windows

Para iniciar o desenvolvimento no sistema MetaReciclagem em ambiente Windows, siga rigorosamente a sequência de comandos abaixo no terminal (PowerShell ou CMD):

Clonar repositório: git clone <url_do_repositorio>

Criar ambiente virtual: python -m venv venv

Ativar ambiente virtual: venv\Scripts\activate

Instalar dependências: pip install -r requirements.txt

Configurar variáveis de ambiente: Criar arquivo .env na raiz com as chaves SECRET_KEY, DATABASE_URL, FERNET_KEY, EMAIL_HOST, EMAIL_PORT e AXES_FAILURE_LIMIT.

Executar migrações: python manage.py migrate

Criar usuário administrador: python manage.py createsuperuser

Iniciar servidor de desenvolvimento: python manage.py runserver

1.2 VS Code Essentials

A produtividade e a padronização do código são sustentadas pelo uso correto das ferramentas de edição. Recomenda-se a seguinte configuração no VS Code:

Extensões Obrigatórias: Python (Microsoft), Django (Baptiste Darthenay) e Pylance.

Interpretador: Configurar o VS Code para utilizar o binário localizado em venv/bin/python.

Debug: Utilizar as configurações de launch.json específicas para Django para permitir breakpoints em Views e Services.

Terminal: Utilizar preferencialmente o PowerShell integrado para compatibilidade com os scripts de ativação.

1.3 Fluxo de Commit

O versionamento segue o modelo de ramificação por funcionalidade. Nenhuma alteração deve ser feita diretamente na branch principal.

Branch: Criar sempre a partir de main com o padrão feature/nome-descritivo.

Mensagem de Commit: Deve seguir o padrão [TIPO] Descrição breve e objetiva.

Tipos de Commit:FEATURE (nova funcionalidade), FIX (correção de erro), DOCS (documentação), REFACTOR (melhoria de código sem alteração lógica) e TEST (adição ou modificação de testes).

Pull Request (PR): Deve conter uma descrição clara das alterações e ser submetido para revisão antes do merge.

2. CODE REVIEW CHECKLIST

O processo de revisão de código é obrigatório para manter a integridade do sistema e a manutenibilidade a longo prazo. O revisor e o autor devem validar os seguintes pontos:

2.1 Antes de Commitar

Item de Verificação

Critério de Aceitação

Testes Automatizados

Todos os testes devem ser executados via pytest e apresentar status de sucesso.

Cobertura de Código

A cobertura deve ser superior a 80%, validada via pytest --cov.

Lógica de Negócio

Ausência de valores hardcoded; uso de constantes ou configurações em .env.

Documentação

Presença de docstrings descritivas em todos os Models e Services.

Nomenclatura

Uso de PascalCase para classes e snake_case para funções, métodos e variáveis.

Performance

Ausência de N+1 queries através do uso estratégico de select_related e prefetch_related.

Segurança

Validação de dados de entrada, proteção contra CSRF, XSS e SQL Injection.

2.2 Pré-Deploy

Antes da promoção do código para o ambiente de produção, os seguintes itens devem ser confirmados:

Aprovação: O Code Review deve ter sido aprovado por ao menos um segundo desenvolvedor.

Staging: Migrações e novas funcionalidades devem ter sido testadas em ambiente de homologação (staging).

Backup: Garantir a existência de um backup recente e íntegro do banco de dados.

Rollback: Existência de um plano de contingência documentado para reversão imediata em caso de falha.

Compliance: Validação de conformidade com a LGPD para qualquer manipulação de dados sensíveis.

3. TROUBLESHOOTING - ERROS COMUNS EM DESENVOLVIMENTO

Esta seção cataloga os erros mais frequentes encontrados durante o ciclo de desenvolvimento e suas respectivas resoluções técnicas.

Erro Identificado

Causa Provável

Solução Recomendada

ModuleNotFoundError

Ambiente virtual (venv) inativo ou dependências não instaladas.

Ativar o venv e executar pip install -r requirements.txt.

ImportError em Backend

InteressadoBackend não registrado nas configurações.

Validar se apps.interessados.authentication.InteressadoBackend consta em AUTHENTICATION_BACKENDS.

Fernet Key Inválida

FIELD_ENCRYPTION_KEY ausente ou incorreta no .env.

Gerar nova chave via script Python e atualizar o arquivo de ambiente.

Falha no Envio de Email

Configurações de HOST ou PORT incorretas para a rede municipal.

Validar o .env com o IP 10.30.166.54 e porta 587.

Erro 429 (Rate Limit)

Bloqueio pelo django-axes após excesso de tentativas.

Aguardar o timeout ou resetar o acesso via Django Admin (axes_accessattempt).

Conflito de Migração

Criação simultânea de migrações em branches distintas.

Resolver manualmente ou utilizar makemigrations --merge.

Timeout em Relatórios

Ocorrência de N+1 Query em loops de processamento.

Implementar prefetch_related() para relacionamentos Many-to-Many.

4. FLUXO DE DADOS COMPLETO (FIM A FIM)

O ciclo de vida da informação no MetaReciclagem é dividido em seis fases críticas, garantindo a rastreabilidade desde o cadastro inicial até a emissão do certificado.

4.1 Fases do Processamento

Fase 1 - Cadastro: O interessado acessa o portal e fornece CPF, email e senha. O sistema valida a unicidade do CPF, aplica criptografia Fernet e registra os dados em interessados_interessado, disparando o email de confirmação.

Fase 2 - Inscrição: Após autenticação, o usuário seleciona um evento. O sistema valida a unicidade da inscrição por evento e a obrigatoriedade do NIS, criando o registro em selecao_inscricao com status Pendente.

Fase 3 - Classificação: O ClassificadorService processa os inscritos com base nos critérios de score. Em caso de empate, utiliza-se a data de inscrição com precisão de milissegundos. O ranking é persistido em selecao_classificacao.

Fase 4 - Matrícula: A equipe administrativa confirma os aprovados conforme a disponibilidade de vagas. O status é alterado para Confirmado e o registro em academico_matricula é gerado automaticamente.

Fase 5 - Avaliação: Durante o curso, instrutores lançam notas e frequências. A aprovação exige nota &ge; 7.0 e frequência &ge; 75%, resultando no status final de Aprovado ou Reprovado.

Fase 6 - Certificação: Para alunos aprovados, o sistema gera o academico_certificado com código de autenticidade único e assinatura digital, disponibilizando-o para download imediato.

4.2 Tratamento de Dados Sensíveis

A segurança dos dados é prioridade absoluta, seguindo os seguintes padrões:

CPF e NIS: Armazenados com criptografia simétrica Fernet em nível de banco de dados.

Senhas: Protegidas por algoritmo de hash bcrypt (padrão Django).

Anonimização: Implementação do "Direito ao Esquecimento" da LGPD, onde dados sensíveis são substituídos por hashes não identificáveis após solicitação de exclusão.

5. TESTES E FIXTURES

A robustez do sistema é garantida por uma suíte de testes automatizados que validam desde a integridade dos modelos até fluxos complexos de classificação.

5.1 Estrutura e Ferramentas

O projeto utiliza o framework pytest. A estrutura de testes é organizada no diretório tests/, contendo arquivos específicos para modelos, serviços, views e formulários. O arquivo conftest.py centraliza as fixtures globais.

5.2 Fixtures e Fábricas

Utilizamos factory-boy para geração de dados de teste consistentes:

interessado_factory: Gera registros com CPFs válidos e consentimento LGPD.

evento_factory: Cria eventos com configurações variadas de vagas e critérios.

inscricao_factory: Simula o processo de inscrição vinculando interessados a eventos.

matricula_factory: Gera registros acadêmicos para testes de avaliação e certificação.

5.3 Execução de Testes

Comandos principais para o desenvolvedor:

pytest: Executa a suíte completa de testes.

pytest --cov: Gera relatório de cobertura de código.

pytest -v: Modo verboso para detalhamento de falhas.

pytest tests/ -k "cpf": Executa apenas testes que contenham "cpf" no nome.

"A meta de cobertura estabelecida para os módulos críticos (interessados, selecao e academico) é de no mínimo 80%."

6. MIGRAÇÕES E DEPLOY

O gerenciamento de mudanças no esquema do banco de dados e a publicação de novas versões seguem protocolos rígidos para evitar indisponibilidade do serviço.

6.1 Fluxo de Migrações

As migrações devem ser criadas localmente após alterações nos modelos e testadas exaustivamente. Em ambientes de produção, o comando python manage.py migrate --plan deve ser executado previamente para inspeção visual das alterações planejadas.

6.2 Estratégia de Rollback

Em caso de falha crítica pós-migração:

Identificar a última migração estável através de showmigrations.

Reverter o estado do banco via python manage.py migrate app_name numero_anterior.

Caso haja corrupção de dados, realizar o Restore a partir do backup realizado imediatamente antes do deploy.

6.3 Protocolo de Deploy em Produção

O deploy no datacenter municipal deve ocorrer em janelas de manutenção programadas, seguindo estes passos:

Preparação: Backup completo de banco de dados e arquivos de mídia.

Atualização: Execução de git pull origin main e atualização de dependências via pip.

Ativos: Coleta de arquivos estáticos via collectstatic.

Banco: Execução das migrações pendentes.

Serviço: Reinicialização dos processos Gunicorn ou uWSGI.

Validação: Execução de health checks e monitoramento de logs de erro em tempo real.

Atenção: Nunca execute migrações em produção sem a confirmação de um backup íntegro e testado.

_____________________________             _____________________________

RESPONSÁVEL TÉCNICO                                                COORDENAÇÃO DE TI

Local e data: Sorocaba/SP, 12 de maio de 2026

Documento elaborado em 12 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 05-Manuais-Usuarios.docx

Prefeitura Municipal de Sorocaba

05-MANUAIS-USUARIOS-V.3.0

Guia de Operação para Interessados, Staff e Administradores

12 de maio de 2026

1. MANUAL DO INTERESSADO

Seja bem-vindo à Plataforma Prefeitura Sorocaba, o portal centralizado para gestão de cursos e eventos do programa MetaReciclagem. Este manual orienta o cidadão desde o cadastro inicial até a obtenção da certificação.

1.1. Criação de Conta e Acesso

Para utilizar os serviços, o usuário deve realizar o cadastro fornecendo CPF, e-mail válido e senha. É obrigatória a leitura e aceitação dos termos da LGPD (Lei Geral de Proteção de Dados). Após o preenchimento, um e-mail de confirmação será enviado; o acesso só será liberado após a validação deste link.

O login é realizado via CPF e senha. O sistema possui uma política de segurança rigorosa: após 5 tentativas incorretas, o acesso será bloqueado por 30 minutos (rate-limit). Caso esqueça a senha, utilize a função "Esqueci minha senha" na tela de login.

1.2. Inscrição e Acompanhamento

Navegue em "Eventos Disponíveis", selecione o curso desejado e clique em "Inscrever-se". Inicialmente, o status da inscrição será Pendente. O acompanhamento deve ser feito na aba "Minhas Inscrições", onde os seguintes status podem ser exibidos:

Status

Significado

Pendente

Aguardando processamento da classificação.

Classificado

Selecionado conforme critérios, aguardando matrícula.

Confirmado

Matrícula efetivada e participação garantida.

Não Classificado

Pontuação insuficiente para as vagas disponíveis.

Expirada

Prazo de matrícula ou evento encerrado.

Desistente

Cancelamento solicitado pelo usuário.

1.3. Desempenho e Certificação

Na seção "Meu Desempenho", o aluno consulta suas notas e frequência. Para aprovação, o sistema exige cumulativamente nota ≥ 7.0 e frequência ≥ 75%. Uma vez aprovado, o certificado estará disponível em "Meus Certificados" para download em PDF, contendo um código de autenticidade para validação externa.

Direito ao Esquecimento (LGPD): O usuário pode solicitar a exclusão de seus dados em Configurações  Privacidade. Após confirmar o CPF e validar o e-mail, o sistema realizará a anonimização completa dos dados em até 24 horas.

1.4. FAQ do Interessado

Como cancelo uma inscrição? Acesse "Minhas Inscrições", cancele a atual e, se desejar, inscreva-se em outro evento. 

Posso me inscrever em múltiplos eventos? Sim, desde que não haja conflito de horários. 

Quando recebo o certificado? Imediatamente após o lançamento da aprovação pelo Staff.

2. MANUAL DO STAFF

O perfil Staff é destinado aos operadores da Prefeitura que gerenciam o ciclo de vida das turmas e alunos. O acesso é realizado via admin.metareciclagem.sorocaba.gov.br com credenciais fornecidas pela TI. No primeiro acesso, a troca de senha é obrigatória.

2.1. Dashboard e Gestão de Vagas

O Dashboard fornece métricas em tempo real sobre inscrições pendentes, classificadas e ativas. É possível monitorar o percentual de ocupação das vagas e a volumetria da lista de espera para cada evento configurado.

2.2. Processamento de Classificação e Matrícula

O processamento de classificação é a etapa crítica onde o sistema aplica os algoritmos de seleção. O Staff deve selecionar o evento e clicar em "Processar Classificação".

Lógica de Desempate: O sistema ordena por Score (DESC). Em caso de empate, o critério é a data de inscrição com precisão de milissegundos (ASC - o mais antigo vence).

Após a classificação, o Staff revisa a lista e clica em "Emitir Matrículas". Este comando altera o status para Confirmado e dispara notificações automáticas aos selecionados.

2.3. Lançamento de Notas e Relatórios

As avaliações devem ser lançadas por evento/turma. O sistema valida entradas de nota (0.0 a 10.0) e frequência (0 a 100%). Para fins de auditoria e gestão externa, o Staff pode gerar relatórios em formato .xlsx (Excel) filtrando por tipo de dado e período.

3. MANUAL DO ADMINISTRADOR

O Administrador possui acesso Root via Django Admin para configurações estruturais do sistema. Todas as ações realizadas neste nível são registradas em logs de auditoria para rastreabilidade completa.

3.1. Configuração de Eventos e Critérios

A criação de eventos exige o preenchimento de metadados (nome, descrição, datas de inscrição e realização, vagas e poster). Após a criação, o Administrador deve definir os Critérios de Seleção, associando pesos e scores (ex: Critério Social peso 5, Critério Idade peso 3).

3.2. Manutenção e Segurança

O sistema realiza backups automáticos diários às 02:00. O monitoramento de infraestrutura (CPU, Memória e Disco) é constante, com alertas disparados ao atingir 90% de uso de disco. Em "Logs de Auditoria", é possível filtrar qualquer alteração por usuário, data ou tabela afetada.

4. NAVEGAÇÃO E INTERFACE (UI)

A interface é adaptativa conforme o perfil de acesso do usuário autenticado:

4.1. Estrutura de Menus

5. FAQ GERAL

Qual o horário de suporte? O suporte técnico funciona de segunda a sexta, das 08h às 17h. Fora deste horário, solicitações devem ser feitas via abertura de ticket.

Como funciona a segurança dos dados? O sistema utiliza criptografia Fernet para dados sensíveis (CPF/NIS), possui cabeçalhos de segurança CSP e segue rigorosamente a LGPD, garantindo o direito ao esquecimento.

O que acontece em caso de empate no score? O desempate é automático e favorece a inscrição realizada primeiro, considerando a data e hora exata em milissegundos.

Como recuperar o acesso à conta? Na tela de login, clique em "Esqueci minha senha". Um link de redefinição será enviado ao e-mail cadastrado. Por segurança, o link expira em curto prazo.

Local e data: Sorocaba, 12 de maio de 2026

Versão do Documento: 3.0

Documento elaborado em 12 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 06-Repositorio-Git.docx

Prefeitura de Sorocaba - Projeto MetaReciclagem

06-REPOSITÓRIO-GIT-V3.0

Documentação Técnica de Repositório e Boas Práticas

12 de maio de 2026

1. README — MetaReciclagem: Sistema de Gestão de Inscrições Municipais

O MetaReciclagem é uma plataforma municipal desenvolvida para a Prefeitura de Sorocaba, focada na gestão integral de processos de inscrição, classificação automática e acompanhamento acadêmico. O sistema visa automatizar fluxos complexos, garantindo transparência e auditabilidade em todas as etapas do processo seletivo e educacional.

1.1 Stack Técnico

Framework Web: Django 5.2.4

Linguagem: Python 3.13.2

Banco de Dados: PostgreSQL 15+

Segurança (Rate-limiting): django-axes 6.1.1

Segurança (Headers): django-csp 4.0+

Criptografia: django-encrypted-model-fields (Algoritmo Fernet)

1.2 Funcionalidades Principais

Cadastro de usuários com validação de CPF criptografado em repouso.

Inscrição em eventos com validação rigorosa de unicidade e pré-requisitos.

Classificação automática baseada em algoritmo de desempate parametrizável.

Gestão de matrícula em lote com sistema de notificações automáticas.

Lançamento de notas, frequência e controle de desempenho acadêmico.

Geração e validação de certificados digitais com assinatura eletrônica.

Conformidade com a LGPD, incluindo ferramentas para o direito ao esquecimento.

Exportação de relatórios gerenciais em formato Excel.

Sistema de auditoria completa registrando logs de criação, alteração e exclusão.

1.3 Quick Start (Guia Rápido)

Realizar o clone do repositório: git clone <url_do_repositorio>

Criar o ambiente virtual: python -m venv venv

Ativar o ambiente virtual: venv\Scripts\activate

Instalar as dependências: pip install -r requirements.txt

Configurar o arquivo .env com as chaves: SECRET_KEY, DATABASE_URL, FERNET_KEY, EMAIL_HOST, EMAIL_PORT.

Executar as migrações do banco de dados: python manage.py migrate

Criar o usuário administrador: python manage.py createsuperuser

Iniciar o servidor de desenvolvimento: python manage.py runserver

1.4 Dependências Críticas 

django-axes 6.1.1

 django-csp 4.0+

 django-encrypted-model-fields

2. CHANGELOG — Histórico de Versões

2.1 Versão [3.0] — 12 de maio de 2026

Adicionado:

Consolidação completa da documentação técnica em 6 arquivos estruturados.

Arquivo 01-Fundacoes-Estatica: Unificação de ADRs, Regras, Glossário e Dicionário de Dados.

Arquivo 02-Estado-Atual-Dinamica: Consolidação de Arquitetura, Endpoints e Status de Funcionalidades.

Arquivo 03-Prompts-Contextos-IA: Definição de Perfil, Contexto, Instruções e Padrões para IA.

Arquivo 04-Desenvolvimento-Manutencao: Guias de Setup, Code-Review, Troubleshooting, Fluxo, Testes e Migrações.

Arquivo 05-Manuais-Usuarios: Manuais para Candidatos, Staff, Admin, Navegação e FAQ.

Arquivo 06-Repositorio-Git: README, CHANGELOG, CONTRIBUTING, ROADMAP e SECURITY.

Arquivo 07-Visao-Executiva-Diagramas: Documentação de Negócio e Lógica de Processos do Sistema.

Implementação de seções específicas para Troubleshooting-Dev e documentação de Endpoints-APIs.

Expansão dos guias de desenvolvimento e protocolos de testes automatizados.

Alterado:

Reorganização estrutural da documentação, reduzindo de 10 arquivos dispersos para 6 volumes consolidados.

Padronização de nomenclatura e versionamento semântico em todos os documentos.

Corrigido:

Eliminação de duplicidade em registros de ADRs (Architectural Decision Records).

Unificação de glossários técnicos e de negócio em uma única fonte da verdade.

2.2 Versão [2.0] — 08 de maio de 2026

Adicionado:

Documentação técnica inicial consolidada do sistema.

Implementação de testes automatizados utilizando o framework pytest.

Introdução da Service Layer para isolamento da lógica de negócio.

Implementação de mecanismos de suporte à conformidade com a LGPD.

2.3 Versão [1.0] — Data de Inicialização

Adicionado:

Estrutura base do sistema MetaReciclagem.

Configuração de 8 aplicações Django: accounts, interessados, eventos, selecao, academico, portal, dashboard, scripts_admin.

Sistema de autenticação customizado com InteressadoBackend e AxesStandaloneBackend.

Integração de serviço de e-mail via DataCenter municipal.

3. CONTRIBUTING — Guia de Contribuição

3.1 Padrões de Desenvolvimento

Para manter a consistência do código, todos os contribuidores devem seguir as convenções abaixo:

- Models: Utilizar PascalCase (ex: Candidato, EventoVaga).

- Variáveis e Funções: Utilizar snake_case (ex: nome_completo, calcular_score).

- Constantes: Utilizar SCREAMING_SNAKE_CASE (ex: STATUS_APROVADO ).

- Documentação: Incluir Docstrings em todos os Models, Views e Services. 

- Lógica: Centralizar lógica complexa na Service Layer (ex: ClassificadorService).

- Testes: Manter cobertura mínima de 80% em aplicações críticas utilizando pytest.

3.2 Segurança e Performance

Proibido o uso de hardcoding para segredos ou chaves; utilizar sempre variáveis de ambiente (.env).

Garantir proteção contra CSRF, XSS e SQL Injection através das ferramentas nativas do ORM Django.

Implementar rate-limiting rigoroso (5 tentativas falhas resultam em bloqueio de 30 minutos).

Otimizar consultas ao banco de dados utilizando select_related() e prefetch_related() para evitar o problema de N+1 queries.

3.3 Fluxo de Trabalho (Git Flow)

Realizar o Fork do repositório oficial.

Criar uma branch específica: feature/nome-descritivo ou fix/nome-descritivo.

Realizar commits padronizados: [TIPO] Descrição breve (Tipos: FEATURE, FIX, DOCS, REFACTOR, TEST).

Realizar o Push para a branch remota.

Abrir um Pull Request (PR) com descrição detalhada das alterações.

O código passará por revisão (Code Review) antes da aprovação e merge.

4. ROADMAP — Plano de Evolução do Sistema

4.1 Q2 2026 (Fase Atual)

Consolidação de documentação técnica e funcional completa [CONCLUÍDO].

Estabelecimento de cobertura de testes automatizados superior a 80% [CONCLUÍDO].

Definição e implementação do processo formal de Code Review [CONCLUÍDO].

4.2 Q3 2026 (Próximas Etapas)

Containerização: Implementação de Docker e Docker Compose para padronização de ambientes.

Processamento Assíncrono: Integração com Celery e Redis para envio de e-mails e tarefas pesadas em background.

Notificações: Implementação de lógica de reativação e retry para falhas de comunicação.

4.3 Q4 2026 (Escalabilidade e Monitoramento)

Observabilidade: Setup de monitoramento e logs centralizados (ELK Stack).

Performance: Implementação de cache estratégico com Redis e otimização de queries complexas.

Infraestrutura: Configuração de CDN para entrega de ativos estáticos e documentos.

4.4 2027 e Visão de Futuro

Migração de Dados: Execução de processos de ETL para importação de dados de sistemas legados.

Expansão Geográfica: Adaptação do sistema para suporte multi-município com segmentação de dados.

Integração: Desenvolvimento de API pública autenticada para integração com outros sistemas municipais.

Mobilidade: Desenvolvimento de aplicação móvel nativa para acompanhamento pelos interessados.

5. SECURITY — Política de Segurança

5.1 Relato de Vulnerabilidades

Caso identifique uma vulnerabilidade de segurança, solicitamos que não abra uma issue pública. O relato deve ser feito exclusivamente através do canal de comunicação confidencial da equipe de segurança da Prefeitura de Sorocaba.

5.2 Padrões de Segurança Implementados

Autenticação: Uso de InteressadoBackend customizado e AxesStandaloneBackend para proteção contra força bruta.

Criptografia de Dados: Utilização de FIELD_ENCRYPTION_KEY para dados sensíveis (CPF e NIS) através do django-encrypted-model-fields.

Headers de Segurança: Configuração de Content Security Policy (CSP), HSTS, X-Frame-Options e X-Content-Type-Options.

Conformidade LGPD: Implementação de fluxos de consentimento, anonimização irreversível para direito ao esquecimento e logs de auditoria detalhados.

Infraestrutura de E-mail: Uso de CustomEmailBackend via DataCenter municipal com TLS obrigatório e rate-limiting de envios.

Backup e Recuperação: Rotina de backup automático diário às 02:00 com retenção de 30 dias e testes de integridade periódicos.

Atenção: O uso de TLS/SSL é obrigatório em todos os ambientes de produção. Nenhuma credencial deve ser armazenada em texto claro no código-fonte.

Nota: Para detalhes adicionais, consulte a pasta /documentacao, que contém os arquivos consolidados de 01 a 05.

Local e data: Sorocaba, 12 de maio de 2026

RESPONSÁVEL TÉCNICO

Documento elaborado em 12 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: 07-Visao-Executiva-Diagramas.docx

Prefeitura de Sorocaba

07 — VISÃO EXECUTIVA E DIAGRAMAS DE FLUXO

Documentação de Negócio e Lógica de Processos do Sistema

13 de maio de 2026

1. O QUE É METARECICLAGEM?

O MetaReciclagem é uma plataforma digital municipal que automatiza o ciclo completo de gestão de inscrições, classificação e acompanhamento acadêmico. Desenvolvida para a Prefeitura de Sorocaba, a solução resolve ineficiências históricas de processos manuais, mitiga riscos de segurança de dados e estabelece um novo padrão de transparência pública.

O sistema atende a três perfis distintos: Candidatos (foco em autoatendimento e usabilidade), Staff (foco em eficiência operacional) e Administradores (foco em governança e auditoria). Tecnicamente, a plataforma é implementada em Django 5.2.4, Python 3.13.2 e PostgreSQL 15+, contando com conformidade nativa à LGPD.

Iniciado em outubro de 2025, o projeto encontra-se atualmente, em maio de 2026, na fase final de consolidação e testes de estresse, estando tecnicamente pronto para implantação em larga escala no datacenter municipal.

1.1 Por que MetaReciclagem?

Redução de 80% no tempo de processamento: Transforma dias de trabalho manual em minutos de processamento automatizado de seleções.

Transparência Total: Candidatos acompanham o status de suas solicitações em tempo real, reduzindo drasticamente o volume de chamados de suporte.

Conformidade LGPD: Proteção nativa de dados sensíveis através de criptografia Fernet para campos críticos como CPF e NIS.

Gestão Baseada em Dados: Geração automática de relatórios gerenciais para suporte a decisões fundamentadas da administração pública.

Segurança Jurídica: Manutenção de uma trilha completa de auditoria, registrando quem realizou cada ação, o quê foi alterado e quando ocorreu.

ROI Estimado: Retorno sobre o investimento previsto entre 6 a 12 meses, devido à liberação de equipe operacional e mitigação de riscos jurídicos.

2. DIAGRAMA 1 — FLUXO DE TRABALHO (Sistema de Gestão de Cursos)

[Diagrama---Fluxo-de-Trabalho.pdf]

2.1 Descrição Passo a Passo

Fase 1: PLANEJAMENTO E INSCRIÇÕES — O curso inicia no estado de Planejamento, onde administradores configuram eventos, vagas e cronogramas. Ao ser publicado, o status muda para Inscrições Abertas. Candidatos realizam inscrições que geram registros com status Pendente, permitindo o cancelamento por iniciativa do usuário.

Fase 2: ENCERRAMENTO E CLASSIFICAÇÃO — Após o encerramento do prazo, o curso transita para Em Classificação. O sistema executa o ClassificadorService, processando as inscrições pendentes e atribuindo scores baseados em critérios objetivos. O resultado gera dois caminhos: Classificado (dentro da quantidade de vagas disponibilizadas) e Lista de Espera (acima do número de vagas).

Fase 3: DIVULGAÇÃO E MATRÍCULA — Com o curso em Resultado Divulgado, as inscrições classificadas passam para Aguardando Confirmação. Se o aluno confirmar a matrícula no prazo, o status evolui para Confirmado e a matrícula torna-se Ativa. Caso contrário, a inscrição é marcada como Expirada, liberando a vaga para a lista de espera.

Fase 4: EXECUÇÃO DO CURSO — Durante o status Em Andamento, a matrícula ativa permite o acompanhamento de notas e frequência. O aluno pode concluir o ciclo, solicitar o status Trancada para pausa temporária ou realizar o Cancelamento definitivo da inscrição.

Fase 5: FINALIZAÇÃO — Ao atingir o status Finalizado, o sistema processa o desfecho: matrículas de alunos que completaram o ciclo tornam-se Concluídas (aptas para certificação), enquanto as demais permanecem como Trancadas ou Canceladas conforme o histórico.

2.2 Legenda de Status

Curso: Planejamento, Inscrições Abertas, Em Classificação, Resultado Divulgado, Em Andamento, Finalizado, Inscrições Encerradas, Cancelado.

Inscrição: Pendente, Classificado, Cancelada, Expirada, Confirmado, Desistente, Lista de Espera, Não Localizado.

Matrícula: Aguardando Confirmação, Ativa, Concluída, Trancada, Não Iniciada.

Simbologia: → (Fluxo principal), ⇢ (Fluxo alternativo/exceção), ◇ (Ponto de decisão).

3. DIAGRAMA 2 — FLUXO DE RECUPERAÇÃO DE SENHA

[Diagrama---Recuperação-de-Senha.pdf]

3.1 Descrição Passo a Passo

Fase 1: IDENTIFICAÇÃO DA ÁREA — O processo inicia com a solicitação de recuperação. O sistema segmenta o fluxo entre Área Administrativa ou Área de Interessados, garantindo que as credenciais sejam validadas contra as tabelas de usuários corretas.

Fase 2: VALIDAÇÃO DO USUÁRIO — Na área administrativa, a validação ocorre via Username. Na área de interessados, a chave de busca é o CPF. Caso o usuário não seja localizado no banco de dados, o sistema retorna um erro de Falha: Usuário não encontrado e encerra o processo por segurança.

Fase 3: VALIDAÇÃO DO EMAIL — Após localizar o usuário, o sistema verifica a existência de um e-mail válido e vinculado à conta. A ausência de um endereço de contato funcional resulta na interrupção do fluxo com a mensagem Falha: Email inválido.

Fase 4: GERAÇÃO E ENVIO DE CREDENCIAL — O sistema gera uma senha aleatória temporária e dispara um e-mail contendo um link de recuperação seguro. O usuário é notificado imediatamente sobre a emissão desta credencial provisória.

Fase 5: OBRIGAÇÃO DE TROCA — Ao acessar o sistema com a senha temporária, o MetaReciclagem impõe a mudança obrigatória de senha no primeiro login. Somente após a definição de uma nova senha definitiva o processo é marcado como Sucesso, restabelecendo o acesso pleno.

3.2 Legenda

Entrada: Solicitação de Recuperação de Senha.

Decisão: Segmentação de área, existência de usuário e validade de e-mail.

Sucesso: Recuperação concluída com troca obrigatória de credencial.

Falha: Interrupção por dados não localizados ou inconsistentes.

4. RESUMO DE IMPACTO

A implementação do fluxo de trabalho automatizado elimina gargalos de processamento manual e fornece visibilidade imediata aos candidatos, reduzindo a carga de trabalho do Staff municipal, que deixa de gerir planilhas externas para focar na análise de dados centralizados.

Complementarmente, o fluxo de recuperação de senha estabelece um equilíbrio entre segurança e usabilidade. A imposição de troca de senha no primeiro acesso garante que credenciais temporárias não se tornem vulnerabilidades permanentes, mantendo a integridade do acesso às áreas restritas.

Em conjunto, estes processos materializam os benefícios fundamentais do projeto: velocidade (redução de 80% no tempo de resposta), transparência (status em tempo real) e segurança robusta (aderência total à LGPD e trilhas de auditoria).

5. DIAGRAMA 3 — FLUXO DE CLASSIFICAÇÃO E MATRÍCULA EM LOTE

Descrição Geral de Classificação

A classificação é o núcleo da seleção. Após o encerramento das inscrições, o ClassificadorService processa todas as inscrições "Pendente" de um evento aplicando critérios previamente configurados pelo administrador.

Cada critério é binário (0 ou 1): candidato atende ou não atende. Quando atende, recebe pontos fixos configuráveis (ex: PCD = 5 pontos, NIS = 3 pontos). Score total é a soma acumulada. Inscrições com mesmo score entram em desempate automático.

Regras de Pontuação e Desempate

Critérios Automáticos Verificáveis:

PCD (Pessoa com Deficiência): validação automática via formulário

NIS (Número de Inscrição Social): validação contra base municipal

Programa Social: indicador booleano no cadastro

Faixa Etária (JOVEM, IDOSO): calculada a partir da data de nascimento

Cota Racial (COTA_RACIAL): seleção categórica (Parda, Preta, Indígena, etc)

Escolaridade (ESCOLARIDADE): nível informado na inscrição

Lógica de Desempate (quando dois candidatos têm score idêntico):

Se evento tem critério JOVEM ativo: ordena por idade ASC (mais jovem vence)

Se evento tem critério IDOSO ativo: ordena por idade DESC (mais velho vence)

Se nenhum critério de idade: ordena por data_inscricao ASC (quem se inscreveu primeiro vence, com precisão de milissegundos)

Resultado da Classificação:

Score DESC (maior para menor)

Dentro do mesmo score: aplicar desempate conforme regra acima

Atribuir posição ordinal (1º, 2º, 3º, etc)

Candidatos dentro das vagas: status "Classificado"

Candidatos excedentes: status "Lista de Espera" com posição na fila

Fluxo de Matrícula em Lote

Após publicação do resultado, o Staff executa a ação "Matrícula em Lote" selecionando um grupo de inscrições classificadas. O sistema realiza validações críticas antes de confirmar:

Capacidade: número de matrículas ≤ vagas disponíveis

Duplicatas: mesmo candidato não matricula 2x no mesmo evento

Atomicidade: ou todas as matrículas são confirmadas ou nenhuma (transação completa ou falha total)

Processamento por Linha:

Cada inscrição selecionada é processada individualmente

Se erro em uma linha (ex: candidato já matriculado): registro salva erro, continua processando demais

Erros são logados para revisão posterior

Notificação automática é enviada a cada candidato matriculado

Pós-Confirmação:

Status da inscrição muda para "Confirmado"

Matrícula recebe status "Ativa"

Se houver vagas restantes e há candidatos em "Lista de Espera": primeira fila é promovida automaticamente para "Aguardando Confirmação"

Relatórios Staff e Mural são gerados (PDF/Excel)

Quotas e Inclusão Social

O sistema implementa políticas de inclusão via quotas obrigatórias:

30% das vagas: reservadas para PCD (Pessoa com Deficiência)

40% das vagas: reservadas para Programa Social (beneficiários de programas municipais)

Remanescente: ampla concorrência

Cotas Raciais (se aplicável): definidas por regulamento municipal específico

Validação de Preenchimento:

Se cota PCD não preenche 30%, vagas remanescentes liberam para Programa Social

Se Programa Social não preenche 40%, vagas remanescentes liberam para ampla concorrência

Ordem de chamada: primeiro preenche todas as cotas, depois passa para próxima categoria

Relatórios Integrados

Após classificação e matrícula, dois tipos de relatório são gerados:

Relatório Staff (Confidencial): com CPF completo, email, telefone, programa social, status completo

Relatório Mural (Público): com CPF mascarado (XXX.XXX.XXX-YY), sem contatos, apenas status básico, com aviso de publicação

Ambos gerados em PDF e Excel, permitindo publicação em murais físicos (PDF impresso) ou planilhas compartilhadas (Excel com filtros).

DIAGRAMA 3 — FLUXO DE CLASSIFICAÇÃO E MATRÍCULA EM LOTE

Local e data: Sorocaba, 13 de maio de 2026

RESPONSÁVEL PELA DOCUMENTAÇÃO

Documento elaborado em 13 de maio de 2026. As informações contidas são de responsabilidade do solicitante.

---

## Arquivo: Instrucoes-IA-containerizacao.txt

Finalidade desta interação:
Continuidade no desenvolvimento de sistema em Django/Python/HTML/CSS/JS

Contexto:
Me ajude a fazer um alinhamento e dar continuidade.


Abaixo algumas informações de como devemos interagir


SEÇÃO 1: PERFIL DO DESENVOLVEDOR
Esta seção define o perfil técnico e as preferências de comunicação do responsável pelo projeto, visando alinhar a interação com modelos de inteligência artificial às necessidades reais de desenvolvimento e arquitetura.
Nome: Marcos Piardi
Cargo: Analista de Sistemas
Nível: Desenvolvedor Iniciante para desenvolvimento em Django/Python/HTML/CSS/JS que desenvolvia em clipper e delphi. 
Possui 17 anos de experiência em outras áreas, encontrando-se em fase de reaprendizado de programação. 

Ambiente de Trabalho: Sistema operacional Windows, utilizando VS Code configurado em Português Brasil. Tecnologias base: Python e Django.
Preferências de Comunicação: As interações devem ser realizadas em Português Brasil (PT-BR). O tom deve ser conciso, técnico e objetivo, sem a utilização de preâmbulos desnecessários. Respostas diretas são priorizadas.
Tecnologias Principais: Framework Django (MVT), banco de dados PostgreSQL e Python 3.13.2.
Padrões Adotados: Utilização de PascalCase para Models, snake_case para variáveis e funções, e SCREAMING_SNAKE_CASE para constantes.
Ênfase Técnica: Foco em Service Layer para isolamento de lógica complexa, uso de UUIDs como chaves primárias (PKs), implementação rigorosa de testes automatizados com pytest e manutenção de toda a documentação técnica em português.

SEÇÃO 2: CONTEXTO DO SISTEMA PARA IA
O sistema MetaReciclagem é uma plataforma municipal voltada à gestão integral de inscrições, classificação automática de candidatos e acompanhamento acadêmico.
2.1. Stack Tecnológica e Arquitetura
O projeto utiliza Django 5.2.4, Python 3.13.2 e PostgreSQL 15+. A segurança é reforçada por django-axes 6.1.1, django-csp 4.0+ e django-encrypted-model-fields.

O sistema é composto por 8 aplicações (Apps) principais:
accounts: Gestão de autenticação para o corpo técnico (staff).
interessados: Cadastro e perfil do candidato.
eventos: Gestão de cursos, editais e oferta de vagas.
selecao: Núcleo de inteligência contendo o ClassificadorService.
academico: Gestão pós-seleção (matrícula e notas).
portal: Interface pública de navegação e interação.
dashboard: Módulo de análise de dados e indicadores.
scripts_admin: Ferramentas utilitárias de administração.

2.2. Fluxo Operacional e Regras Críticas
O fluxo de negócio é dividido em 6 fases:
Cadastro → Inscrição → Classificação → Matrícula → Avaliação → Certificação.

As 10 ADRs (Architectural Decision Records) consolidadas são:
CPF identificador: Chave única de identificação do cidadão.
Fernet encryption: Criptografia simétrica para dados sensíveis.
Service Layer: Lógica de negócio fora de models e views.
JSONB: Armazenamento de dados semiestruturados no PostgreSQL.
Rate-limiting: Proteção contra ataques de força bruta.
CSP: Content Security Policy para mitigação de XSS.
Django Admin ERP: Uso do admin como interface de gestão interna.
pytest: Framework padrão para testes automatizados.
LGPD anonymization: Processos de anonimização para conformidade legal.
Email DataCenter: Integração com servidor SMTP interno.
Regras de Negócio: CPF único por evento; NIS obrigatório para cotas sociais; Score decrescente para classificação com desempate por data_inscricao em milissegundos; Aprovação exige nota ≥ 7.0 e frequência ≥ 75%.

SEÇÃO 3: INSTRUÇÕES PARA NOVAS CONVERSAS COM IA
O objetivo desta seção é padronizar as solicitações para otimizar o tempo de resposta e a precisão das análises geradas pela IA.
Crie um índice navegável das interações desta conversa;
A cada interação, quero que numere e date (dd/mm/yyyy) suas respostas;
Respostas em Português Brasil;
Nunca inventar dados ou informações;
Fazer perguntas específicas claramente quando houver dúvidas (não presumir);
Questionar decisões ambíguas em vez de assumir
Separação de PY, HTML, CSS e JavaScript em arquivos distintos
Gerar código apenas quando solicitado ou consentido (artefatos completos com cabeçalho padronizado)
Arquivo com código completo pronto para copy-paste (não trechos)
Modelo de cabeçalho:
"""
Arquivo: [nome_arquivo]
Caminho: [caminho_completo]
Finalidade: [finalidade do programa]
Atualizações:
 - [dd/mm/aaaa] - [descrição da mudança/alteração no código]
"""
Sempre copiar o cabeçalho existente e acrescentar as atualizações feitas
Quando necessário ou solicitado, colocar comentários no corpo do código indicando alterações e data
Código testável e funcional
Indicação clara de qual arquivo substituir e caminho
Fluxo Esperado:
1ª mensagem (Contexto + Código) → 2ª mensagem (Dúvidas da IA) → 3ª mensagem (Respostas do Desenvolvedor) → 4ª mensagem (Entrega da análise/documentação).

SEÇÃO 4: PADRÕES E CONVENÇÕES DE IMPLEMENTAÇÃO
4.1. Nomenclatura e Estrutura de Código
● Models: PascalCase (ex: Candidato, EventoVaga). Devem conter docstrings e validações no método clean().
● Variáveis/Funções: snake_case.
● Constantes: SCREAMING_SNAKE_CASE.
● PKs: Uso obrigatório de UUIDs.
4.2. Camadas de Lógica
● Views: Preferência por Function-Based Views (FBV). Devem ser otimizadas com select_related() e prefetch_related().
● Service Layer: Toda lógica complexa (classificação, certificados) deve residir em classes de serviço com métodos verbais (ex: processar_lote).
4.3. Segurança e Performance
● Segurança: Rate-limiting (5 tentativas = 30min de bloqueio) via django-axes. CSP ativo. Criptografia Fernet para CPF e NIS. Primeiro acesso exige troca de senha.
● Performance: Índices obrigatórios em campos de busca (CPF, Email, Data). Evitar queries N+1. Cache em relatórios de alta densidade.
4.4. Testes e Qualidade
● Framework:pytest com factory-boy.
● Cobertura: Mínimo de 80% nos apps críticos (selecao, interessados, academico).
● Documentação: Todo o código e comentários devem estar em Português Brasil.






---

