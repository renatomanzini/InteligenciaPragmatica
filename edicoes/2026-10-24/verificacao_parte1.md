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
