> Padrão inicial — ajuste conforme sua preferência.

# Stack: Análise de Dados (`profile: dados`)

## Quando se aplica
Projetos de análise exploratória, pipelines ETL/ELT, engenharia de dados, relatórios reproduzíveis, métricas de negócio e modelagem analítica.

## Estrutura de diretórios
```text
data/
  raw/          # dados brutos IMUTÁVEIS (nunca editar manualmente; fora do git)
  processed/    # dados limpos/transformados reproduzíveis a partir de raw/
notebooks/      # apenas exploração visual e prototipagem; lógica reutilizável vai para src/
src/            # transformações, validações de schema e cálculo de métricas
reports/        # saídas finais reproduzíveis (tabelas, gráficos, relatórios)
tests/          # testes de transformações, schema e regras de métricas
```

## Convenções
- **Imutabilidade de `data/raw`:** dados brutos nunca são sobrescritos no lugar; toda limpeza gera saída em `data/processed/`.
- **Notebooks vs `src/`:** notebooks servem para explorar; funções de limpeza, agregação e cálculo de métricas devem ser extraídas para `src/` e testadas.
- **Reprodutibilidade:** fixe seeds aleatórias (`seed`), ordens de ordenação determinísticas e versões exatas de dependências (`requirements.txt` / `pyproject.toml` / lockfile).
- **Validação de schema e qualidade:** antes de transformar ou agregar, valide colunas obrigatórias, tipos, nulos inesperados, duplicatas e faixas de valores.
- **Dicionário de dados e métricas:** nenhuma métrica/KPI vai para relatório ou dashboard sem estar definida (fórmula, grão, filtros, fonte) em `.agents/02_data_model_and_persistence.md` e `.agents/03_business_rules_and_logic.md`.
- **Privacidade e git:** nunca versionar datasets reais, dumps ou dados sensíveis/PII no git — mantenha `data/raw/` e `data/processed/` no `.gitignore` (versione apenas amostras sintéticas mínimas para teste, se necessário).

## Testes
- **Qualidade de dados e lógica:** testes unitários em `tests/` com pequenos datasets sintéticos verificando schema, tratamento de nulos/duplicatas e fórmulas de métricas.
- **Reprodutibilidade:** rodar o pipeline do zero deve produzir exatamente a mesma saída em `data/processed/` e `reports/`.

## Lint/Format/Build
- Configurar `checks.lint`, `checks.test` e `checks.build` em `.agents/project.config.yml`.

## Proibido
- Modificar arquivos dentro de `data/raw/`.
- Manter lógica crítica de negócio presa apenas dentro de células de notebook sem testes.
- Commitar CSVs/Parquets reais de produção ou dados pessoais.
- Inventar ou alterar fórmula de métrica sem atualizar a documentação técnica.
