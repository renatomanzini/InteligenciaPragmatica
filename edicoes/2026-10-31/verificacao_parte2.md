# Verificação, parte 2 (Números da semana até a pergunta) - edição 2026-10-31

Método: WebFetch e curl simples nas fontes citadas. SEC bloqueou o acesso automatizado (não contornei). `main.py github` falhou (HTTP 403, repositório não habilitado na sessão); estrelas conferidas pela página do GitHub via WebFetch e a data pelo `git log` de um clone raso.

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| Desemprego 5,2% no trimestre até setembro, IBGE, divulgado 30/10 | Estadão (30/10/2026) | confirmada | - |
| Menor taxa para o trimestre desde 2012 | Estadão: "a menor taxa para o período desde 2012, início da série" | confirmada | - |
| Contra 5,6% um ano antes | Estadão: 5,6% no 3º tri de 2025 | confirmada | - |
| "FGV e Inter já veem perda de fôlego" | Estadão: FGV IBRE projeta alta do desemprego em 2027; Inter diz que o mercado está "muito próximo do pico" | confirmada (com nuance) | Ideal: "FGV prevê alta do desemprego em 2027; Inter vê o mercado perto do pico". |
| DoorDash: "algumas centenas" de pedidos de agentes de IA de terceiros, Tony Xu, no total, sem período | TechCrunch: "maybe several hundred orders in total from some of these third-party agents" (teleconferência do 3º tri) | confirmada | Opcional: "talvez algumas centenas". |
| 993 milhões de pedidos no 3º trimestre | Link SEC (press release). A SEC bloqueou o acesso automatizado; o TechCrunch não traz esse número | NÃO CONFIRMADA | Abrir o release no navegador e conferir "Total Orders" do 3T26 e o escala (milhões). Se não conferir, cortar o número ou apontar só a fonte que o traz. |
| Microsoft: ~11% da receita vem de acordos com a OpenAI, US$ 10 bi de US$ 92,3 bi, trimestre até 30/09 | Startups: "quase 11%", US$ 10 bi, US$ 92,3 bi, trimestre encerrado em 30/9 | confirmada | Conta 10/92,3 = 10,8%, coerente. |
| "Não se sabe quanto é repasse e quanto é Azure" | Startups: a Microsoft não detalhou | confirmada | - |
| Kalshi vale US$ 40 bi | Folha/C-Level: rodada avalia em US$ 40 bi (Tarek Mansour, 29/10) | confirmada | - |
| Alta de 82% desde maio (US$ 22 bi) | Folha: rodada de maio a US$ 22 bi; o "82%" não está na fonte, é conta (40/22 = +81,8%) | confirmada (número calculado) | Dizer "alta de cerca de 82%, pela nossa conta" ou "de US$ 22 bi em maio". |
| Quase o dobro da Polymarket (US$ 21 bi) | Folha: "quase o dobro"; Polymarket US$ 21 bi era a rodada de agosto "sendo finalizada" | confirmada (com nuance) | Acrescentar "na rodada de agosto". |
| Fujifilm quer 5 vezes a capacidade de fitas LTO "até o ano fiscal de 2028" | Ars Technica: 5x sobre o nível do ano fiscal de 2025; projeto roda dos anos fiscais 2026 a 2028 | confirmada (com ressalva) | "5x em relação ao ano fiscal de 2025, com o projeto indo até o ano fiscal de 2028". |
| Cerca de ¥10 bi (~US$ 63 mi) | Ars: "roughly 10 billion yen (about $63 million)" | confirmada | - |
| IA generativa aumentou a demanda por arquivar dados | Ars: Fujifilm atribui a alta à IA generativa | confirmada | Deixar claro que é a atribuição da Fujifilm. |
| "na prática, a fita, barata e fora da rede, voltou a ter emprego" | Ars não diz "barata" nem "fora da rede" (diz que o mundo corporativo nunca abandonou a fita) | NÃO CONFIRMADA / opinião sem selo | Cortar, ou reescrever como fato da fonte ("a fita nunca saiu das empresas") ou pôr `**Opinião:**`. "Voltou" também contraria a fonte. |
| IA na prática: em 30/10 o Google (John Mueller) anunciou controle novo baseado no AIPREF do IETF | Post do Google, sexta 30/10/2026, assinado por John Mueller, cita o AIPREF do IETF | confirmada | - |
| Meta é 2027 e é rascunho, não padrão | Google: "We aim to support this new control along with other AI providers in 2027"; "This draft proposal" | confirmada | - |
| Linha `user-agent: __usage_ai-training` com Disallow, "segundo SER e PPC"; o post do Google não a escreve | PPC Land traz o token `__usage_ai-training`. O post do Google fala em "policy token" e não a escreve. O SER (pelo que consegui ler) não menciona a linha | parcialmente confirmada | Atribuir a linha só ao PPC Land. A ressalva de que o Google não a escreve está correta. |
| Se o site recusar treino pelo token e não mencionar Google-Extended, o Google trata como se estivesse bloqueado | Google: "Google plans to interpret that as if the publisher had disallowed Google-Extended" | confirmada | Trocar "trata" por "pretende tratar" (é plano para 2027). |
| Bing separou treino de "grounding" (usar a página para montar resposta com citação) | SER e PPC: AI Training, AI Grounding e Limited Grounding | confirmada | - |
| Dá para recusar treino e seguir citado no Copilot; ranking normal do Bing não muda | SER: exemplo de editor que bloqueia treino e permite citação no Copilot; "traditional Bing rankings are unaffected" | confirmada | - |
| Bing passa a valer em 01/02/2027 | SER/PPC: 1/2/2027 "Microsoft starts honoring the new preferences as it crawls" | confirmada | - |
| Bing: controles temporários em 15/12 e migração das regras antigas até 01/03/2027 | SER/PPC: 15/12/2026 (para quem usa NoArchive/NoCache); 1/3/2027 prazo para quem usa as diretivas antigas | confirmada | Ressalva: 15/12 vale só para sites com NoArchive/NoCache. Falta citar 30/09/2027 (fim das preferências temporárias), opcional. |
| "OpenAI e Anthropic também aderem, segundo as mesmas fontes" | SER: OpenAI e Anthropic "on board". PPC: OpenAI publicou compromisso; Anthropic "reportedly", citando o SER. O post do Google não os menciona | confirmada (fraca para Anthropic) | Trocar por "segundo o Search Engine Roundtable" e, para a Anthropic, "segundo relato". Cuidado também com o título da história no front matter ("Google, Bing, OpenAI e Anthropic apoiam"). |
| Freio: Nate Hake, "editor que participou do grupo", diz que o trabalho está incompleto, segundo o PPC Land | PPC: Hake, "publisher" do grupo, alertou no X que o trabalho está inacabado (paráfrase, sem citação) | confirmada (cargo impreciso) | Trocar "editor" por "publisher/dono de site de mídia". Sem aspas, ok. |
| "E não se sabe o efeito sobre as AI Overviews na busca do Google" | Nenhuma fonte afirma isso; o post do Google não trata das AI Overviews | NÃO CONFIRMADA | Reescrever: "o post do Google não diz se o sinal vale para as AI Overviews" (verdadeiro como ausência) ou cortar. |
| "O robots.txt vale por educação, não por fechadura / é um pedido, não uma tranca" | Contexto geral, sem fonte específica | não confirmada (explicação genérica) | Aceitável como explicação; evitar tom de fato novo. |
| UE: Diretiva 2019/790, art. 4(3), só libera mineração de texto e dados se o titular não reservou o direito | legislation.gov.uk (art. 4): "has not been expressly reserved by their rightholders in an appropriate manner, such as machine-readable means in the case of content made publicly available online" (texto da UE, sem alteração) | confirmada | - |
| Aspas "por meios legíveis por máquina" | O texto oficial em inglês é "such as machine-readable means"; a versão portuguesa oficial (EUR-Lex PT) não conferi e não é essa frase literal | ASPAS NÃO VERIFICADAS | Tirar as aspas (parafrasear) ou copiar a redação exata da versão PT do EUR-Lex. Usar "reservado expressamente, de forma adequada, p. ex. por meios de leitura automática". |
| "Um sinal padronizado dá forma a essa reserva" | Inferência; o post do Google cita o Código de Práticas da UE (GPAI), não o art. 4(3) | opinião/inferência sem selo | Pôr `**Opinião:**` ou escrever "o Google cita o Código de Práticas de IA de uso geral da UE, que reconhece o robots.txt". |
| Oportunidades (advogado, e-commerce, jornalista) e o serviço "política de IA do site" | Sugestões editoriais | n/a | A frase "**Opinião:** é serviço pequeno..." tem selo. "Por que agora" usa as datas do Bing (confirmadas). |
| Link SigNoz (28/02/2026): "quando a IA resolve 95% dos incidentes, o humano piora nos 5% que importam" | SigNoz, 28/02/2026, "AI Isn't Replacing SREs. It's Deskilling Them.": o 95%/5% é pergunta hipotética, sem dado | PARCIAL (enganoso) | Escrever "e se a IA resolver 95% dos incidentes: o humano piora nos 5% que importam?" e deixar claro que a divisão é hipotética. |
| Verge (Lauren Feiner, 30/10): Wikimedia, em amicus brief, diz que treinar IA deve ser fair use, mas regurgitar artigos não | Verge, 30/10/2026, Lauren Feiner: amicus brief (sexta), sem apoiar nenhum lado no caso NYT x OpenAI | confirmada | "Pode ter paywall" não conferi (a página abriu por curl). |
| nesformer: Drew Breunig pôs a CPU do NES nos pesos do Qwen3.5-4B, Super Mario roda "very slowly" | Simon Willison (30/10): "emulator for a NES 6502 CPU into the weights of Qwen3.5-4B ... (very slowly)" | confirmada | - |
| Repositório criado em 30/10 | Clone raso: 1 commit, 30/10/2026 08:59 -0700. A API de criação não ficou acessível | confirmada (por indício) | - |
| 194 estrelas em 31/10 | Página do GitHub (WebFetch): 194 estrelas. `main.py github` falhou (403), então não foi pelo comando do manual | confirmada (por página) | Rodar `python main.py github dbreunig/nesformer` na máquina com token antes de enviar, para registrar a contagem. |
| Pergunta da semana | Sem afirmação factual | n/a | - |

Sem aspas inventadas encontradas, fora a do art. 4(3). A citação de Willison "very slowly" é do post dele, curta.

## Correções obrigatórias

1. **993 milhões de pedidos (DoorDash)**: não confirmado (TechCrunch não traz, SEC bloqueou). Conferir no release da SEC ou cortar o número.
2. **Fujifilm**: cortar ou selar como opinião "a fita, barata e fora da rede, voltou a ter emprego"; corrigir "até o ano fiscal de 2028" para "5x em relação ao ano fiscal de 2025, projeto até o ano fiscal de 2028".
3. **Art. 4(3)**: remover as aspas de "por meios legíveis por máquina" (ou usar a redação exata da versão PT) e selar com `**Opinião:**` a frase "Um sinal padronizado dá forma a essa reserva".
4. **"Não se sabe o efeito sobre as AI Overviews"**: reescrever como "o post do Google não diz" ou cortar.
5. **SigNoz**: marcar que o 95%/5% é hipotético, não dado.
6. **Google-Extended**: trocar "trata" por "pretende tratar".
7. **Linha `user-agent: __usage_ai-training`**: atribuir só ao PPC Land (o SER não a traz, pelo que li).
8. **OpenAI e Anthropic**: atribuir ao Search Engine Roundtable (e a Anthropic como "segundo relato"); o Google não os cita. Rever o título da história robots-txt-treino-ia no front matter.
9. **Estrelas do nesformer**: rodar `main.py github` com token antes do envio (hoje só a página do GitHub mostra 194).

Menores (opcionais): Nate Hake é "publisher", não "editor"; "82%" é conta nossa; Polymarket US$ 21 bi é da rodada de agosto; Bing 15/12 vale só para quem usa NoArchive/NoCache.
