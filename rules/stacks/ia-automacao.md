> Padrão inicial — ajuste conforme sua preferência.

# Stack: IA e Automação (`profile: ia-automacao`)

## Quando se aplica
Agentes de IA, fluxos com LLMs, pipelines de automação, bots, integrações por API/webhook e orquestradores.

## Estrutura de diretórios
```text
src/
  tools/        # ferramentas isoladas e testáveis chamadas pelo agente
  workflows/    # orquestração com estado explícito
prompts/        # prompts versionados em arquivos (.md/.txt), nunca inline no código
evals/          # casos de teste e métricas de avaliação de saídas de LLM
tests/          # testes unitários das tools e fluxos (com mocks do provedor LLM)
```

## Convenções
- **Prompts versionados:** todo prompt fica em `prompts/` com versão ou nome claro, carregado em tempo de execução — nunca strings longas soltas no código.
- **Tools isoladas:** cada tool tem contrato de entrada/saída tipado, validação de parâmetros e testes unitários independentes do LLM.
- **Workflows com estado explícito:** transições, passos e checkpoints ficam representados em estado estruturado, permitindo retomada e auditoria.
- **Confiabilidade em integrações:** toda chamada externa (LLM, APIs, webhooks) define timeout explícito, política de retentativas com backoff e chave/lógica de idempotência quando houver efeito colateral.
- **Logs estruturados:** registre modelo, latência, tokens/custo estimado e status da execução sem gravar dados sensíveis, PII ou segredos.
- **Config/ambiente:** chaves de API exclusivamente em variáveis de ambiente, documentadas em `.env.example`.

## Testes e Evals
- **Unitários/Integração (`tests/`):** testam tools, parsers de saída estruturada e máquina de estados usando mocks/fixtures determinísticos.
- **Evals (`evals/`):** conjunto reproduzível de entradas esperadas e critérios de aceite para validar mudanças de prompt ou modelo.

## Lint/Format/Build
- Configurar `checks.lint`, `checks.test` e `checks.build` em `.agents/project.config.yml` (incluindo checagem de tools e evals rápidos quando aplicável).

## Proibido
- Prompts gigantes hardcoded dentro de funções de negócio.
- Chamadas de rede/LLM sem timeout.
- Efeitos colaterais (envio de e-mail, cobrança, escrita em produção) sem idempotência e validação.
- Logar prompts/respostas contendo tokens, senhas ou dados pessoais não mascarados.
