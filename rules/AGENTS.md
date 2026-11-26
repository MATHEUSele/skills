# Regras Core — Dev Previsível

Estas regras valem para qualquer projeto, stack e agente. Sempre ativas.

## 1. Fonte da verdade
1. Se existir `.agents/`, leia `.agents/project.config.yml` e os documentos `.agents/01..05_*.md` ANTES de escrever código.
2. Na dúvida entre o que está documentado e o que você acha melhor, vale o documentado.
3. Se o documento não cobre o caso, ou há ambiguidade: **pergunte**. Não invente requisito, rota, tabela, campo ou dependência.

## 2. Escopo
4. Faça somente o que a task pedida descreve. Sem refatorações, renomeações ou "melhorias" fora do escopo.
5. Não adicione dependências novas sem declarar o motivo e sem aprovação do usuário.
6. Não apague nem sobrescreva arquivos que você não criou sem pedir confirmação.
7. Nunca coloque segredos, tokens ou senhas no código ou em commits. Use variáveis de ambiente e atualize `.env.example`.

## 3. Consistência de código
8. Siga o padrão já existente no repositório (nomes, estrutura de pastas, estilo). Em conflito, vale `.agents/01_system_architecture.md`.
9. Siga as regras do módulo da stack do projeto em `rules/stacks/<stack>.md`, se existir, e as de `rules/code-style.md`.
10. Toda mudança de comportamento vem com teste, quando o projeto tiver suíte de testes.
11. Antes de dizer que terminou, rode os comandos de `checks` do `project.config.yml` (lint, testes, build). Se falharem, corrija ou reporte. Nunca declare "pronto" com checks quebrados.

## 4. Git
12. A branch é da **Issue** (padrão `issue-<n>`), nunca da task (BACK).
13. Commit no formato do `project.config.yml` (padrão `<BACK-ID>: <descrição>`).
14. Nunca use `git add .` às cegas: revise `git status` e adicione apenas arquivos da task. Nunca use `--force` nem `--no-verify`.
15. Não faça push nem commit sem o usuário ter acionado `/end` (ou pedido explicitamente).

## 5. Comunicação
16. Ao terminar, apresente: o que mudou (lista de arquivos), o que foi verificado (checks) e o que ficou pendente ou assumido.
17. Declare todas as suposições feitas. Nunca esconda incerteza.
