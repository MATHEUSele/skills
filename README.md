# Skills para padronizar projetos

Este repositório fornece a skill `padronizar-projeto`, no formato aberto [Agent Skills](https://agentskills.io/). Ela orienta uma LLM compatível a analisar um projeto e criar ou atualizar instruções e skills para que o comportamento dos agentes fique consistente, sem repetir manualmente as mesmas orientações em cada tarefa.

## Instalação

Adicione a pasta `skills/padronizar-projeto` ao diretório de skills reconhecido pelo seu agente de programação. Por exemplo:

- Claude Code: `.claude/skills/padronizar-projeto/`
- GitHub Copilot: `.github/skills/padronizar-projeto/`
- Codex: `.agents/skills/padronizar-projeto/`

Mantenha o arquivo `SKILL.md` dentro dessa pasta. O agente compatível lê o nome e a descrição da skill e pode carregá-la automaticamente quando a tarefa corresponder. Para iniciar a padronização explicitamente, peça: **“Padronize as instruções e skills deste projeto.”**

## O que a skill faz

Quando ativada, ela inspeciona a estrutura e as convenções existentes e então:

1. cria ou atualiza `AGENTS.md` com orientações gerais específicas do projeto;
2. identifica fluxos de trabalho repetíveis que se beneficiariam de skills próprias;
3. cria skills seguindo o formato Agent Skills, sem duplicar instruções já existentes;
4. preserva configurações e instruções existentes que não conflitem com o objetivo;
5. informa quais arquivos alterou e o que ainda precisa de decisão humana.

A skill não executa código nem instala arquivos sozinha: a ferramenta de LLM precisa suportar Agent Skills e ter acesso de leitura e escrita ao projeto. Cada host pode ter requisitos adicionais de instalação ou configuração.
