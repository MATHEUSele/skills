> Padrão inicial — ajuste conforme sua preferência.

# Stack: Dev de Software (`profile: dev`)

## Quando se aplica
Aplicações web, APIs, CLIs, bibliotecas e serviços backend/frontend em geral.

## Estrutura de diretórios
```text
src/            # código de produção separado por domínio/camada
tests/          # espelha a estrutura de src/ (unit/ e integration/)
migrations/     # alterações de schema versionadas
```

## Convenções
- **Separação de camadas:** transporte/interface (rotas, CLI) não contém regra de negócio; regra de negócio fica isolada de acesso a banco/HTTP externo.
- **Validação na borda:** valide e tipifique entradas na entrada da aplicação (DTOs/schemas) antes de passar para o domínio.
- **Erros tipados:** use exceções/erros específicos de domínio com mensagens claras; nunca engula exceção silenciosamente (`except: pass` / `catch {}`).
- **Config/ambiente:** configurações vêm de variáveis de ambiente validadas na inicialização; nunca hardcoded.
- **Migrations versionadas:** toda mudança de banco passa por migration reversível e registrada, nunca alteração manual em produção.

## Testes
- **Unitários:** cobrem regras de negócio e casos de borda sem depender de rede ou banco real.
- **Integração:** cobrem contratos de API, persistência e fluxos críticos.
- **Regra prática:** toda correção de bug ganha um teste de regressão que falhava antes da correção.

## Lint/Format/Build
- Configurar `checks.lint`, `checks.test` e `checks.build` em `.agents/project.config.yml` e mantê-los verdes antes de qualquer `/end`.

## Proibido
- Misturar SQL/chamadas externas direto em handlers/controllers.
- Alterar schema em produção sem migration.
- Subir segredos, tokens ou arquivos `.env` para o git.
