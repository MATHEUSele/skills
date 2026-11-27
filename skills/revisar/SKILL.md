---
name: revisar
description: Auditoria independente e adversarial das mudanças atuais contra docs técnicos, regras, critérios de aceite e casos de borda, sem alterar código. Use com "/revisar" antes do /end para evitar viés de confirmação.
---

# /revisar [BACK-ID]

> **Princípio anti-viés:** A hipótese nula é **`PRECISA DE AJUSTES`**. Nunca confie em memória da conversa anterior nem no resumo entregue por `/executar`. Toda aprovação exige evidência direta (`arquivo:linha` ou saída real de comando executado nesta revisão).

## 1. Isolamento de contexto (obrigatório quando suportado)
- **Se o ambiente suportar subagentes isolados** (ex.: `invoke_subagent` no Antigravity ou ferramenta de subagente no Claude Code): delegue esta auditoria para um subagente revisor em contexto limpo (somente leitura + execução de comandos de verificação). Passe apenas:
  - o `BACK-ID` (ou instrução para usar a BACK `In Progress`);
  - os caminhos de `.agents/` e `AGENTS.md`;
  - a instrução de seguir este protocolo integralmente.
  **Nunca** envie o raciocínio, justificativas ou resumo de quem implementou o código.
- **Se o ambiente não suportar subagentes** (ex.: Cursor): execute localmente os passos 2 a 6, mas abra o relatório obrigatoriamente com:
  `> ⚠️ Revisão no mesmo contexto da implementação (menor independência). Para mudanças críticas, rode /revisar em uma conversa nova.`

## 2. Spec-first (checklist cego antes do diff)
Antes de abrir qualquer arquivo de código alterado:
1. Leia a BACK em `.agents/backlog.md` (sem argumento, use a BACK `In Progress`; se houver mais de uma, pergunte qual; se nenhuma, pare).
2. Leia `.agents/project.config.yml`, os 5 docs `.agents/01..05_*.md`, `AGENTS.md` e `.agents/stacks/*.md`.
3. Extraia em lista objetiva os requisitos da BACK, as regras aplicáveis e todos os **critérios de aceite** — antes de olhar a implementação.

## 3. Inspeção real do código e checks
1. Rode `git status` e `git diff` completo (incluindo arquivos untracked relacionados à task).
2. Leia os arquivos modificados ou criados **por inteiro ao redor das alterações** para detectar impactos colaterais não visíveis no diff isolado.
3. Reexecute de forma independente todos os comandos de `checks` (`lint`, `test`, `build`) definidos em `.agents/project.config.yml` e registre a saída real (sem confiar em execução anterior).

## 4. Falsificação (tentar quebrar)
Para cada critério de aceite e cada regra de negócio tocada pela task, formule explicitamente pelo menos **1 cenário que poderia quebrá-lo**:
- entrada nula, vazia, malformada ou tipo inesperado;
- limites numéricos (zero, negativo, overflow, precisão);
- erro de I/O, rede, timeout ou estado inválido;
- regressão em fluxos ou módulos vizinhos.
Verifique no código e nos testes se cada cenário foi realmente tratado e testado.

## 5. Auditoria de escopo, regras e testes
- **Escopo:** há mudanças fora do que a BACK pede? Refatorações ou renomeações não solicitadas? Dependências novas sem aprovação? Arquivos suspeitos (`.env`, segredos, dumps, dados reais)?
- **Docs e regras:** alguma decisão contradiz `.agents/01..05_*.md`, `AGENTS.md` ou `.agents/stacks/*`?
- **Anti-teste-teatro:** os testes verificam comportamento real e caminhos de falha, ou apenas mocks circulares e asserts triviais que continuariam passando mesmo se a lógica principal quebrasse?

## 6. Relatório estruturado e veredito
1. Informe o **Modo de revisão** (`Subagente isolado` ou `Mesmo contexto` + o aviso do passo 1).
2. Apresente a tabela de evidências:
   `| Critério de aceite | Evidência (arquivo:linha / saída de teste) | Caso de borda verificado | Status |`
3. Liste os achados por severidade: **Bloqueante**, **Importante**, **Sugestão** (cada item deve citar `arquivo:linha`, evidência observada e impacto concreto).
4. **Regra estrita de veredito:**
   - Qualquer achado **Bloqueante**, qualquer critério de aceite sem evidência objetiva ou qualquer comando de `checks` falhando ⇒ veredito obrigatoriamente **`PRECISA DE AJUSTES`**.
   - Só emita **`APROVADO`** quando 100% dos critérios tiverem evidência direta, todos os `checks` passarem nesta revisão e houver zero bloqueantes.
5. **Somente leitura:** nunca edite código nem corrija nada sem o usuário pedir.
