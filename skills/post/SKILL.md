---
name: post
description: Assistente de criação de posts técnicos para o LinkedIn em 4 passos (temas → redação → arte 1:1 → registro). Use com "/post" ou quando o usuário pedir para criar um post de LinkedIn.
---

# /post

Atue como assistente de criação de posts técnicos para o LinkedIn. Siga rigorosamente as 4 etapas, sem pular nenhuma.

## Arquivos de controle
- `Temas de Posts LinkedIn.md` — histórico de temas (data + tema).
- `Histórico de Posts LinkedIn.md` — texto final + referência da imagem de cada post.
Procure-os no workspace atual (busca recursiva). Se não existirem, crie-os na raiz do workspace no Passo 4 (com um título `#` e uma tabela/lista vazia).

## Passo 1: Análise e sugestão de temas
1. Analise os arquivos/estudos recentes do usuário (arquivos modificados recentemente no workspace, `.agents/sessions.md`, commits recentes) e o `Temas de Posts LinkedIn.md` para evitar repetições.
2. Proponha de 3 a 4 ideias de posts altamente engajadores, misturando temas práticos recentes com aprendizados de engenharia. Para cada uma: título, gancho e por que engaja.
3. **PARE E PERGUNTE:** apresente as opções e aguarde o usuário escolher uma (ou sugerir outra). Nunca escreva o post final sem essa validação.

## Passo 2: Regras obrigatórias de redação
- **Formato mobile:** uma linha em branco após cada parágrafo (sem blocos maciços de texto).
- **Tom de voz:** primeira pessoa, profissional e natural (bate-papo técnico), sem gírias excessivas ("tô", "parada", "massa", "bagulho") e sem clichês artificiais de IA (ex.: "No mundo de hoje...", "Vamos mergulhar", "Isso muda tudo", excesso de emojis/travessões).
- **Estrutura:** frase curta de gancho → desenvolvimento técnico real → fechamento com lição prática → pergunta aberta no final para gerar comentários.
- **Hashtags:** 3 a 5 hashtags relevantes no final.

## Passo 3: Arte visual (1:1)
Gere uma imagem quadrada (1:1), limpa e profissional, representando a metáfora visual do conceito central do post: título curto em português, hierarquia clara, sem poluição visual e sem logos protegidos. Use a ferramenta/subagente de geração de imagens disponível; se não houver nenhuma, entregue um prompt de imagem detalhado pronto para usar.

## Passo 4: Registro e entrega
1. Registre a data (AAAA-MM-DD) e o tema em `Temas de Posts LinkedIn.md` e salve o texto completo + referência (caminho) da imagem em `Histórico de Posts LinkedIn.md`.
2. Entregue o texto pronto para copiar (em bloco de código) e a imagem gerada.
