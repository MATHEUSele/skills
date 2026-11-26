---
name: conselho
description: Protocolo LLM Council em 4 etapas (enquadramento, 5 conselheiros independentes, revisão anônima entre pares, veredito do presidente). Use com "/conselho" ou quando o usuário pedir para validar/debater uma decisão com riscos reais.
---

# /conselho <pergunta ou decisão>

Execute o protocolo **LLM Council** em 4 etapas obrigatórias. Não pule etapas e não antecipe sua opinião antes da Etapa 4.

## Etapa 1: Enquadramento (contexto)
Enquadre a pergunta de forma neutra, incluindo contexto relevante (perfil do usuário, restrições, o que está em jogo e histórico do projeto — use `.agents/`, `sessions.md` e a conversa se existirem), sem dar opinião ainda. Se faltar informação crítica, pergunte antes de seguir.

## Etapa 2: Os 5 conselheiros independentes (em paralelo)
Analise a questão sob 5 lentes independentes (150–300 palavras cada, sem ficar em cima do muro — cada um defende seu ângulo com força total). Se a ferramenta suportar subagentes, rode os 5 em paralelo, cada um recebendo apenas o enquadramento da Etapa 1; caso contrário, escreva cada parecer sem referenciar os outros.
1. **The Contrarian (Advogado do Diabo):** busca falhas fatais, riscos escondidos, pontos fracos e o que pode dar errado ou soar falso.
2. **The First Principles Thinker (Primeiros Princípios):** questiona as premissas básicas e pergunta se estamos resolvendo o problema certo desde a raiz.
3. **The Expansionist (Expansionista):** procura o maior potencial de alta (upside), oportunidades ocultas e como multiplicar o impacto.
4. **The Outsider (Olhar de Fora):** lê sem contexto prévio, com olhos frescos, expondo jargões, clichês e a "maldição do conhecimento".
5. **The Executor (Executor):** foca 100% em execução prática imediata: o que funciona agora e qual o caminho mais rápido para fazer acontecer.

## Etapa 3: Revisão anônima entre pares
Anonimize os 5 pareceres como Respostas A, B, C, D e E (em ordem embaralhada, sem revelar o mapeamento até o fim) e faça revisões cruzadas respondendo objetivamente:
1. Qual resposta é a mais forte e por quê?
2. Qual resposta tem o maior ponto cego e o que faltou nela?
3. O que TODAS as 5 respostas deixaram passar?

## Etapa 4: Veredito do Presidente (entrega final)
Sintetize de forma direta, escaneável e sem rodeios, exatamente nesta estrutura:
- **Onde o Conselho Concorda** (sinais de alta confiança)
- **Onde o Conselho Diverge** (conflitos reais, sem suavizar)
- **Pontos Cegos Capturados** (o que só surgiu na revisão entre pares)
- **A Recomendação** (decisão clara e direta — proibido responder "depende")
- **A Única Coisa que Você Deve Fazer Primeiro** (1 único próximo passo concreto)
