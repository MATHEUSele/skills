# Esqueleto dos 5 documentos técnicos (gerados em `.agents/` pelo /setup-projeto)

Cada documento DEVE ter exatamente as seções base abaixo, na ordem. Quando o `profile` do projeto exigir seções extras, inclua-as logo após as seções base do respectivo documento. Seção sem conteúdo: escreva `N/A — <motivo>`. Nunca omita seções.

## 01_system_architecture.md
1. Visão geral e componentes · 2. Stack e versões · 3. Estrutura de diretórios · 4. Padrões de projeto · 5. Ciclo de vida da requisição · 6. Autenticação/autorização · 7. Segurança e privacidade · 8. Diretrizes de UX/UI

### Seções extras por perfil
- `ia-automacao`: 9. Arquitetura do agente, memória/estado e fluxo de orquestração
- `dados`: 9. Fluxo ponta a ponta dos dados (fontes → processamento → consumo)

## 02_data_model_and_persistence.md
1. Entidades e relacionamentos · 2. DDL/schemas (tipos, PK, FK, restrições, índices) · 3. Estratégia de migrations · 4. Camada analítica (se aplicável)

### Seções extras por perfil
- `dados`: 5. Fontes de dados (origem, formato, frequência, SLA) · 6. Dicionário de dados (campo, tipo, significado, regras de nulidade)
- `ia-automacao`: 5. Persistência de estado, histórico de conversas/execuções e artefatos de eval

## 03_business_rules_and_logic.md
1. Casos de uso e fluxos · 2. Validações e restrições · 3. Fórmulas, algoritmos e máquinas de estado · 4. Exceções e mensagens de erro de negócio

### Seções extras por perfil
- `dados`: 5. Definições de métricas e KPIs (nome, fórmula exata, grão, filtros, fonte) · 6. Regras de qualidade e saneamento de dados
- `ia-automacao`: 5. Comportamento do agente, política de prompts e guardrails · 6. Critérios de avaliação (evals) e limiares de aprovação

## 04_api_and_integration_specs.md
1. Convenções de rotas · 2. Contratos (request/response/status) · 3. Paginação e filtros · 4. Workers/ingestão · 5. Integrações, webhooks, filas e retentativas

### Seções extras por perfil
- `dados`: 6. Pipelines ETL/ELT, agendamento e idempotência de carga
- `ia-automacao`: 6. Catálogo de tools, APIs de LLM, limites de custo/rate limit e fallbacks

## 05_devops_ci_cd_deployment.md
1. Docker/compose · 2. Variáveis de ambiente (`.env.example`) · 3. CI/CD (testes, lint, build, deploy) · 4. Ambientes

### Seções extras por perfil
- `ia-automacao`: 5. Orquestração, agendadores, monitoramento de custos e alertas de falha
- `dados`: 5. Agendamento de pipelines, reprodutibilidade de ambiente e retenção de dados
