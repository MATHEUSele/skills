---
name: padronizar-projeto
description: Analisa um repositório e cria ou atualiza instruções AGENTS.md e skills reutilizáveis para padronizar o comportamento de agentes de IA. Use ao configurar um projeto para agentes, criar ou revisar instruções e skills, ou quando solicitado a padronizar um repositório.
---

# Padronizar projeto para agentes de IA

Inspecione o repositório antes de propor ou fazer alterações. Use as convenções, ferramentas e comandos que já existem; não invente requisitos nem substitua escolhas técnicas do projeto.

## Processo

1. Leia a documentação principal, os arquivos de configuração e as instruções existentes, como `AGENTS.md`, `CLAUDE.md` e arquivos de skills.
2. Identifique a linguagem, os comandos reais de teste, lint e build, a estrutura do projeto e as convenções demonstradas pelo código.
3. Crie ou atualize um `AGENTS.md` na raiz com orientações concisas e verificáveis para tarefas futuras. Inclua comandos somente quando confirmados nos arquivos do projeto.
4. Crie skills apenas para fluxos repetíveis que precisem de instruções detalhadas. Cada skill deve ficar em `skills/<nome>/SKILL.md`, ter frontmatter YAML com `name` e `description`, e explicar quando e como aplicar o fluxo.
5. Preserve conteúdo útil. Edite a seção pertinente em vez de apagar instruções existentes; não duplique o mesmo conteúdo em vários arquivos.
6. Valide os caminhos, a estrutura do frontmatter e as referências a comandos ou arquivos. Se houver alterações, execute as verificações pertinentes já disponíveis no projeto.
7. Resuma os arquivos criados ou atualizados, as verificações executadas e qualquer informação que não pôde ser confirmada.

## Limites

- Não crie instruções genéricas que contradigam o comportamento observado no repositório.
- Não adicione dependências, scripts, workflows ou ferramentas de validação sem necessidade e autorização.
- Não altere arquivos fora do escopo de padronização solicitado.
- Se faltarem informações para definir uma convenção, deixe a decisão explícita em vez de inventá-la.
