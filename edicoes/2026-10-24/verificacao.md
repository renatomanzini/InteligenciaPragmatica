# Verificação — 24/10/2026 (nº 9)

# Verificação, parte 1 (bom dia, breakthroughs, histórias em andamento) — edição 2026-10-24

Fontes abertas por WebFetch ou curl em 24/10/2026. The Verge e Ars Technica bloqueiam o WebFetch; foram lidos por curl.

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Kimi K3.1 Pro, da Moonshot, lançado em 23/10 | Artificial Analysis (release date Oct 23, 2026); blog Kimi ("rolls out today", sem data) | confirmada | — |
| 2 | 4º entre 215 modelos, 55 pontos | Artificial Analysis | confirmada (com ressalva) | A página também cita 217 e 709 modelos em outros trechos. Manter "4º de 215" só com o rótulo "no resumo do modelo", ou escrever "4º lugar". |
| 3 | API a US$ 2 (entrada) e US$ 10 (saída) por milhão de tokens, segundo Willison | Willison; Artificial Analysis | confirmada | — |
| 4 | Cerca de 5x menos que Claude Fable 5.1 (US$ 10 e US$ 50) | Página de preços da Anthropic | confirmada | — |
| 5 | Mesmo preço do Sonnet 5.5 (US$ 2/US$ 10) | Anthropic: Sonnet 5.5 US$ 2 / US$ 10 | confirmada | — |
| 6 | Mesmo preço do Gemini 4 Argon, "este até 30/11" | Google: US$ 2/US$ 10 até 30/11/2026, depois US$ 4/US$ 20 | confirmada | — |
| 7 | Pesos "só prometidos"; citação "Full model weights will be released by Nov 4, 2026" | Blog Kimi: "The full model weights will be released by Nov 4" (seção de disponibilidade repete "by Nov 4, 2026"); Willison cita a frase com "Full" e "2026" | confirmada em substância; citação não literal | O blog tem "The full model weights will be released by Nov 4". Citar assim, ou manter a forma de Willison e creditar a ele. |
| 8 | 65,7% no Terminal-Bench 4.0, número da própria Moonshot | Blog Kimi | confirmada | — |
| 9 | Usuários no Hacker News: cota das assinaturas acaba rápido e modelo é verboso | HN 50212065 | confirmada | Houve quem discordasse (um usuário usou 22% da cota semanal). Considerar "vários usuários". |
| 10 | Licença comercial "ainda não confirmada" | Blog Kimi não especifica licença | confirmada | — |
| 11 | **Opinião:** (pesos em 4/11, voltar ao assunto) | — | selo presente | — |
| 12 | 21/10: PHP corrigiu duas falhas críticas, nota 9,2 no CVSS | php.net (21/10, CVE-2026-109618 e -109619); Wiz; Euronews (9.2 de 10) | confirmada | — |
| 13 | Valem para toda versão desde o PHP 5.4 | Wiz: "nearly every PHP version", "releases back to PHP 5.4" | confirmada com ressalva | "Toda" é forte; Wiz diz que toda versão da última década é afetada por pelo menos uma das falhas. Escrever "praticamente toda versão desde o PHP 5.4". |
| 14 | PHP move cerca de 70% dos sites, segundo a Wiz | Wiz: "70% of all websites" | confirmada | — |
| 15 | "A Calif achou uma delas **em agosto**, em auditoria paga pela OpenAI **com o GPT-5.6 Sol**" | Euronews: Calif achou uma durante auditoria financiada pela OpenAI. Wiz: agradece Calif e OpenAI sem detalhar o papel; usa o GPT-5.6 Sol na própria descoberta; "agosto" (19/08) é a primeira descoberta **da Wiz** | **errada / não confirmada** | Cortar "em agosto" e "com o GPT-5.6 Sol" da frase sobre a Calif. Texto seguro: "A Calif achou uma delas em auditoria financiada pela OpenAI, e a Wiz achou as duas de forma independente (a Wiz usou, entre outras ferramentas, o GPT-5.6 Sol)". A `apuracao.md` marca como confirmado, mas o Euronews não diz isso. |
| 16 | A Wiz achou as duas por conta própria | Euronews: "independently found both" | confirmada | — |
| 17 | "No mesmo dia" (21/10), Wikimedia desligou serviços e França e Alemanha tiraram sites do ar | Euronews (22/10): correções na quarta (21/10); Wikimedia, Interior francês e ITZBund tiraram sites do ar; a NSA pedia que ficassem fora até haver correção | não confirmada quanto ao "mesmo dia" | Os desligamentos são em torno da correção, sem data exata. Trocar por "em seguida" ou "por precaução, na mesma semana". |
| 18 | HTTP2Shell: falha no descompressor Brotli, do Google, CVE-2026-111497, nota 9,2 | Aikido (CVSS v4.0 9.2) | confirmada | — |
| 19 | Node.js divulgou em 21/10, Python em 22/10, em 23/10 ficou claro que atinge outras linguagens | Aikido | confirmada | — |
| 20 | Apache e Nginx não decodificam Brotli por padrão | Aikido | confirmada | — |
| 21 | OpenAI achou em fevereiro; correção não tratada como de segurança | Aikido | confirmada | — |
| 22 | "Quem mantém site de cliente teve uma semana de atualização dupla" | — (inferência) | opinião sem selo | Pôr `**Opinião:**` ou cortar. |
| 23 | OpenAI, em 23/10, passa a treinar sem internet ao vivo, "só com cópia em cache da web" | TechCrunch: cópias em cache e versões simuladas da web | confirmada com ressalva | Escrever "com conteúdo em cache e versões simuladas da web". |
| 24 | "Até 20/09 um modelo explorou uma configuração errada... treino pausado pelo resto do mês" | TechCrunch: "as recently as Sept. 20", treino pausado pelo resto de setembro | confirmada, redação ambígua | "Pelo resto do mês" lido em 24/10 soa como outubro. Escrever "até 20/09... pausado pelo resto de setembro". "Até 20/09" soa como parou; melhor "em 20/09". |
| 25 | Steven Adler (ex-OpenAI) diz que data centers offline custam caro e que uma empresa sozinha ganha pouco | TechCrunch: Adler disse à Fortune que exigiria equipes de pesquisa em data centers pelo mundo, chamou o custo de "a lot" e questionou se o benefício compensa para uma empresa agindo sozinha | parcialmente confirmada | Era declaração à Fortune, citada pelo TechCrunch. Escrever "Adler, que falou à Fortune, questiona se o ganho compensa o custo para uma empresa agindo sozinha". "Ganha pouco" é mais forte que a fonte. |
| 26 | "É a continuação da conversa de 16/10 sobre agentes e responsabilidade" | Nenhuma das fontes citadas | não verificável nesta checagem | É referência a edição anterior; conferir a edição de 17/10 ou cortar. |
| 27 | Meta: termos valiam de 30/10, ficam para 20/11 | Verge (23/10); PPC Land | confirmada | — |
| 28 | Porta-voz: é para ter mais tempo de explicar | Verge: Daniel Roberts, "to allow more time for us to explain..." | confirmada | — |
| 29 | "O texto não mudou, só a data" | PPC Land: sem novo texto ligado ao adiamento. Verge: antes, a Meta já tirara a palavra "training" | confirmada com ressalva | Escrever "o adiamento não mudou o texto". |
| 30 | Editores europeus pedem a suspensão | PPC Land (European Publishers Council pede suspensão); Verge (anunciantes e editores da UE e do Reino Unido pedem aos reguladores que barrem) | confirmada | — |
| 31 | Google: política vigente desde 16/10; não usa Drive, Gmail e Fotos para anúncio personalizado, a menos que você libere esses dados para serviços com anúncio | policies.google.com/privacy | confirmada | — |
| 32 | Google diz ao Ars que é opt-in e que o anúncio não sai "diretamente" da caixa de entrada | Ars: "Connecting your apps is entirely opt-in... Ads will not be based directly on your Gmail inbox or Photos library" (declaração, não necessariamente "ao Ars") | confirmada | Trocar "diz ao Ars Technica" por "disse em declaração citada pelo Ars". |
| 33 | Título da história: "Google pode usar Gmail e Fotos em anúncios para quem liga o Personal Intelligence" | Ars: política reconhece que dados do Personal Intelligence podem contribuir para personalizar anúncios | confirmada | — |
| 34 | LGPD art. 5º, XII: consentimento é manifestação livre, informada e inequívoca do titular | Planalto, lido por curl: "XII - consentimento: manifestação livre, informada e inequívoca pela qual o titular concorda com o tratamento de seus dados pessoais para uma finalidade determinada" | confirmada | — |
| 35 | "A resposta depende de como ele é apresentado" (se botão de ativar cumpre o consentimento) | — (análise jurídica) | opinião sem selo | Pôr `**Opinião:**` ou reformular como pergunta aberta. Ars sustenta que há "prompts e pop-ups" que induzem a ativar, o que dá base à dúvida. |
| 36 | Muse: em 22/10 a Meta religou o compartilhamento depois que pesquisadores da Claroc mostraram links de "artifacts" fáceis de achar; links antigos mudaram | Verge (22/10), com Singleton: "new URL" | confirmada | — |
| 37 | Descompilação: ports de IA de Halo no navegador e Wind Waker no iPhone; Xbox Labs; preservacionistas reclamam de "slop" | Verge (23/10) | confirmada | "O que mudou desde 17/10" é relativo à edição anterior, não à fonte. Xbox Labs foi criado pela CEO do Xbox, Asha Sharma, como divisão interna. Ok. |
| 38 | China: DeepSeek e MiniMax "concluíram o registro de exportação, segundo mídia estatal" | Reuters (via Central Oregon Daily): MiniMax confirmou o registro; uma conta de rede social ligada à CCTV disse que ambas obtiveram aprovação para uso global; DeepSeek não respondeu | confirmada com ressalva | A fonte estatal é uma conta ligada à CCTV e fala em "aprovação", e só a MiniMax confirmou o registro. Escrever "uma conta ligada à CCTV disse que as duas obtiveram aprovação; a MiniMax confirmou à Reuters o registro". |
| 39 | Cerca de uma semana depois da proposta de controle de 23 tecnologias de IA | Reuters | confirmada | — |
| 40 | Brent fechou a sexta (23/10) perto de US$ 117, alta de mais de 6% na semana, após ataques à Arábia Saudita; valor diverge | InvestNews: manchete "US$ 117", corpo "abaixo de US$ 117", alta de mais de 6% | confirmada | A divergência é interna ao próprio InvestNews. Se possível, citar uma segunda fonte para o fechamento exato. |
| 41 | Sem selo em "Nenhum esta semana, e tudo bem" e "o critério é simples" | — | juízo editorial do formato, aceitável | — |

## Correções obrigatórias

1. **Item 15 (PHP):** tirar "em agosto" e "com o GPT-5.6 Sol" da frase sobre a Calif. Nenhuma fonte liga esses dois detalhes à Calif; o "agosto" (19/08) e o GPT-5.6 Sol são da descoberta da Wiz. Corrigir também a `apuracao.md`, que marca como confirmado.
2. **Item 17 (PHP):** "No mesmo dia" não é sustentado pela fonte. Trocar por "em seguida" ou sem marcador de dia.
3. **Item 25 (OpenAI/Adler):** a declaração foi à Fortune, e "uma empresa agindo sozinha ganha pouco" é mais forte que a fonte, que só questiona se o benefício compensa. Reescrever.
4. **Item 24 (OpenAI):** trocar "pelo resto do mês" por "pelo resto de setembro" e "até 20/09" por "em 20/09".
5. **Item 38 (China):** deixar claro que a fonte estatal é uma conta ligada à CCTV, que fala em aprovação, e que só a MiniMax confirmou o registro.
6. **Itens 22 e 35 (opinião sem selo):** pôr `**Opinião:**` em "quem mantém site de cliente teve uma semana de atualização dupla" e em "a resposta depende de como ele é apresentado", ou cortar.
7. **Item 26:** "continuação da conversa de 16/10" não tem fonte; conferir na edição anterior ou cortar.

Correções recomendadas (menores): itens 2 (215 vs. 217 modelos), 7 (citação literal do blog Kimi), 13 ("praticamente toda versão"), 23 (cache e versões simuladas), 29 (o adiamento não mudou o texto), 32 (declaração, não "ao Ars").

# Verificação, parte 2 (Os números da semana até o fim) - 24/10/2026

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| Multa civil de US$ 25 bi imposta à Meta em 21/10 (Novo México) | 10-Q Meta: "On October 21, 2026, the court issued an order imposing a civil penalty in the amount of $25 billion" | confirmada | - |
| ~2,5x o lucro líquido do 3T (US$ 9,86 bi) | 10-Q: net income 3T26 = US$ 9.860 mi; 25/9,86 = 2,54 | confirmada | - |
| Provisão de valor não divulgado; vai recorrer | 10-Q: "accrued an amount for loss contingencies... intend to appeal" | confirmada | - |
| YouTube 15,8% do tempo de TV nos EUA em agosto, recorde | Nielsen: "platform-record 15.8% of TV" | confirmada | - |
| Netflix 7,7%; YouTube "pouco mais que o dobro" | Nielsen: Netflix 7.7%; 15,8/7,7 = 2,05 | confirmada | - |
| Uso total de TV caiu 4,4% de julho a agosto | Nielsen: "4.4% decrease in total TV usage" | confirmada | - |
| Muse: 10,2 milhões de downloads nos EUA em 40 dias | 9to5Mac: "10 million US downloads in 40 days"; o número 10,2 não aparece na página (a apuração.md também escreveu 10,2 sem trecho) | não confirmada | Escrever "mais de 10 milhões" / "10 milhões", ou cortar o decimal |
| ChatGPT 3,7 milhões no mesmo período (40 dias) | 9to5Mac: "ChatGPT... 3.7 million... during their first 40 days" (US) | confirmada | - |
| Estimativa da Sensor Tower | 9to5Mac (fonte secundária, relata o relatório) | confirmada | - |
| Uber: 30 mil funcionários no ChatGPT Work | TechCrunch 22/10: "some 30,000 people" | confirmada | - |
| 30 vezes o piloto de cerca de 1.000 | TechCrunch: piloto com 1,000; 30.000/1.000 = 30 | confirmada | - |
| Custo não divulgado | TechCrunch: "didn't disclose how much it's spending" | confirmada | - |
| Em 08/10 a AT&T virou "parceira de desenho" da OpenAI para "criar, construir e avaliar" fluxos jurídicos com supervisão de advogados | Artificial Lawyer (08/10) diz só "partnering with OpenAI to develop AI-enabled legal workflows"; "design partner" e "create, build, evaluate" não aparecem. Página da OpenAI deu 403 (só JS) | não confirmada | Trocar por "parceria para desenvolver fluxos jurídicos com IA" ou citar fonte que traga "design partner"; a apuração marcou PARCIAL no release da AT&T e da OpenAI |
| LegalEdge, centro "AI-first" criado em janeiro | AL: "AI-first centre of expertise... launched in January this year" | confirmada | - |
| "quase 100 casos" em seis meses; número da empresa | AL: "handled nearly 100 matters in its first six months" (citação da AT&T) | confirmada | "casos" traduz "matters"; ok |
| David McAtee, general counsel; "Legal judgment remains human." | AL: "senior executive vice president and general counsel"; frase idêntica | confirmada | - |
| "A OpenAI também conta o caso em seu site" (openai.com/index/att-legal) | 403/JS, conteúdo não lido | não confirmada | Cortar o link ou tirar a frase; a apuração também só tinha 403 |
| Sem número de tempo, custo ou erro; ferramentas e tarefas não nomeadas; fase de desenho | AL não traz tais números nem ferramentas | confirmada (ausência) | - |
| ABA Opinião Formal 512 (29/07/2024) exige competência, sigilo e consentimento informado | PDF da ABA: data July 29, 2024; trata de competência, confidencialidade e "informed consent" | confirmada | - |
| OAB: "Conselho Pleno da OAB aprovou em 11/11/2024" recomendações de IA generativa | Página OAB-SP (27/11/2024): "aprovado pelo Conselho Federal da OAB"; não cita 11/11 nem "Conselho Pleno" | errada (órgão) / não confirmada (data) | Escrever "o Conselho Federal da OAB aprovou recomendações (divulgadas em 27/11/2024)", sem 11/11. Sigilo, ética e comunicação ao cliente conferem |
| Simon Willison comenta em 19/10 o texto de Jeremy Scheff (agentes tiraram o quebra-cabeça de que ele gostava) | Willison 19/10 e dumbmatter.com (08/10): conferem | confirmada | - |
| Johnathan Bi entrevista Harvey Lederman, professor da NYU, 23/10 | Substack: "NYU Professor Harvey Lederman", Oct 23, 2026 | confirmada | - |
| Corvos ~235 ms; cerca de 2x mais rápido que humanos e macacos; Univ. de Tübingen; só 2 corvos; comparação com estudos anteriores | Ars Technica (Oct 23): "averaged 235 milliseconds", macacos 410/490/600 ms em três estudos, "two carrion crows", Nieder da Univ. de Tübingen | confirmada | Observação: Ars chama de "task"/decisão, não só "direção de movimento"; ok |
| Estudo "na Science" | Ars (texto lido) não nomeia a revista; só a apuração diz Science | não confirmada | Cortar "na Science" ou confirmar na fonte primária |
| Opinião sem selo | Trecho "valor está mais na arrumação e no sigilo" tem `**Opinião:**`; "Freio de realidade" e "Agora aplica" são orientação, não fato | confirmada | - |

## Correções obrigatórias
1. Muse: trocar "10,2 milhões" por "mais de 10 milhões" (a fonte só diz 10 milhões).
2. OAB: o órgão é o Conselho Federal, não "Conselho Pleno", e "11/11/2024" não está na fonte; usar a data da divulgação (27/11/2024) ou cortar a data.
3. AT&T: "parceira de desenho" e "criar, construir e avaliar" não estão na fonte linkada; reescrever como "parceria para desenvolver fluxos jurídicos com IA".
4. Remover a frase "A OpenAI também conta o caso em seu site" e o link openai.com/index/att-legal (não lido, 403), ou marcar como não verificado.
5. Corvos: tirar "na Science" (o Ars não cita a revista) ou confirmar na fonte primária.

## Correções aplicadas
Parte 1: Calif sem 'agosto'/'GPT-5.6 Sol'; 'em seguida' no lugar de 'no mesmo dia'; Adler à Fortune, reescrito; '20/09' e 'resto de setembro'; China com a conta ligada à CCTV e só a MiniMax confirmando; selo de Opinião em duas frases; cortada a ligação com 16/10; '4º lugar' sem o 215; citação dos pesos parafraseada; 'praticamente toda versão'; 'cache e versões simuladas'; 'o adiamento não mudou o texto'; 'declaração citada pelo Ars'.
Parte 2: Muse 'mais de 10 milhões'; Conselho Federal da OAB, divulgadas em 27/11/2024; AT&T 'parceria para desenvolver fluxos'; link openai att-legal removido; corvos sem 'na Science'; freio sem 'fase de desenho'.
