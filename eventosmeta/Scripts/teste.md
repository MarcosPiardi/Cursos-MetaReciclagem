SEÇÃO 5: FLUXO DE CLASSIFICAÇÃO E MATRÍCULA EM LOTE

### 5.1 Descrição Geral de Classificação

**Parágrafo 1:** A classificação é o núcleo da seleção. Após o encerramento das inscrições, o ClassificadorService processa todas as inscrições "Pendente" de um evento aplicando critérios previamente configurados pelo administrador.

**Parágrafo 2:** Cada critério é binário (0 ou 1): candidato atende ou não atende. Quando atende, recebe pontos fixos configuráveis (ex: PCD = 5 pontos, NIS = 3 pontos). Score total é a soma acumulada. Inscrições com mesmo score entram em desempate automático.

### 5.2 Regras de Pontuação e Desempate

**Parágrafo 1:** Critérios Automáticos Verificáveis:
- PCD (Pessoa com Deficiência): validação automática via formulário
- NIS (Número de Inscrição Social): validação contra base municipal
- Programa Social: indicador booleano no cadastro
- Faixa Etária (JOVEM, IDOSO): calculada a partir da data de nascimento
- Cota Racial (COTA_RACIAL): seleção categórica (Parda, Preta, Indígena, etc)
- Escolaridade (ESCOLARIDADE): nível informado na inscrição

**Parágrafo 2:** Lógica de Desempate (quando dois candidatos têm score idêntico):
- Se evento tem critério JOVEM ativo: ordena por idade ASC (mais jovem vence)
- Se evento tem critério IDOSO ativo: ordena por idade DESC (mais velho vence)
- Se nenhum critério de idade: ordena por data_inscricao ASC (quem se inscreveu primeiro vence, com precisão de milissegundos)

**Parágrafo 3:** Resultado da Classificação:
- Score DESC (maior para menor)
- Dentro do mesmo score: aplicar desempate conforme regra acima
- Atribuir posição ordinal (1º, 2º, 3º, etc)
- Candidatos dentro das vagas: status "Classificado"
- Candidatos excedentes: status "Lista de Espera" com posição na fila
- Candidatos que não atendem mínimo de critérios: status "Não Localizado"

### 5.3 Fluxo de Matrícula em Lote

**Parágrafo 1:** Após publicação do resultado, o Staff executa a ação "Matrícula em Lote" selecionando um grupo de inscrições classificadas. O sistema realiza validações críticas antes de confirmar:
- Capacidade: número de matrículas ≤ vagas disponíveis
- Duplicatas: mesmo candidato não matricula 2x no mesmo evento
- Atomicidade: ou todas as matrículas são confirmadas ou nenhuma (transação completa ou falha total)

**Parágrafo 2:** Processamento por Linha:
- Cada inscrição selecionada é processada individualmente
- Se erro em uma linha (ex: candidato já matriculado): registro salva erro, continua processando demais
- Erros são logados para revisão posterior
- Notificação automática é enviada a cada candidato matriculado

**Parágrafo 3:** Pós-Confirmação:
- Status da inscrição muda para "Confirmado"
- Matrícula recebe status "Ativa"
- Se houver vagas restantes e há candidatos em "Lista de Espera": primeira fila é promovida automaticamente para "Aguardando Confirmação"
- Relatórios Staff e Mural são gerados (PDF/Excel)

### 5.4 Quotas e Inclusão Social

**Parágrafo 1:** O sistema implementa políticas de inclusão via quotas obrigatórias:
- 30% das vagas: reservadas para PCD (Pessoa com Deficiência)
- 40% das vagas: reservadas para Programa Social (beneficiários de programas municipais)
- Remanescente: ampla concorrência
- Cotas Raciais (se aplicável): definidas por regulamento municipal específico

**Parágrafo 2:** Validação de Preenchimento:
- Se cota PCD não preenche 30%, vagas remanescentes liberam para Programa Social
- Se Programa Social não preenche 40%, vagas remanescentes liberam para ampla concorrência
- Ordem de chamada: primeiro preenche todas as cotas, depois passa para próxima categoria

### 5.5 Relatórios Integrados

**Parágrafo 1:** Após classificação e matrícula, dois tipos de relatório são gerados:
- Relatório Staff (Confidencial): com CPF completo, email, telefone, programa social, status completo
- Relatório Mural (Público): com CPF mascarado (XXX.XXX.XXX-YY), sem contatos, apenas status básico, com aviso de publicação

**Parágrafo 2:** Ambos gerados em PDF e Excel, permitindo publicação em murais físicos (PDF impresso) ou planilhas compartilhadas (Excel com filtros).