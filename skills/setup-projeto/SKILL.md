---
name: setup-projeto
description: Prepara um projeto para geração de código previsível. Cria `.agents/` com project.config.yml, 5 documentos técnicos, backlog e adaptadores para Claude Code, Cursor e Antigravity. Use quando o usuário pedir setup, inicializar o projeto ou "/setup-projeto".
---

# /setup-projeto

Os templates ficam no plugin, em `../../templates/` relativo a este arquivo. As regras core ficam em `../../rules/AGENTS.md` e os módulos de perfil/stack em `../../rules/stacks/`. Copie os arquivos fixos, sem reescrevê-los.

## Passos
1. **Coleta.** Se o usuário não forneceu escopo/requisitos, peça:
   - objetivo do sistema;
   - `profile` principal (`dev`, `ia-automacao` ou `dados`) e eventuais stacks extras;
   - equipe (nomes e papéis);
   - comandos de `lint`, `test` e `build`.
   Não invente. Se `.agents/` já existe, avise e pergunte antes de sobrescrever qualquer coisa.
2. **Config e stacks.** Copie `templates/project.config.yml` para `.agents/project.config.yml` e preencha com as respostas. Copie o módulo do perfil para `.agents/stacks/` usando o mapeamento:
   - `dev` → `rules/stacks/dev-software.md`
   - `ia-automacao` → `rules/stacks/ia-automacao.md`
   - `dados` → `rules/stacks/analise-dados.md`
   Para cada item extra em `project.stack`, confira se existe `rules/stacks/<stack>.md` no plugin e copie para `.agents/stacks/`; se não existir, avise o usuário.
3. **Docs técnicos.** Gere os 5 arquivos de `.agents/01..05_*.md` seguindo EXATAMENTE as seções base e as seções extras do `profile` definidas em `templates/docs-outline.md`. Conteúdo vem apenas do escopo do usuário. Falta de informação: `N/A — <motivo>` ou uma pergunta, nunca invenção.
4. **Backlog.** Copie `templates/backlog.md` para `.agents/backlog.md` e preencha:
   - Issues funcionais, cada uma com UM responsável da equipe de `project.config.yml`, distribuídas de forma equilibrada.
   - BACKs com IDs sequenciais (`BACK-001`...), status `To Do` e **critérios de aceite** verificáveis.
   - Dependência apenas para BACKs da mesma Issue ou de Issues anteriores. Nunca para Issue futura.
5. **Sessões.** Copie `templates/sessions.md` para `.agents/sessions.md`.
6. **Adaptadores e higiene.** Copie `rules/AGENTS.md` para a raiz do projeto como `AGENTS.md` (Antigravity/Cursor/Codex). Copie `templates/adapters/CLAUDE.md` para `CLAUDE.md` e `templates/adapters/cursor-core.mdc` para `.cursor/rules/core.mdc`. Se já existirem, faça merge preservando o conteúdo do usuário. Garanta no `.gitignore` entradas básicas da stack (ex.: `.env`, `__pycache__/`, e para `dados` também `data/raw/` e `data/processed/`).
7. **Validação** (obrigatória antes de entregar): confira que não há dependência para Issue futura, que cada Issue tem um único responsável, que os módulos de stack do perfil foram copiados para `.agents/stacks/` e que todos os 5 docs têm todas as seções base e extras do perfil.
8. **Entrega.** Mostre o backlog e sugira a primeira task: `/executar BACK-001` (ou a primeira sem dependência).
