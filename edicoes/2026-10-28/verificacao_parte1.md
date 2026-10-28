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
