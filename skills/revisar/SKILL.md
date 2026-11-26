---
name: revisar
description: Revisa as mudanças atuais contra as regras do projeto, os docs técnicos e os critérios de aceite da BACK, sem alterar código. Use com "/revisar" antes do /end ou quando o usuário pedir revisão.
---

# /revisar [BACK-ID]

1. Sem argumento, use a BACK `In Progress`. Leia a BACK, os docs `.agents/` e as regras de `AGENTS.md`.
2. Analise `git diff` e verifique:
   - **Escopo:** há mudanças fora do que a BACK pede?
   - **Docs:** contradiz arquitetura, modelo de dados, regras de negócio ou contratos de API?
   - **Regras:** viola `AGENTS.md`, `.agents/stacks/*`? Dependência nova sem aprovação? Segredos?
   - **Testes:** mudança de comportamento sem teste? Os checks passam?
   - **Aceite:** cada critério está atendido?
3. Responda com uma lista por severidade (Bloqueante / Importante / Sugestão), com arquivo e linha, e um veredito: APROVADO ou PRECISA DE AJUSTES.
4. Somente leitura: não corrija nada sem o usuário pedir.
