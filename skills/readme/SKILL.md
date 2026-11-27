---
name: readme
description: Gera ou atualiza o README.md estilizado e as imagens SVG (assets/banner.svg, assets/logo.svg, assets/demo.svg) no padrão visual do plugin, baseado nos arquivos reais do projeto. Use com "/readme" ou quando o usuário pedir para gerar/estilizar o README e assets visuais.
---

# /readme

Gera documentação visual padronizada (README.md + SVGs animados sem JavaScript) fiel ao estado real do repositório.

Os modelos ficam no plugin em `../../templates/readme/` relativo a este arquivo:
- `templates/readme/README.template.md`
- `templates/readme/banner.template.svg`
- `templates/readme/logo.template.svg`
- `templates/readme/demo.template.svg`

## Passos

1. **Inspeção real (proibido inventar).** Leia o que existir no projeto antes de escrever uma linha:
   - `.agents/project.config.yml` e `.agents/01..05_*.md` (para objetivo, `profile`, stack, comandos de `checks` e arquitetura);
   - manifestos do projeto (`package.json`, `pyproject.toml`, `plugin.json`, `Cargo.toml`, etc.) para nome, versão e dependências reais;
   - `.github/workflows/*.yml`, `LICENSE` e a árvore real de pastas e scripts/comandos do repositório.
   Tudo no `README.md` e nos SVGs deve refletir apenas o que existe no projeto.

2. **Confirmação de escopo e estilo.** Se `README.md` ou `assets/*.svg` já existirem, avise o usuário e pergunte antes de sobrescrever:
   - se quer atualizar tudo, só o `README.md` ou só os SVGs;
   - se mantém a paleta padrão (roxo → azul) e ícone base ou prefere outra paleta/ícone.

3. **Gerar os SVGs em `assets/`.** Use `templates/readme/banner.template.svg`, `templates/readme/logo.template.svg` e `templates/readme/demo.template.svg` como base para gerar `assets/banner.svg`, `assets/logo.svg` e `assets/demo.svg`, seguindo estas regras obrigatórias:
   - use apenas fontes de sistema (`sans-serif` e `monospace`), nunca fontes externas;
   - **zero `<script>`**: animações de `demo.svg` usam somente CSS `@keyframes` para renderizar dentro de `<img>` no GitHub;
   - XML bem-formado (escape `&` como `&amp;`, além de `<` e `>` em textos);
   - ajuste larguras das pills no `banner.svg` para o texto não vazar;
   - em `demo.svg`, mostre comandos e saídas reais do projeto (CLI, API, pipeline de dados ou comandos de agente);
   - se existir `plugin.json` na raiz sem `"logo"`, pergunte se deseja adicionar `"logo": "assets/logo.svg"`.

4. **Gerar `README.md`.** Siga a estrutura e hierarquia visual de `templates/readme/README.template.md`, adaptando as seções ao `profile` (`dev`, `ia-automacao`, `dados` ou genérico):
   - só inclua badge de licença se existir `LICENSE` e badge de CI se existir `.github/workflows/*.yml`;
   - em diagramas Mermaid, coloque aspas em todo label com caracteres especiais (`/`, `(`, `)`, `:`, `-`, etc.);
   - gere a árvore de pastas a partir da estrutura real do repositório (sem pastas fictícias).

5. **Validação antes de entregar:**
   - confira que nenhum placeholder `{{...}}` sobrou em `README.md` ou em `assets/*.svg`;
   - valide que os 3 SVGs são XML bem-formados e não contêm `<script>`;
   - confira que todas as imagens (`assets/*.svg`) e links relativos citados no `README.md` existem no repositório;
   - apresente a lista de arquivos criados/atualizados e **pare sem fazer commit nem push**.
