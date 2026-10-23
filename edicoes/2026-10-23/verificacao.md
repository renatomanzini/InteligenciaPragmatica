# Verificação — 2026-10-23

Todas as correções obrigatórias das duas partes foram aplicadas no edicao.md (Opus, passo 5). Links: todos ok; EWD667 inconclusivo (tempo esgotado), conteúdo conferido na apuração.

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

# Verificação parte 2 (ECONOMIA até o fim) - edição 2026-10-23

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Ibovespa -1,15% na quinta (22), 204.120 pts | InvestNews | confirmada | - |
| 2 | Menor fechamento desde 2/10 | InvestNews | confirmada | - |
| 3 | Dólar +0,22% a R$ 5,04, reta final do 2º turno | InvestNews | confirmada | - |
| 4 | Bradesco lucro recorrente R$ 7,11 bi, +0,8% tri, +14,6% ano | Bloomberg Línea | confirmada | - |
| 5 | Inadimplência 90+ dias 4,6% (4,1% um ano antes) | Bloomberg Línea | confirmada | - |
| 6 | "crédito mais caro de carregar" (interpretação) | - | interpretação sem selo | Marcar com **Opinião:** ou cortar |
| 7 | França PMI composto 48,4 em outubro, de 51,1, menor em 4 meses | Trading Economics | confirmada (agregador) | Se houver, citar S&P Global/HCOB |
| 8 | Brent "passou de US$ 114" nesta sexta (23) | Trading Economics | não confirmada | A página mostra "cerca de US$ 114,00" no topo e US$ 113,86 nas estatísticas. Escrever "chegou a cerca de US$ 114" |
| 9 | Máxima de 4 anos US$ 114,44, em maio | Trading Economics | confirmada (4/5) | - |
| 10 | Ataques houthis à Arábia Saudita | Trading Economics | confirmada (Yanbu, campo de petróleo, aeroporto de Dammam) | - |
| 11 | Brent 74% acima de um ano atrás | Trading Economics | errada (arredondamento) | Fonte: +74,85% (tabela) e +74,63% (estatísticas). Escrever "cerca de 75%" ou "quase 75%" |
| 12 | Tractian Série D US$ 130 mi, avaliação US$ 1,4 bi, +94% | Bloomberg Línea | confirmada (rodada anterior corrigida para US$ 720 mi) | - |
| 13 | "~R$ 650 mi" | Bloomberg Línea | não confirmada | A fonte não traz o valor em reais. O cálculo é nosso (R$ 656 mi a 5,045). Escrever "cerca de R$ 656 mi (conversão nossa)" ou cortar |
| 14 | Receita anualizada acima de US$ 100 mi (contra US$ 40 mi em 2024) | Bloomberg Línea | confirmada (setembro de 2026) | - |
| 15 | Sensores para prever quebra de máquina | Bloomberg Línea | confirmada | - |
| 16 | Cade/SG recomendou arquivar queixa da Aiqfome; é recomendação | Bloomberg Línea | confirmada | - |
| 17 | Acordo de 2023 limita exclusividade a 25% "do volume vendido" | Bloomberg Línea | errada (termo) | A fonte diz 25% do GMV total da plataforma (valor, não volume). Escrever "25% do GMV (valor vendido) da plataforma" |
| 18 | Carrefour vendeu 22 imóveis ao Pátria Renda Urbana, valor não divulgado, depende do Cade | InvestNews | confirmada | - |
| 19 | OpenAI negocia até US$ 30 bi a US$ 1,25 tri antes do dinheiro entrar (pre-money), segundo a CNBC | TechCrunch | confirmada | - |
| 20 | "Bloomberg falava em US$ 1,4 tri, US$ 150 bi a mais" | TechCrunch | parcialmente confirmada | O TechCrunch diz que a Bloomberg reportou US$ 30 bi a US$ 1,4 tri um mês antes, mas não informa se era pre ou post-money. Os US$ 150 bi são conta nossa e só valem na mesma base. Acrescentar "sem confirmar se a base é a mesma" ou cortar a diferença |
| 21 | Front matter: "abaixo da meta anterior" | TechCrunch | não confirmada | O artigo não fala em "meta". Usar "abaixo do valor reportado antes" |
| 22 | Barclays corta cerca de 5.000 vagas (5%) até o fim de 2026, ligado a IA | Business Standard (Reuters) | confirmada (WebFetch deu 403; conferido via curl: "5 per cent of its workforce this year", "remainder by end of the year", 1.000 já saíram) | Atribuir a "Reuters, via Business Standard" |
| 23 | Meta: termos de 30/10, anunciantes "solely responsible" | Adweek | confirmada | - |
| 24 | Bookshop.org "tiraram ou corrigiram anúncios" | Adweek | parcialmente confirmada | A fonte diz que a Bookshop.org desligou todos os recursos de IA da Meta, após um anúncio receber ilustração gerada por IA. Não há "tirou o anúncio" citado no trecho lido. Reescrever como "desligou os recursos de IA da Meta" |
| 25 | "revise as opções do Advantage+ campanha por campanha" | Adweek | confirmada (recomendação de agências) | Atribuir a agências como Exverus e AdCellerant, ou marcar como orientação nossa |
| 26 | AI Overviews em 88% de 400 buscas comerciais, EUA, desktop, agosto | Semrush | confirmada | - |
| 27 | 45,75% em setembro de 2025; "quase o dobro de 11 meses antes" | Semrush | confirmada (88/45,75 = 1,92) | - |
| 28 | Semrush mede só aparição, não clique | Semrush e PPC Land | confirmada | - |
| 29 | Em 100 sites, ChatGPT = 0,62% do Google orgânico (amostra pequena) | PPC Land | confirmada | O PPC Land cita estudo de terceiros e não o nomeia. Acrescentar "segundo o PPC Land" |
| 30 | Bloco **Opinião:** em STATS (hipótese da Semrush, não medida) | Semrush | confirmada | Selo presente. A Semrush diz "ranking number one likely won't lead to as much traffic": é expectativa. OK |
| 31 | "quase toda busca de compra" no TL;DR | Semrush | ok | 88% das palavras-chave. Pelo volume é cerca de 97% |

## Itens não checados nesta parte
A seção "Para ler, ouvir ou assistir" e o texto de "Hoje eu aprendi" estão fora da lista de checagem desta parte. Os links de Dijkstra, TechCrunch (agentes na ilha) e YouTube não foram abertos. O fato de a seção ser "Para ler/assistir" sem cunho opinativo é aceitável. A frase "a linguagem formal protege de erro bobo..." é paráfrase de Dijkstra, sem selo, e deveria ser conferida na fonte.

## Correções obrigatórias
1. Brent: trocar "passou de US$ 114" por "chegou a cerca de US$ 114" (fonte: US$ 114,00 no topo, US$ 113,86 nas estatísticas). Ajustar também o título em front matter ("Brent passa de US$ 114").
2. Brent: "74% acima" para "cerca de 75%" (fonte: 74,85% / 74,63%).
3. Tractian: remover "~R$ 650 mi" ou indicar "cerca de R$ 656 mi, conversão nossa".
4. iFood: "25% do volume vendido" para "25% do GMV total da plataforma" (valor, não volume).
5. OpenAI: a diferença de "US$ 150 bi" compara bases não confirmadas (o US$ 1,25 tri é pre-money; a base da Bloomberg não é informada). Ressalvar ou cortar. No front matter trocar "meta anterior" por "valor reportado antes".
6. Meta: "tiraram ou corrigiram anúncios" não é sustentado para a Bookshop.org (ela desligou os recursos de IA). Reescrever. Atribuir o conselho do Advantage+ às agências.
7. Bradesco: "crédito mais caro de carregar" é interpretação sem selo. Pôr **Opinião:** ou cortar.
8. Barclays: atribuir a Reuters (via Business Standard).
9. PPC Land: citar que o 0,62% vem de estudo de terceiros reportado pelo PPC Land.
