# Verificação parte 1 (início até o fim do IA NA PRÁTICA) - edição 23/10/2026

Fontes abertas por WebFetch ou curl (Ars Technica bloqueou o WebFetch; lido via curl).

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Charlie Precourt, ex-astronauta e membro do painel de segurança da NASA | Ars Technica (Starship 22) | confirmada | "ex-astronauta da NASA e membro do Aerospace Safety Advisory Panel" |
| 2 | Última estimativa "cerca de 22 voos" para Artemis IV | Ars | confirmada ("I think the last estimate is around 22 flights") | Dizer que é fala de Precourt ("acho que a última estimativa") |
| 3 | "contra cerca de uma dúzia na conta da NASA de 2023" | Ars | parcialmente confirmada | A NASA nunca deu número: em 2023 Lisa Watson-Morgan disse "high single digits to the low double digits"; a "dúzia" é inferência do Ars. Reescrever: "contra algo como uma dúzia, pelo que a NASA deixou entender em 2023" |
| 4 | Musk diz "6 a 8" | Ars | confirmada ("Actual number will be more like 6 to 8"; disse que 22 é "way too high") | ok |
| 5 | Pesquisa publicada na quinta (22), Frontier Red Team da Anthropic com a Theorem | Anthropic | confirmada (Oct 22, 2026; 22/10 é quinta) | ok |
| 6 | 239 pontos de entrada, 123 bibliotecas | Anthropic | confirmada ("239 entry points across 123 different OSS-Fuzz libraries") | Acrescentar "do OSS-Fuzz" (são bibliotecas do OSS-Fuzz) |
| 7 | "sem falha para entradas de até 64 MB" | Anthropic | quase | Fonte: "less than 64 MB" (menos de 64 MB). Propriedade provada: sem crash, erro de memória ou falha de assertiva, sob premissas. Trocar "até 64 MB" por "menos de 64 MB" |
| 8 | "algumas semanas" (entre aspas) | Anthropic | confirmada (tradução de "a few weeks") | Tirar as aspas ou assumir como tradução |
| 9 | Rocq (antigo Coq) | Anthropic | não confirmada para "antigo Coq" | A página só diz Rocq e nunca menciona Coq. Cortar "(antigo Coq)" ou citar outra fonte |
| 10 | seL4: 2 pessoas-ano para escrever, 20 para verificar, "10 vezes" | Anthropic | confirmada (20 e 2); "10 vezes" é conta nossa | Ok com "(dado citado pela Anthropic)"; melhor "20 vs 2, ou 10 vezes mais" |
| 11 | ~180 milhões de linhas de prova, 600 mil numa prova típica | Anthropic | confirmada ("about 180 million lines of Rocq", "typical proof ... about 600,000 lines") | ok |
| 12 | "centenas" de bugs; provas podem gastar "centenas de milhões" de tokens | Anthropic | confirmada | ok |
| 13 | PHP2Shell: falhas escondidas por mais de uma década, achadas com IA da OpenAI e do Google; Amazon viu tentativa 4 dias antes do aviso público | Ars Technica (FT), 22/10 | confirmada | ok. Observação: o texto do Ars é do Financial Times; a Amazon falou na quarta (21) |
| 14 | Jason Gross, coautor do estudo | Anthropic (lista de autores) e HN | confirmada (Gross está na lista de autores; usuário jasongross no HN) | ok |
| 15 | Gross diz no HN que em software o gargalo "é só escala" | HN 50202217 | confirmada com ressalva | Original: "In software verification... the bottleneck is just scale" (em verificação de software, contrastando com matemática). Trocar "em software" por "em verificação de software" |
| 16 | "Formal verification against what?" no HN | HN | confirmada (usuário pinevale) | ok |
| 17 | Anthropic avisa que "formalmente verificado" não é "sem bug"; erro pode estar na especificação | Anthropic | confirmada ("'Formally verified' does not mean 'bug-free'") | ok |
| 18 | "Só vale para binários RISC-V estáticos e de uma thread, e a maioria roda em x86 ou ARM" | Anthropic | ERRADA/incompleta | A página diz que as provas principais assumem binário estático, single-thread, orçamento de memória fixo, CPU RISC-V e Linux, mas também relata uma prova direta de binário x86 (com semântica x86 gerada pelo Claude) em exemplo adicional e que ampliar o escopo "está ao alcance". "A maioria roda em x86 ou ARM" não está na fonte. Reescrever: "as provas principais assumem binário RISC-V estático, de uma thread e memória fixa; houve um caso em x86; a Anthropic diz que ampliar está ao alcance". Cortar "a maioria roda em x86 ou ARM" ou fontear |
| 19 | Skill = pasta com SKILL.md (nome, quando usar, instruções) e scripts; agente carrega só nome e descrição, ~100 tokens | agentskills.io/specification | confirmada ("Metadata (~100 tokens)") | ok |
| 20 | Anthropic doou o Agent Skills à Agentic AI Foundation em 22/10; AAIF sob a Linux Foundation, que já guarda o MCP | Anthropic (news) | confirmada | ok |
| 21 | Mais de 70 plataformas, como ChatGPT, Cursor, GitHub Copilot | Anthropic (news) | confirmada | ok |
| 22 | 1 milhão de skills publicadas, "quase 280 milhões" de instalações | Anthropic (news) | confirmada ("nearly 280 million installed") | ok |
| 23 | Rakuten: processo de contabilidade de um dia para cerca de uma hora | claude.com/blog/skills | confirmada | A frase é de Yusuke Kaji, GM de IA da Rakuten: "What once took a day, we can now accomplish in an hour" (contabilidade gerencial e finanças). Dá para dizer "um dia para uma hora" sem "cerca de" |
| 24 | Zack Shapiro, advogado de escritório pequeno nos EUA, skills para revisar contratos e padronizar citações | Artificial Lawyer | confirmada | ok |
| 25 | "a Anthropic manda instalar só de fonte confiável" | link no texto é o da AAIF; docs da Anthropic | confirmada na fonte errada | A página da AAIF não diz isso. A documentação (platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) diz "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic". Citar esse link |
| 26 | Snyk: 3.984 skills de dois marketplaces; 534 (~13 em 100) com problema crítico; 76 maliciosas | Snyk | confirmada com ressalva | 3.984, 534 (13,4%) e 76 conferem. A página é inconsistente sobre "dois marketplaces" (ClawHub e skills.sh, em 5/2/2026, mas a seção de achados cita só ClawHub). Dizer "marketplaces como o ClawHub" ou "da ClawHub e skills.sh, segundo a Snyk" |
| 27 | Guia de segurança do padrão ainda é só proposta | Anthropic (news) | confirmada ("We've proposed starting with a roadmap ... security guidance") | ok |

## Opinião / previsão sem selo (manual 14.6)

- Linha ⚖️: "'verificado formalmente' tende a virar argumento de qualidade e de responsabilidade" é previsão sem fonte nem "a aposta é". Selar com **Opinião:** ou cortar.
- "quem vende sites e apps ... vai ouvir do cliente, cada vez mais, 'como você sabe que funciona?'" é previsão sem selo. Selar ou suavizar.
- "O cliente pagaria agora porque o mesmo pacote passa a rodar em várias ferramentas" está antes do selo e é opinião. Mover para dentro do **Opinião:**.
- "Achar um erro é uma coisa; garantir que não existe nenhum é outra, bem mais cara": leve, sustentada pelo seL4. Aceitável.
- "Hoje é pesquisa, não ferramenta de prateleira": a Theorem oferece rodar o pipeline para outros projetos open source; ajustar para "ainda é pesquisa; a Theorem oferece rodar o processo em outros projetos abertos".

## Correções obrigatórias

1. Item 18: reescrever a limitação RISC-V/x86. A Anthropic relata prova em binário x86, e "a maioria roda em x86 ou ARM" não está na fonte.
2. Item 25: trocar o link do "instalar só de fonte confiável" pelo da documentação de Skills da Anthropic (o link da AAIF não diz isso).
3. Item 3: a NASA não deu "uma dúzia" em 2023. Ela disse "high single digits to the low double digits", e a dúzia é inferência do Ars.
4. Item 9: cortar "(antigo Coq)" ou fontear (a Anthropic só cita Rocq).
5. Item 7: "menos de 64 MB", não "até 64 MB".
6. Item 15: "em verificação de software", não "em software".
7. Selar ou cortar as previsões sem selo: linha ⚖️, "vai ouvir do cliente, cada vez mais" e "O cliente pagaria agora porque...".
8. Item 26 (recomendado): ajustar "dois marketplaces", pois a fonte é inconsistente.
9. Item 23 (menor): atribuir o depoimento a Yusuke Kaji e tirar "cerca de".
