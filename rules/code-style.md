# Estilo de Código (RASCUNHO — a definir)

> Pendente: o dono do plugin ainda vai decidir estas regras transversais. Enquanto estiver como rascunho, o agente segue o padrão existente do repositório (regra 8 do core) e o módulo do perfil ativo em `rules/stacks/`.

## Regras específicas por perfil
As diretrizes iniciais por área de atuação ficam em `rules/stacks/`:
- `dev-software.md` (`profile: dev`)
- `ia-automacao.md` (`profile: ia-automacao`)
- `analise-dados.md` (`profile: dados`)

## A decidir (transversal)
- [ ] Idioma de nomes (identificadores, commits, comentários): pt-BR ou en?
- [ ] Convenção de nomes (camelCase, snake_case) por linguagem
- [ ] Tamanho máximo de função/arquivo
- [ ] Política de comentários e docstrings
- [ ] Tratamento de erros e logging
- [ ] Cobertura mínima de testes
- [ ] Política de dependências
- [ ] Segurança (validação de entrada, autenticação, LGPD)

## Como adicionar uma stack extra
Copie `rules/stacks/_TEMPLATE.md` para `rules/stacks/<stack>.md` (ex.: `python.md`, `typescript-node.md`).
