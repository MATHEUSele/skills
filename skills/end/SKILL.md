---
name: end
description: Encerra a task em andamento, com checks, commit padronizado, push na branch da Issue e atualização do backlog. Use com "/end" depois de /executar e da revisão do usuário.
---

# /end

1. Identifique a BACK `In Progress` em `.agents/backlog.md`. Se houver mais de uma, pergunte qual. Se nenhuma, pare.
2. Rode os `checks` do `project.config.yml`. Se falharem, **não commite**: reporte e pare.
3. Atualize `.agents/backlog.md`: BACK → `Done`; Issue → `Done` se todos os seus BACKs estiverem `Done`.
4. Rode `git status` e `git diff --stat`. Adicione ao stage apenas os arquivos da task e `.agents/backlog.md`, com `git add <arquivos>`. Se houver arquivos suspeitos (`.env`, chaves, binários grandes, `data/raw/`), pare e avise.
5. Commit com `git.commit_format` (padrão `BACK-001: <descrição curta>`).
6. **Registre a sessão** no topo de `.agents/sessions.md`, usando o modelo do arquivo: BACKs trabalhadas, resumo, decisões, pendências, arquivos-chave e o hash curto do `HEAD` (`git rev-parse --short HEAD`). Faça `git add .agents/sessions.md` e commit `chore: sessão`. Assim o `/init` da próxima sessão sabe o ponto de retomada.
7. `git push <remote> <branch_da_issue>`. Nunca use `--force`.
8. Informe o encerramento e sugira a próxima task executável (dependências `Done`), no formato `/executar BACK-XXX`.
