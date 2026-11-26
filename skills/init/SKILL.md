---
name: init
description: Retoma o trabalho no início de uma sessão. Lê o histórico de sessões (`.agents/sessions.md`), as mudanças do git desde a última sessão e o backlog, e apresenta um briefing com o estado atual e a próxima ação. Use com "/init" ao começar uma conversa nova.
---

# /init

Somente leitura (exceto o aviso do passo 6).

1. Leia `.agents/sessions.md`. Se não existir, diga que é a primeira sessão e sugira `/setup-projeto` (ou crie o arquivo a partir de `templates/sessions.md` do plugin).
2. Pegue a entrada mais recente. Ela registra o `HEAD` (hash do commit) no fim da sessão. Se vier vazio, use a data da entrada.
3. Levante o que mudou desde então (se houver remote configurado, considere avisar caso haja commits não baixados):
   - `git log --oneline <hash>..HEAD` (ou `--since=<data>`), ignorando o próprio commit `chore: sessão` da entrada lida;
   - `git diff --stat <hash>..HEAD`;
   - `git status` para mudanças não commitadas;
   - `git diff <hash>..HEAD -- .agents/0*.md` para destacar alterações em documentação técnica/requisitos.
   Se o hash não existir mais (rebase), avise e use a data.
4. Leia `.agents/backlog.md` e identifique BACKs `In Progress` e a próxima BACK executável.
5. Apresente o briefing, curto:
   - **Última sessão:** resumo, decisões e pendências registradas;
   - **Desde então:** commits e mudanças de docs, inclusive feitas por outras pessoas;
   - **Estado do backlog:** contagem por status e o que está em andamento;
   - **Próxima ação sugerida:** `/executar BACK-XXX` ou a retomada da BACK em andamento.
6. Se houver divergência entre `sessions.md`, git e backlog (ex.: BACK `In Progress` sem branch ou commits), aponte e pergunte como proceder. Não corrija sozinho.
7. Releia as regras de `AGENTS.md` e os docs `.agents/` que o briefing indicar como alterados.
