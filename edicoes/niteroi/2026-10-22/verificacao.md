# Verificação de fatos: caderno Niterói, edição de 2026-10-22 (teste, formato sexta)

Entrega considerada: quinta, 22/10/2026, por volta das 13h30. Todos os 22 links foram abertos uma vez (200). Os dias da semana batem com as datas: 14/10 quarta, 20/10 terça, 21/10 quarta, 22/10 quinta, 23/10 sexta, 24/10 sábado, 25/10 domingo, 26/10 segunda, 27/10 terça, 28/10 quarta, 29/10 quinta, 30/10 sexta. Nenhum evento da agenda terá passado na hora da entrega.

Para o ISP, além da página citada (que é só o portal), baixei a base oficial `BaseMunicipioMensal.csv` do próprio portal (2,4 MB, só leitura, guardada fora do projeto) para conferir os números que a página da Prefeitura não traz. O alerta do Inmet foi lido direto do feed JSON citado (`/avisos/ativos`), não só da matéria secundária.

Resultado: 52 afirmações conferidas. 46 confirmadas, 4 corrigidas, 2 não confirmadas pela fonte. Há 5 correções obrigatórias (9 trocas de texto) e 10 ajustes recomendados.

## Tabela de afirmações

| # | Afirmação (edição) | Fonte | Status | Correção |
|---|---|---|---|---|
| 1 | Assunto "terça pode faltar água em niterói" e prévia "ônibus de graça no domingo" | Regra do manual (datas explícitas) | corrigida | Weekday sem data. Ver correção 1. |
| 2 | Cedae para o Sistema Imunana-Laranjal das 4h de terça (27/10) às 4h de quarta (28/10) | [Cedae](https://www.cedae.com.br/Noticias/detalhe/sistema-imunana-laranjal-cedae-faz-manutencao-anual-no-dia-27-de-outubro/id/1014): "das 4h de terça-feira (27/10) às 4h de quarta-feira (28/10)" | confirmada | |
| 3 | Niterói está entre as cidades atendidas | Cedae (lista São Gonçalo, Niterói, Itaboraí, Maricá, Paquetá) | confirmada | |
| 4 | Sistema atende cerca de 2 milhões de pessoas | Cedae: a ETA Laranjal "atende cerca de 2 milhões de pessoas"; Folha do Leste repete | confirmada | |
| 5 | "mais de quatro Niteróis" | Cedae (2 milhões) e [IBGE](https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/2022/variaveis/93?localidades=N6%5B3303302%5D) (481.749 hab., Censo 2022): 2.000.000 / 481.749 = 4,15 | confirmada | Cálculo correto. |
| 6 | Lista de afetados: Niterói, São Gonçalo, Itaboraí, Maricá (Inoã e Itaipuaçu), Paquetá | Cedae e Folha do Leste | confirmada | Ajuste recomendado: Itaboraí recebe só água bruta (R2). |
| 7 | A Cedae não diz quais bairros ficam sem água | Cedae e Folha do Leste (nenhum lista bairros; Folha diz que não são necessariamente todos os imóveis) | confirmada | |
| 8 | Águas do Rio prevê até 72 horas em São Gonçalo, Maricá e Paquetá | [Folha do Leste](https://folhadoleste.com.br/falta-de-agua-niteroi-27-outubro-cedae/): Águas do Rio, depois que a produção chegar a 100%; áreas: São Gonçalo, Inoã/Itaipuaçu, Paquetá | confirmada | |
| 9 | Em Niterói a distribuidora é a Águas de Niterói | Cedae e Folha do Leste | confirmada | |
| 10 | Águas de Niterói, até esta quinta (22/10), não tinha aviso próprio no site | [Site da Águas de Niterói](https://www.grupoaguasdobrasil.com.br/aguas-niteroi/): notícias mais recentes de 15/10, 08/10 e 29/09, nada sobre a parada | confirmada | Vale só para o momento da consulta (R3). |
| 11 | TL;DR: "A volta da água pode levar mais que isso" | Folha do Leste: retomada da produção não é água na torneira; o prazo de 72 h é da Águas do Rio e "não deve ser aplicado automaticamente" a Niterói | confirmada | Ajuste recomendado (R1): o texto não deixa claro que não há prazo para Niterói. |
| 12 | Na prática: encher caixa-d'água, guardar água em recipientes limpos, adiar lavagem de carro e calçada | Cedae recomenda reservar água e adiar tarefas que gastem muito; Folha do Leste lista as mesmas medidas | confirmada | O "segunda (26/10)" é recomendação da edição, razoável (o corte começa às 4h de terça). |
| 13 | 0800 723 1222 e WhatsApp (21) 97211-8064 | Folha do Leste e rodapé do site da Águas de Niterói (os dois números estão no HTML) | confirmada | |
| 14 | Eleição domingo (25/10): ônibus municipais gratuitos até a meia-noite | [Prefeitura](https://niteroi.rj.gov.br/niteroi-repetira-operacao-especial-para-transporte-publico-no-segundo-turno-das-eleicoes-no-domingo-25/): gratuidade por lei de 2022, "operação funcionará até às 00h" | confirmada | |
| 15 | Frequência de dia útil | Prefeitura: "frequência equivalente à de dias úteis" | confirmada | |
| 16 | Linhas circulares 62C (Caramujo–Santa Bárbara) e 28C (Vila Ipiranga–Ponto Cem Réis) | Prefeitura | confirmada | A fonte diz que as circulares rodam "durante o período de votação", e a edição não diz. Ver correção 5. |
| 17 | No 1º turno, 215 mil embarques | Prefeitura: 215.025 embarques | confirmada | |
| 18 | "três vezes a média dos domingos de agosto e setembro" | Prefeitura: "superou em aproximadamente 211%" a média de 69,2 mil; 215.025 / 69.200 = 3,1 | confirmada | |
| 19 | Renovação de matrícula 2027 até sexta (23/10), na escola onde o aluno já estuda | [Prefeitura](https://niteroi.rj.gov.br/rede-municipal-de-educacao-divulga-calendario-de-matriculas-para-2027/): renovação "até sexta-feira (23)", presencial, na unidade onde já está matriculado | confirmada | Falta "presencialmente" (R5). |
| 20 | Vaga nova na Educação Infantil: inscrição de 23 a 27/11 em niteroi.rj.gov.br/matriculas | Prefeitura: "de 23 a 27 de novembro, por meio do site niteroi.rj.gov.br/matriculas"; a página existe (200) | confirmada | |
| 21 | Aviso amarelo de tempestade do Inmet para Niterói **de sexta (23/10)** a domingo (25/10) | [Inmet, feed ativo](https://apiprevmet3.inmet.gov.br/avisos/ativos): há aviso amarelo "Tempestade" para Niterói **hoje, 22/10, das 09:25 às 23:59**, e também 23, 24 e 25/10. A matéria da A Seguir Niterói só cita sexta a domingo | corrigida | O aviso já está em vigor na quinta. Ver correção 2 (3 lugares). |
| 22 | Chuva de até 50 mm por dia (50 litros por metro quadrado) | Inmet: "20 e 30 mm/h ou até 50 mm/dia"; 1 mm = 1 L/m² (conversão da edição, correta) | confirmada | |
| 23 | Vento de 40 a 60 km/h e granizo; risco de alagamento baixo | Inmet: "ventos intensos (40-60 km/h), e queda de granizo. Baixo risco de... alagamentos" | confirmada | |
| 24 | Em rajadas, não se abrigue sob árvores; Defesa Civil: 199 | Inmet: instrução idêntica e "Defesa Civil (telefone 199)" | confirmada | |
| 25 | NitTrans fecha parcialmente a Av. Almirante Ary Parreiras, em Icaraí, entre a Av. Jornalista Alberto Francisco Torres e a Rua Ator Paulo Gustavo | [Enfoco](https://enfoco.com.br/noticias/regiao/niteroi/festa-de-sao-judas-tadeu-tera-missas-procissao-e-angu-a-baiana-em-niteroi-veja-mudancas-no-transito/) | confirmada | |
| 26 | Inverte o sentido da Rua Ator Paulo Gustavo entre a Joaquim Távora e a Ary Parreiras | Enfoco | confirmada | "dessa rua" é ambíguo (R4). |
| 27 | Vale das 8h de segunda (26/10) às 8h de quinta (29/10) | Enfoco: "entre as 8h da próxima segunda-feira (26) e as 8h de quinta-feira (29)" | confirmada | |
| 28 | Túnel do Tibau: obra de R$ 38 milhões começou na quarta (21/10) | [Prefeitura](https://niteroi.rj.gov.br/prefeitura-inicia-obras-para-recuperar-circulacao-de-agua-do-mar-na-lagoa-de-piratininga/) e [Folha do Leste](https://folhadoleste.com.br/obra-tunel-tibau-lagoa-piratininga-niteroi/) | confirmada | |
| 29 | Túnel construído pelo Estado há mais de 20 anos, desmoronamentos em 2018 e 2019 | Prefeitura e Folha do Leste ("entre 2018 e 2019") | confirmada | |
| 30 | A prefeitura diz que assumiu a obra diante da demora na recuperação | Prefeitura | confirmada | Atribuição correta. |
| 31 | Em 12 meses a entrada de água do mar mais que triplica; reduziria a mortandade de peixes | Prefeitura: prazo de 12 meses, "mais do que triplicar", objetivo de "reduzir o risco de mortandade" | confirmada | Atribuída à prefeitura e em condicional, sem adjetivo. |
| 32 | Prefeito assinou na terça (20/10) a desapropriação do teatro da Praça da República, fechado desde 1991 | [Prefeitura](https://niteroi.rj.gov.br/prefeito-rodrigo-neves-assina-decreto-de-desapropriacao-do-teatro-leopoldo-froes-e-anuncia-restauracao-para-2027/) (assinatura em 20/10; fechado desde 1991) e [A Seguir Niterói](https://aseguirniteroi.com.br/noticias/prefeitura-de-niteroi-oficializa-desapropriacao-para-reabrir-teatro-leopoldo-froes/) (Praça da República) | confirmada | A Seguir diz que o decreto foi publicado hoje, 22/10 (R8). |
| 33 | "A restauração deve começar no início de 2027" | Prefeitura: "previsão de início das obras no começo de 2027" | corrigida | É previsão da prefeitura, não fato. Ver correção 4. |
| 34 | O comunicado não informa custo nem indenização | Prefeitura e A Seguir: nenhum dos dois traz valor | confirmada | |
| 35 | Niterói teve 4 roubos de veículo em setembro, o menor número mensal da série do ISP | [Prefeitura](https://niteroi.rj.gov.br/niteroi-registra-menor-numero-da-serie-historica-do-isp-sobre-roubos-de-veiculos/): menor da série por município, iniciada em 2003; base do ISP confere (4 em 2026m09, antes o menor era 7) | confirmada | |
| 36 | "em agosto foram 9" | Não está na Prefeitura nem no portal citado. Base do ISP (`BaseMunicipioMensal.csv`): 9 em 2026m08 | confirmada | Só conferível na base; ver R6. |
| 37 | Jan–set, roubos de rua caíram 38,5% (559 casos, contra 909) | Prefeitura: 559 contra 909, redução de 38,5%; base do ISP confere | confirmada | |
| 38 | No estado a queda foi de 19,5% | Não está na Prefeitura (ela só traz o estado em roubo de veículo: alta de 3,6%). Cálculo na base do ISP: 35.927 contra 44.625 = -19,5% | confirmada | Número calculado pela edição, só reproduzível na base do ISP (R6). |
| 39 | Sex (23/10), 18h, Mercado Municipal, Centro: Festival Samba Niterói, com Dudu Nobre e Vou Zuar. Grátis | [Folha do Leste](https://folhadoleste.com.br/dudu-nobre-vou-zuar-show-gratuito-niteroi/): sexta (23), 18h, Mercado Municipal (R. Santo Antônio, 53), entrada gratuita | confirmada | |
| 40 | Sáb (24/10), a partir das 6h, Praia de Charitas: 3ª etapa do Super Paddle; primeira largada às 6h30; premiação às 15h | [Prefeitura](https://niteroi.rj.gov.br/niteroi-recebe-a-3a-etapa-do-super-paddle-na-praia-de-charitas-neste-sabado-24/) | confirmada | |
| 41 | Sáb (24/10), 9h às 12h, Campo de São Bento, Icaraí: dois anos do Niterói Inclusivo, música ao vivo, Feira Atípica. Grátis | [Prefeitura](https://niteroi.rj.gov.br/programa-niteroi-inclusivo-celebra-dois-anos-com-programacao-gratuita-no-campo-de-sao-bento-neste-sabado-24/) | confirmada | |
| 42 | Vassouras: aviso amarelo do Inmet vale lá também, **de sexta (23/10)** a domingo (25/10) | Inmet: "Vassouras - RJ" está nos avisos de 22, 23, 24 e 25/10 | corrigida | Começa quinta (22/10). Ver correção 2. |
| 43 | "Semana calma em Vassouras" | Nenhuma fonte citada além do Inmet; é afirmação de ausência | não confirmada | Não verificável por link. O manual (seção 7) permite a linha, mas só se a busca da semana não achou nada. |
| 44 | Seabourn Venture, primeiro navio da temporada 2026/27, chega terça (27/10) às 8h, sai às 15h, desembarque no píer do Centro | [Prefeitura de Búzios](https://buzios.rj.gov.br/errata-buzios-recebe-primeiro-navio-de-cruzeiro-da-temporada-2026-2027-no-dia-27-de-outubro/) | confirmada | A URL tem "errata"; li o texto atual, que bate com a edição. |
| 45 | Sexta (30/10), Swan Hellenic Vega, das 8h às 19h | Prefeitura de Búzios | confirmada | |
| 46 | A prefeitura prevê 105 escalas até abril de 2027 | Prefeitura de Búzios | confirmada | |
| 47 | "cerca de uma a cada dois dias" | Nenhuma fonte traz. É cálculo da edição, e a fonte só diz "até abril" (27/10 a 30/04 dá uma a cada 1,8 dia; a 15/04, uma a cada 1,6) | não confirmada | Número calculado pela edição, não confirmado pela fonte. Ver correção 3. |
| 48 | Audiência na Câmara (14/10): prefeitura quer coleta de lixo no Centro às 4h e varrição às 6h | [Prensa de Babel](https://prensadebabel.com.br/buzios-verao-restricoes-transito-limpeza-taxa-turistica/): audiência em quarta (14); secretário de Serviços Públicos; "previsão apresentada", sem data de início | confirmada | |
| 49 | Discute-se proibir ônibus de turismo e veículos de carga nos corredores principais, 8h às 10h e 16h às 18h | Prensa de Babel: "corredores principal e alternativo"; mesmos horários | confirmada | Ajuste de precisão em R7. |
| 50 | Taxa turística, arquivada no ano passado a pedido do próprio prefeito; nada virou regra | Prensa de Babel: projeto do prefeito arquivado a pedido dele no ano anterior; taxa exige nova iniciativa legislativa; restrições "sem publicação de novas regras" | confirmada | |
| 51 | Ponto facultativo de quarta (28/10) a sexta (30/10), pelo Dia do Servidor; urgência médica, limpeza urbana e Guarda Municipal em plantão | [Prefeitura de Búzios](https://buzios.rj.gov.br/prefeitura-de-buzios-decreta-ponto-facultativo-nos-dias-28-29-e-30-de-outubro-em-alusao-ao-dia-do-servidor-publico/) | confirmada | |
| 52 | Fecho "Até segunda." | Manual, seção 6 (sexta termina com "Até segunda.") | confirmada | |

## Regras de redação conferidas

- **Datas relativas e dias da semana:** todos batem. Só faltam datas no assunto, na prévia e em "4h de quarta" (correção 1).
- **Evento que já terá passado:** nenhum. O alerta do Inmet de quinta está em vigor agora (correção 2).
- **Adjetivo de assessoria:** nenhum virou fato. "Histórica", "importante", "referência", "emblemático" e "ultraluxo" ficaram de fora. As promessas do túnel e do teatro vêm com "a prefeitura diz" ou em condicional (o teatro precisa da correção 4).
- **Opinião sem selo:** não há opinião. "Planeje o trajeto" e "Atenção à volta" são orientação de serviço.
- **Corrida eleitoral:** nenhuma. O item da eleição traz só transporte, sem candidato, pesquisa ou campanha.
- **Crime:** só dado oficial do ISP, sem detalhe mórbido nem nome de suspeito.
- **Tamanho:** 882 palavras no corpo (meta de sexta: 550 a 900) e 203 na história (120 a 220). Com todas as correções obrigatórias fica perto de 886, e com todas as recomendadas, perto de 906. Se adotar tudo, corte algo no Búzios.

## Correções obrigatórias

Cada trecho abaixo aparece exatamente assim no `edicao.md`.

**1. Datas explícitas no assunto, na prévia e na história (manual, seção 2 e checklist)**

- Trocar `assunto: "terça pode faltar água em niterói"` por `assunto: "terça (27/10) pode faltar água em niterói"`
- Trocar `previa: "+ ônibus de graça no domingo, mas com aviso de tempestade"` por `previa: "+ ônibus de graça no domingo (25/10), mas com aviso de tempestade"`
- Trocar `Atenção à volta: 4h de quarta não garante água na torneira.` por `Atenção à volta: 4h de quarta (28/10) não garante água na torneira.`

**2. O aviso do Inmet já está em vigor hoje, quinta (22/10), desde as 9h25. A edição diz que começa na sexta (3 lugares)**

- Front matter. Trocar `titulo: "Inmet mantém aviso amarelo de tempestade de sexta (23/10) a domingo (25/10)"` por `titulo: "Inmet mantém aviso amarelo de tempestade de quinta (22/10) a domingo (25/10)"`. O `id` (`aviso-tempestade-inmet-23-25-out`) pode ficar, ou virar `aviso-tempestade-inmet-22-25-out`.
- Serviço, Tempo. Trocar `→ **Tempo:** aviso amarelo de tempestade do Inmet para Niterói de sexta (23/10) a domingo (25/10), com chuva` por `→ **Tempo:** aviso amarelo de tempestade do Inmet para Niterói, em vigor desde as 9h25 desta quinta (22/10) e válido até domingo (25/10), com chuva`
- Vassouras. Trocar `vale lá também, de sexta (23/10) a domingo (25/10)` por `vale lá também, de quinta (22/10) a domingo (25/10)`

**3. Cruzeiros: número calculado pela edição, que a fonte não traz (não confirmado pela fonte)**

- Trocar `**105** escalas até abril de 2027, cerca de uma a cada dois dias (` por `**105** escalas até abril de 2027 (`

**4. Teatro Leopoldo Fróes: previsão da prefeitura apresentada como fato (manual, seção 4)**

- Trocar `A restauração deve começar no início de 2027;` por `A prefeitura prevê começar a restauração no início de 2027;`

**5. Serviço da eleição sem o "quando" das linhas circulares**

A fonte diz que as circulares rodam só durante a votação. A edição dá a impressão de que valem até a meia-noite.

- Trocar `Duas linhas circulares atendem quem mudou de local de votação:` por `Durante a votação, duas linhas circulares atendem quem mudou de local de votação:`

## Ajustes recomendados (não obrigatórios)

- **R1. TL;DR da água.** Trocar `A volta da água pode levar mais que isso.` por `A volta da água pode levar mais que isso; a concessionária de Niterói ainda não deu prazo.` O corpo já separa os 72 h da Águas do Rio, mas o TL;DR não.
- **R2. Itaboraí.** Trocar `Niterói, São Gonçalo, Itaboraí, Maricá (Inoã e Itaipuaçu)` por `Niterói, São Gonçalo, Itaboraí (só água bruta), Maricá (Inoã e Itaipuaçu)`. Cedae e Folha do Leste dizem que Itaboraí recebe só água bruta.
- **R3. Aviso da Águas de Niterói.** Trocar `que até esta quinta (22/10) não tinha aviso próprio em seu site` por `que, até o fechamento desta edição, não tinha aviso próprio em seu site`. A afirmação vale só para o momento da consulta e pode envelhecer entre a checagem e as 13h30.
- **R4. São Judas.** Trocar `e inverte o sentido dessa rua entre` por `e inverte o sentido da Rua Ator Paulo Gustavo entre`. A fonte é a Enfoco (secundária). Se a NitTrans ou a Prefeitura publicou o aviso, usar o link dela (manual, seção 4). Não verifiquei se existe.
- **R5. Matrícula.** Trocar `na escola onde o aluno já estuda` por `presencialmente, na escola onde o aluno já estuda`.
- **R6. ISP.** O "agosto foram 9" e o "19,5%" do estado não aparecem na página da Prefeitura nem na do portal. Conferem na base `BaseMunicipioMensal.csv`. Trocar `enquanto no estado a queda foi de **19,5%**` por `enquanto no estado a queda, pelos dados do ISP, foi de **19,5%**`.
- **R7. Búzios, trânsito.** Trocar `nos corredores principais em horário de pico` por `nos corredores principal e alternativo em horário de pico`.
- **R8. Teatro.** Acrescentar que o decreto saiu no Diário Oficial hoje (22/10), segundo a A Seguir Niterói. A edição só diz "assinou na terça (20/10)", que está certo.
- **R9. Vassouras.** "Semana calma em Vassouras" não tem fonte. Só mantenha se a busca da semana (patrimônio, festivais, RJ-127, RJ-143, universidade) não achou nada.
- **R10. Eleição.** Trocar `→ **Eleição, domingo (25/10):**` por `→ **Eleição, 2º turno, domingo (25/10):**`, para o leitor saber qual votação é.
