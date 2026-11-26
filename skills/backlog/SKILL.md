---
name: backlog
description: Mostra o backlog do projeto (`.agents/backlog.md`) formatado, com resumo por status. Use com "/backlog" ou quando o usuário perguntar o que falta fazer.
---

# /backlog

1. Leia `.agents/backlog.md`. Se não existir, sugira `/setup-projeto`.
2. Renderize as duas tabelas (Issues e BACKs). Aceite filtros opcionais: `/backlog <responsável|issue|status|sprint>`.
3. Mostre o resumo: contagem de BACKs por status (`To Do`, `In Progress`, `Done`) e por Issue.
4. Sugira a próxima task: o primeiro BACK `To Do` cujas dependências estão todas `Done`.
5. Somente leitura: não altere nenhum arquivo.
