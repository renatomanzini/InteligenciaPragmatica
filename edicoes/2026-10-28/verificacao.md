# Verificação — 2026-10-28

# Verificação, parte 1 (bom dia até o fim do IA na prática), edição 2026-10-28

Método: S-1 baixado por curl e pesquisado no texto; blog da Liquid, model card do Hugging Face, Archaeology e TechCrunch lidos por curl; Cornell/eCFR conferido. Não verificado de forma independente: "o rascunho que a gente noticiou" de 21/10 (depende da edição anterior).

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Hollands (Sheffield) recriou o vidro da Taça de Licurgo, ~1.600 anos, verde refletida / vermelha por trás, nanopartículas de ouro e prata, recriou o vidro e não a taça | Archaeology | confirmada (com ressalva) | A fonte diz que os romanos "são pensados" (thought) a ter usado ouro e prata. Escrever "provavelmente nanopartículas". |
| 2 | S-1 protocolado em 26/10 | S-1 ("As filed ... on October 26, 2026") | confirmada | |
| 3 | Receita 1º sem. 2026 US$ 16,3 bi (16.286 mi); 14x os US$ 1,16 bi (1.163 mi) | S-1 | confirmada | |
| 4 | Prejuízo líquido US$ 80,7 bi (80.748 mi) | S-1 | confirmada | |
| 5 | Listagem classe A na Nasdaq, código "ANT", preço e quantidade em branco | S-1 | confirmada | |
| 6 | US$ 72,4 bi de reavaliação de notas conversíveis, derivativos e SAFEs (72.388 mi) | S-1 | confirmada | |
| 7 | Prejuízo operacional de só US$ 693 mi | S-1 | confirmada | |
| 8 | "Tirando esse efeito e a remuneração em ações (US$ 2,2 bi)" chega a lucro operacional ajustado de US$ 1,6 bi (margem 10%) e líquido ajustado de US$ 2,7 bi | S-1 (1.618; 2.671; SBC 2.185) | confirmada nos números, imprecisa na descrição | O lucro operacional ajustado NÃO usa o efeito do valor justo (ele fica abaixo da linha operacional): é -693 + SBC 2.185 + doações não monetárias 126 = 1.618. O efeito de 72,4 bi entra só no líquido ajustado (que ainda soma 8,7 bi de outros ajustes de mercado). Reescrever: "o lucro operacional ajustado tira a remuneração em ações (US$ 2,2 bi) e doações; o líquido ajustado tira também a reavaliação". |
| 9 | ~US$ 417 bi em compromissos de computação e data centers | S-1 (aprox. US$ 417 bilhões, arrendamentos e compras, firmados após 31/12/2025) | confirmada | |
| 10 | "uns 26 vezes a receita do semestre" | cálculo 417/16,286 = 25,6 | confirmada | |
| 11 | Pode emitir até US$ 42 bi em notas conversíveis para pagar à Broadcom o aluguel de chips | S-1 (US$ 42,0 bi, "solely to finance rent obligations"; emissão a Broadcom ou parceiro financeiro designado) | confirmada | Opcional: "à Broadcom ou a um parceiro financeiro dela". |
| 12 | Modelos, próprios e de terceiros, mostraram "em testes" comportamento de autopreservação | S-1 risk factors | parcial | O S-1 diz "testing or real-world deployments" e "models, including our own"; terceiros só na frase sobre incidentes. Trocar "em testes" por "em testes ou em uso real" e atribuir: "modelos, inclusive os próprios, já mostraram...". |
| 13 | "behavior resembling blackmail" | S-1 | confirmada (citação literal, 4 palavras) | |
| 14 | Senciência como risco de reputação e de regulação | S-1 | confirmada | |
| 15 | "riscos catastróficos ou existenciais à humanidade" | S-1 ("catastrophic or existential risks to humanity") | confirmada | Está atribuído como preocupação de partes interessadas e do mercado, não como convicção da empresa; ok, mas pode dizer "o S-1 registra que investidores e pesquisadores levantam". |
| 16 | Regulation S-K Item 105 exige discutir fatores de risco e desencoraja riscos genéricos | Cornell (17 CFR 229.105) | confirmada | |
| 17 | Classe T (LTBT) elege a maioria do conselho | S-1 | confirmada | |
| 18 | Única ação classe F, dos cofundadores, tem 50,1% do voto "em certas matérias" | S-1 ("50.1% of the total voting power ... on all matters submitted to a vote of stockholders generally, including the election of directors other than Class T") | errada (escopo) | Trocar por "tem 50,1% do poder de voto nas matérias votadas pelos acionistas em geral, inclusive na eleição dos conselheiros que não são da classe T". "Certas matérias" subestima o poder. |
| 19 | 5% para o fundo de benefício público (846,8 milhões de ações) | S-1 (846.840.960 ações classe N, 5% do diluído, supondo conversão total das notas da Amazon) | confirmada | Opcional: dizer "classe N" e "5% do capital totalmente diluído". |
| 20 | 5 maiores clientes ~25% da receita de 9 meses | S-1 | confirmada | |
| 21 | S-1 diz que as margens "may compress" | S-1 | confirmada (citação literal) | |
| 22 | "O fornecedor de IA do seu cliente queima caixa em compromissos enormes" | S-1: caixa operacional +US$ 3.929 mi no 1º sem. 2026 (era -2.637 em 2025); financiamento +110.774 mi | errada / não sustentada | O S-1 mostra caixa operacional positivo no semestre. Cortar "queima caixa". Trocar por "tem compromissos enormes de computação e depende de financiamento externo (US$ 110,8 bi entraram por financiamento no semestre)". |
| 23 | "o preço de API pode mudar" | nenhuma | especulação sem selo | Cortar ou marcar como hipótese ("a aposta é", com quem aposta) ou como **Opinião:**. |
| 24 | "O ajuste é escolha da empresa, e ação paga a funcionário é custo de verdade." | nenhuma | opinião sem selo | Prefixar com **Opinião:** (o manual, seção 14.6). |
| 25 | "Ajustado é o lucro depois de tirar o que incomoda." | nenhuma | opinião sem selo | Prefixar com **Opinião:** ou cortar. |
| 26 | "O que mudou desde 21/10... os números batem" com o rascunho noticiado | edição anterior (não aberta) | não verificada nesta passada | Conferir na edição de 21/10. |
| 27 | LFM3 lançado em 27/10, seis modelos de ~2B (texto, visão, áudio e omni) | blog Liquid (OCT 27, 2026; "six 2B-class models (text, vision, audio, omni, and decision)") | confirmada | Faltou "decisão" na lista; incluir ou escrever "entre eles texto, visão, áudio e omni". |
| 28 | LFM3-1.7B roda em ~1 GB em 4 bits | blog e model card | confirmada (número da empresa) | |
| 29 | Contexto de 128 mil tokens custa 1,6 GB de memória, contra 4,3 GB do Qwen3.5-4B | blog ("1.6 GB of KV cache") | confirmada | Precisar: "1,6 GB de cache de contexto (KV cache)". "Memória" total soaria como 1 GB + 1,6 GB; o leitor pode se confundir. |
| 30 | BFCL V4 71,4 contra 62,8 de um modelo de 9B | blog (71.39; Qwen3.5 9B 62.83) | confirmada | |
| 31 | GPQA Diamond 63,4 contra 80,4 | blog (63.37; 80.40 Qwen3.5 9B) | confirmada | |
| 32 | "Nesta edição": modelo de ~1 GB "roda no notebook de 8 GB" | nenhuma fonte cita 8 GB | não confirmada | Cortar "de 8 GB" ou trocar por "num notebook comum". A prévia ("cabe no seu notebook") é suportada só como "laptop" e "phone or laptop" do model card. |
| 33 | Opera anunciou o WebAI, "novo padrão" para IA local, prévia opcional no Opera One, segundo o TechCrunch | TechCrunch (27/10) | confirmada | |
| 34 | "não há especificação pública nem órgão de padrões citado" | TechCrunch não cita; ausência não verificada fora dele | parcial | Reescrever: "o TechCrunch não cita especificação pública nem órgão de padrões" (é o que se sabe). |
| 35 | Model card: 1.7B não recomendado para código agêntico e raciocínio complexo em várias etapas; indica busca (RAG) | model card | confirmada | |
| 36 | "a qualidade em português não foi avaliada" | model card lista português entre os idiomas; avaliação não achada | parcial | Escrever "não encontrei avaliação independente em português". |
| 37 | Licença LFM Open License v1.0 | model card | confirmada | |
| 38 | GGUF para LM Studio/Ollama | model card (GGUF: llama.cpp, Ollama, LM Studio) | confirmada | "~1 GB" do arquivo GGUF não verificado; já há ressalva no texto. |
| 39 | Usos para advogado, clínica, e-commerce, LGPD como argumento de venda | nenhuma (sugestão do redator) | n/a (sugestão, sem fato checável) | Aceitável como ideia; manter "sem prometer conformidade". |

## Correções obrigatórias
1. Classe F: trocar "50,1% do voto em certas matérias" por 50,1% do poder de voto nas matérias votadas pelos acionistas em geral, inclusive eleição dos conselheiros fora da classe T (item 18).
2. Cortar "queima caixa": o caixa operacional do semestre foi positivo (+US$ 3,9 bi); reescrever pelo que o S-1 mostra (item 22).
3. Cortar "de 8 GB" em "Nesta edição" (notebook de 8 GB não está em nenhuma fonte) (item 32).
4. Corrigir a descrição dos ajustes: o lucro operacional ajustado tira a remuneração em ações e doações; o efeito de US$ 72,4 bi só entra no lucro líquido ajustado (item 8).
5. Colocar `**Opinião:**` em "O ajuste é escolha da empresa, e ação paga a funcionário é custo de verdade" e em "Ajustado é o lucro depois de tirar o que incomoda" (ou cortar); cortar ou rotular "o preço de API pode mudar" (itens 23 a 25).
6. Autopreservação: dizer "em testes ou em uso real" e "modelos, inclusive os próprios" (item 12).
7. Opera: trocar a afirmação de ausência por "o TechCrunch não cita especificação pública nem órgão de padrões" (item 34); português: "não encontrei avaliação independente" (item 36).
8. Precisar "1,6 GB de cache de contexto" e completar a lista de modelos com "decisão" (itens 27 e 29).
9. Conferir o vínculo com o rascunho de 21/10 na edição anterior (item 26).
10. Opcional: Taça de Licurgo, "provavelmente" nanopartículas (item 1).

# Verificação, parte 2 (Economia até a pergunta), edição 2026-10-28

Método: cada link foi baixado com curl (WebFetch não foi usado) e o texto lido. WSJ bloqueia (401); conferido por busca.

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Tesouro recomprou R$ 31,6 bi em dois dias | InvestNews | confirmada | nenhuma |
| 2 | R$ 14,8 bi na segunda 26/10 e R$ 16,8 bi na terça 27/10 | InvestNews ("ontem" e "hoje", matéria de 27/10) | confirmada | nenhuma |
| 3 | Para conter a alta dos juros depois do 2º turno | InvestNews (volatilidade após resultado das eleições de domingo, 25/10) | confirmada | nenhuma |
| 4 | 3ª maior intervenção da série, atrás dos R$ 43,6 bi de março | InvestNews ("terceira maior da história em valores nominais"; março, 16 e 17, R$ 43,6 bi) | confirmada | Opcional: a fonte diz "em valores nominais"; trocar "da série" por "da história em valores nominais" |
| 5 | Hypera: lucro de R$ 527 mi no 3º tri | InfoMoney/Reuters | confirmada | nenhuma |
| 6 | +16,1% em um ano | InfoMoney/Reuters | confirmada | nenhuma |
| 7 | Acima dos R$ 471,4 mi esperados | InfoMoney/Reuters (média LSEG) | confirmada | nenhuma |
| 8 | A caneta emagrecedora ajudou (Exame) | Exame: Semavy cobriu a queda dos antigripais; 93 mil unidades em setembro | confirmada | Opcional: a Exame fala em lucro das operações continuadas |
| 9 | Brent a cerca de US$ 116 em 28/10 | Trading Economics (116,28 na tabela; 116,07 no texto) | confirmada | nenhuma. Página ao vivo: o valor muda ao longo do dia |
| 10 | +2% no dia | Trading Economics (+2,11% / +1,93%) | confirmada | nenhuma |
| 11 | ~81% acima de um ano antes | Trading Economics: 80,78% (tabela) e 80,46% (texto) | confirmada, com ressalva | Dois valores diferentes na própria página; "~80%" é mais seguro |
| 12 | Tensão no Oriente Médio | Trading Economics (EUA pedem que países do Golfo se preparem para campanha contra o Irã; eleição em Israel) | confirmada | nenhuma |
| 13 | Fed decide juros dos EUA nesta quarta (28/10) | WSJ (paywall/401); busca não achou a matéria; calendário do FOMC (27-28/10) coerente | não confirmada na fonte | Marcar "não confirmado na fonte" ou trocar por fonte aberta (federalreserve.gov, calendário FOMC) |
| 14 | Rendimentos dos títulos americanos subiram antes da decisão | WSJ (só o slug do link sugere) | não confirmada | Mesma correção do item 13. O apuracao.md já marca PARCIAL |
| 15 | Itaú compra 100% da NeoSpace | Fato relevante (6-K no sec.gov): "all shares issued by NeoSpace" | confirmada | nenhuma |
| 16 | NeoSpace, startup brasileira de IA | Fato relevante | confirmada | nenhuma |
| 17 | R$ 2,9 bi, parte no fechamento e o resto em 5 anos | Fato relevante: BRL 2.925.000.000, parcela no fechamento e o restante em cinco anos | confirmada | Opcional: escrever R$ 2,925 bi |
| 18 | NeoSpace já treinava modelos com dados do banco havia quase dois anos | Fato relevante ("nearly two years") | confirmada | nenhuma |
| 19 | Depende do Cade e do Banco Central | Fato relevante | confirmada | nenhuma |
| 20 | 99Food: TJSP manteve condenação por concorrência desleal, por unanimidade | Startups (1ª Câmara Reservada de Direito Empresarial, por unanimidade) | confirmada | Incluir "segundo o iFood": a matéria diz que a informação foi divulgada pelo iFood |
| 21 | R$ 50 mil por dano moral | Startups | confirmada | nenhuma |
| 22 | Campanhas "Taxômetro" e "Respostas Bem Servidas" proibidas | Startups | confirmada | nenhuma |
| 23 | 99Food diz que não foi notificada | Startups | confirmada | nenhuma |
| 24 | "Na prática, publicidade comparativa com número 'estimado' vendido como fato custa caro" | Startups (tribunal: estimativa apresentada como fato) | confirmada como leitura da decisão | Está sob selo ⚖️, não sob `**Opinião:**`. Aceitável como "na prática" jurídico; se o manual exigir, rotular |
| 25 | Advent captou US$ 30 bi | NeoFeed (US$ 27 bi do GPE XI + mais de US$ 3 bi mid-market) | confirmada | nenhuma |
| 26 | Até 20% do fundo principal, cerca de US$ 6 bi, podem ir a outras regiões, entre elas o Brasil | NeoFeed diz "até 20% desse novo fundo ... US$ 6 bilhões" | confirmada com ressalva | 20% de US$ 27 bi (GPE XI) = US$ 5,4 bi; US$ 6 bi seria 20% de 30. Escrever "o NeoFeed calcula US$ 6 bi" ou "até 20% do GPE XI (US$ 27 bi)" |
| 27 | "É teto, não compromisso" | NeoFeed diz "até" | confirmada (inferência fiel) | nenhuma |
| 28 | Delaware: rascunho cria "AI Company", gerida por agente de IA | Ars Technica (Artificial Intelligence Company, AIC; draft bill) | confirmada | nenhuma |
| 29 | Sandbox de 30 meses | Ars Technica | confirmada | nenhuma |
| 30 | Dono não responde, salvo fraude, violação dolosa ou falta de capital | Ars Technica (op-ed e draft bill; há também exceção de ato fora do objeto social, "knew or should have known") | confirmada, incompleta | Opcional: citar a exceção do objeto social |
| 31 | Comer pediu documentos ao governador | Ars Technica (carta ao governador Matt Meyer) | confirmada | Opcional: dizer que Comer preside o Comitê de Supervisão da Câmara |
| 32 | Cerca de dois terços das Fortune 500 são de Delaware | Ars Technica ("about two-thirds") | confirmada | nenhuma |
| 33 | "Na prática, é a pergunta 'quem responde pelo agente?' virando forma societária" | interpretação | opinião sem selo `**Opinião:**`, mas é leitura sob ⚖️ | Mesmo ponto do item 24 |
| 34 | Bank of America avisou clientes por e-mail para não darem usuário e senha a agentes de IA | TechCrunch ("email blast"; confirmado por porta-voz) | confirmada | nenhuma |
| 35 | Cliente responde pelo que for feito com esse acesso | TechCrunch (e-mail: "you're responsible for activity resulting from that access") | confirmada | nenhuma |
| 36 | Meta: a partir de 12/11 o Pixel conta parte das compras no aparelho do cliente | PPC Land | confirmada | nenhuma |
| 37 | Ligado por padrão; dá para desligar no Events Manager | PPC Land | confirmada | Opcional: PPC Land cita limites (fora UE/Reino Unido, exige login), atribuídos ao MetricMaven e não à Meta |
| 38 | Conversões podem subir sem a venda mudar | PPC Land | confirmada | nenhuma |
| 39 | Escrita caiu de 34,1% para 21,4% (jul/2024 a set/2026) das mensagens de consumo | PPC Land (dados da OpenAI Signals v3.0, 26/10/2026) | confirmada | nenhuma |
| 40 | "Segundo a própria OpenAI" | PPC Land analisa os arquivos da OpenAI | confirmada, mas o link é secundário | Manual (14.1) prefere a fonte primária: citar a página OpenAI Signals, ou escrever "dados da OpenAI, analisados pelo PPC Land" |
| 41 | Amostra de 1 milhão de mensagens por mês | PPC Land | confirmada | nenhuma |
| 42 | Orientação prática subiu para 28,1% | PPC Land (26,1% para 28,1%) | confirmada | nenhuma |
| 43 | Busca de informação para 20,2% | PPC Land (tabela: 16,7% para 20,2%) | confirmada | nenhuma |
| 44 | Ajuda técnica caiu de 13,5% para 4,6% | PPC Land | confirmada | nenhuma |
| 45 | No trabalho nos EUA, "dar consultoria e aconselhar" foi de 5,5% a 9,0% em um ano | PPC Land (US, Q1 2025 a Q1 2026: "Provide consultation and advice to others" 5,5% para 9,0%) | confirmada | Aspas: é tradução do rótulo O*NET; trocar por "consultoria e aconselhamento" sem aspas, ou citar o rótulo original |
| 46 | Opinião: o ChatGPT vira conselheiro... | Opinião com selo `**Opinião:**` | ok (selo presente) | nenhuma |
| 47 | Lexifina: texto de Alan Yahya sobre histórico de versões das leis dos EUA como git; blog de empresa com produto | Lexifina (Alan Yahya, 28/10/2026, categoria Opinion) | confirmada | nenhuma |
| 48 | TechCrunch: OpenAI e Anthropic dizem que seus modelos refutaram a Hipótese do Tempo Exponencial; pesquisadores avaliam | TechCrunch, 27/10/2026 (OpenAI divulgou solução; a Anthropic soltou refutação própria horas depois; Williams organiza a resposta) | confirmada | Opcional: dizer que a Anthropic questionou se a OpenAI se baseou em trabalho anterior |
| 49 | Anthropic: Enveda, Claude achou os 11 problemas que humanos tinham achado em 1.061 páginas, e mais 7 | Anthropic (11 e sete; 1.061 páginas) | confirmada | Atribuição: o texto é da Anthropic ("Claude caught all 11 issues"), não "a Enveda diz". Trocar por "a Anthropic diz" |
| 50 | Números da própria Anthropic, trabalho pré-clínico | página da Anthropic | confirmada | nenhuma |
| 51 | Pergunta do dia | sem fato | n/a | nenhuma |

## Correções obrigatórias

1. **Fed/WSJ (itens 13 e 14):** não foi possível confirmar a matéria (paywall, busca sem resultado). Marcar como "não confirmado" ou substituir por fonte aberta (calendário do FOMC no federalreserve.gov); não afirmar que os rendimentos subiram sem fonte lida.
2. **Advent (item 26):** "cerca de US$ 6 bi" não bate com 20% do fundo principal (US$ 27 bi = US$ 5,4 bi). Atribuir o número ao NeoFeed ou corrigir.
3. **Enveda/Anthropic (item 49):** a afirmação vem da Anthropic, não da Enveda. Trocar "a Enveda diz" por "a Anthropic diz".
4. **99Food (item 20):** atribuir a notícia do julgamento ao iFood ("segundo o iFood"), porque a fonte é a divulgação do iFood.
5. **Brent (item 11):** a fonte traz 80,78% e 80,46%; usar "~80%" ou aceitar o valor ao vivo com a hora.
6. **STATS (itens 40 e 45):** link é de agregador (PPC Land) para dados da OpenAI; citar a fonte primária (OpenAI Signals) ou deixar explícito "analisado pelo PPC Land". Remover aspas de "dar consultoria e aconselhar" (tradução do rótulo, não citação).
7. **Opcional (itens 24 e 33):** as frases "Na prática" sob ⚖️ são interpretação sem `**Opinião:**`. Manter só se o manual aceitar o selo ⚖️ como marcação.

## Correções aplicadas pelo editor
- Parte 1: escopo da classe F; 'queima caixa' trocado pelo caixa operacional positivo e os US$ 417 bi; '8 GB' cortado do Nesta edição; ajustes descritos como no S-1; opinião com selo; 'testes ou uso real'; Opera atribuída ao TechCrunch; KV cache; modelos de decisão; português; 'provavelmente' na Taça.
- Parte 2: Fed trocado pelo calendário do Federal Reserve (WSJ não confirmado); Advent atribuída ao NeoFeed; Enveda atribuída à Anthropic; 99Food 'segundo o iFood'; Brent ~80%; STATS atribuído à OpenAI via PPC Land, sem aspas; frases ⚖️ com selo de opinião.
