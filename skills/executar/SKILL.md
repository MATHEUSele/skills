---
name: executar
description: Executa uma task do backlog (ex. "/executar BACK-001") seguindo os docs técnicos e as regras do projeto, na branch da Issue. Use quando o usuário pedir para implementar, executar ou desenvolver uma BACK.
---

# /executar <BACK-ID>

## Antes de codar
1. Leia `.agents/project.config.yml`, os 5 docs `.agents/01..05_*.md`, `.agents/backlog.md`, a última entrada de `.agents/sessions.md` e as regras de `AGENTS.md` (mais `.agents/stacks/*.md`, se houver).
2. Localize a BACK e a Issue. Verifique que todas as dependências estão `Done`. Se não, pare e informe.
3. Confira o responsável (`one_owner_per_issue`). Se o usuário não for o responsável da Issue, avise e peça confirmação.
4. Confira `git status`. Se a árvore estiver suja com mudanças alheias à task, avise antes de seguir.
5. Crie ou mude para a branch da Issue conforme `git.branch_pattern` (ex.: `issue-1`). **NUNCA crie branch com nome de BACK.**
6. Marque a BACK como `In Progress` no `backlog.md`.

## Implementação
7. Implemente somente o descrito na BACK, conforme os docs. Ambiguidade ou lacuna: pergunte, sem improvisar.
8. Escreva ou atualize testes conforme a regra 10 do core.
9. Rode os `checks` do config (lint, test, build). Corrija até passarem, ou reporte o bloqueio com a causa.

## Entrega
10. Apresente: arquivos criados/alterados, cada critério de aceite marcado como atendido ou não (com evidência), checks executados e suposições feitas.
11. **Pare e aguarde** revisão ou `/end`. Não faça commit nem push.
