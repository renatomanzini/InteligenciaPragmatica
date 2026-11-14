# Verificação parte 2 (SERVIÇO e AGENDA), edição de sáb 14/11/2026

Fontes abertas e lidas (curl). Calendário: 14/11/2026 é sábado, 15/11 é domingo (feriado), 13/11 é sexta. Os dias da semana batem.

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Niterói não tem caso confirmado de sarampo | Folha do Leste: "a cidade não registre casos confirmados" | confirmada | nenhuma |
| "segundo o balanço da prefeitura de sexta (13/11)" | Folha do Leste: a prefeitura "reforçou nesta sexta, 13/11, o alerta de prevenção". Não fala em balanço nem em número | não confirmada (palavra "balanço") | trocar por "segundo a prefeitura, em alerta de sexta (13/11)" |
| A vigilância continua | "a Secretaria Municipal de Saúde mantém a vigilância" | confirmada | nenhuma |
| Vacina gratuita, segunda a sexta, 8h às 17h, policlínicas, UBS e módulos do Médico de Família | idem, "de segunda a sexta-feira, das 8h às 17h" | confirmada | falta data explícita: hoje é sábado e não há vacina hoje nem domingo; dizer "a partir de segunda (16/11)" |
| Levar a caderneta, se tiver | "levar a caderneta de vacinação, caso esteja disponível" | confirmada | nenhuma |
| Crianças e jovens até 29 anos (duas doses); adultos de 30 a 59 (ao menos uma dose); quem vai viajar | tabela do Ministério da Saúde na matéria | confirmada | "vale conferir" é vago: dizer "duas doses até 29 anos" |
| "Gestante precisa de avaliação antes" | Fonte: tríplice viral "contraindicada durante a gestação" e "gestantes ... precisam de avaliação específica" | confirmada, mas suaviza uma contraindicação | ver correção 3 |
| Link do serviço é Folha do Leste | O manual (seção 9) pede o link da fonte primária. A própria matéria cita o portal da Secretaria de Saúde, sem URL | não confirmada (fonte secundária) | se o agente achar a página da prefeitura, trocar; senão manter e dizer "segundo a prefeitura" |
| Rótulo "Saúde · Sarampo" | manual: rótulo `→ **Saúde**:` | confirmada (Niterói, cidade certa) | nenhuma |
| Sáb (14/11), 17h, Praça Luiz Gomes da Silva, Piratininga: Tiago Iorc, com Celso Fonseca e Aprendiz Musical, grátis | Folha do Leste: "A partir das 17h, o público poderá acompanhar apresentações do Aprendiz Musical, Celso Fonseca e Tiago Iorc"; lista: "Sábado (14), a partir das 17h ... Gratuito" | errada em parte | 17h é a abertura, não o horário do Iorc (que aparece por último). Ver correção 1 |
| Dom (15/11), 15h, Praça Luiz Gomes da Silva: Barão Vermelho, com Gui Schwab, grátis | Folha do Leste: "No domingo, 15/11, a programação musical começa às 15h, com apresentações anunciadas de Gui Schwab e Barão Vermelho" | errada em parte | 15h é o início da programação, não o show do Barão. Ver correção 2 |
| "O horário foi 'anunciado' e pode mudar" | A fonte diz "apresentações anunciadas" (as atrações), não o horário. "pode mudar" é inferência | errada (citação truncada e deturpada) | ver correção 2 |
| Sáb e dom, 9h às 17h, Casa da Amizade, Charitas: 41ª Exposição de Orquídeas, grátis | Enfoco, 13/11 10h12: "sábado (14) e domingo (15) ... Casa da Amizade, em Charitas, das 9h às 17h, com entrada gratuita" | confirmada | opcional: dizer que tem venda de plantas e palestras gratuitas |
| Búzios, dom (15/11): missa campal 18h, Adriana Arydes 20h, Banda Herança de Deus 21h30, Praça da Tia Uia, Rasa, grátis | Prensa de Babel: "No domingo (15), o encerramento terá missa campal às 18h, show da cantora católica Adriana Arydes, às 20h, e apresentação da Banda Herança de Deus, às 21h30", "entrada gratuita" | confirmada | opcional: dizer que é o encerramento dos 31 anos de Búzios. Cidade certa (Búzios no rótulo) |
| Datas relativas, adjetivos de assessoria, opinião sem selo | Nenhuma encontrada em SERVIÇO e AGENDA | confirmada | nenhuma |
| Algum evento já passado na hora da entrega | Todos são de sábado à tarde em diante ou de domingo; nenhum terá passado de manhã. O sarampo só funciona a partir de segunda | confirmada | nenhuma além da data do sarampo |

## Correções obrigatórias

1. Agenda, Tiago Iorc. Trocar
`→ **Sáb (14/11), 17h · Praça Luiz Gomes da Silva, Piratininga**: Tiago Iorc, com Celso Fonseca e Aprendiz Musical. Grátis.`
por
`→ **Sáb (14/11), a partir das 17h · Praça Luiz Gomes da Silva, Piratininga**: Aprendiz Musical, Celso Fonseca e Tiago Iorc. Grátis. A fonte não traz o horário de cada um.`

2. Agenda, Barão Vermelho. Trocar
`→ **Dom (15/11), 15h · Praça Luiz Gomes da Silva, Piratininga**: Barão Vermelho, com Gui Schwab. Grátis. O horário foi "anunciado" e pode mudar.`
por
`→ **Dom (15/11), a partir das 15h · Praça Luiz Gomes da Silva, Piratininga**: Gui Schwab e Barão Vermelho, atrações anunciadas pela prefeitura. Grátis. A fonte não traz o horário de cada um.`

3. Serviço, sarampo. Trocar
`Niterói não tem caso confirmado, segundo o balanço da prefeitura de sexta (13/11), mas a vigilância continua. A vacina é gratuita, de segunda a sexta, das 8h às 17h, nas policlínicas, nas UBS e nos módulos do Médico de Família; leve a caderneta, se tiver. Vale conferir a vacinação de crianças e jovens até 29 anos, de adultos de 30 a 59 (ao menos uma dose) e de quem vai viajar. Gestante precisa de avaliação antes.`
por
`Niterói não tem caso confirmado, segundo a prefeitura, que reforçou o alerta na sexta (13/11) e mantém a vigilância. A vacina é gratuita, de segunda a sexta, das 8h às 17h (a próxima chance é segunda, 16/11), nas policlínicas, nas UBS e nos módulos do Médico de Família; leve a caderneta, se tiver. Confira a caderneta: até 29 anos são duas doses, de 30 a 59 anos pelo menos uma, e vale também para quem vai viajar. Gestante não deve tomar a tríplice viral sem avaliação médica (é contraindicada na gravidez).`
Nota: "Folha do Leste" é link secundário; se houver a página da prefeitura, usar como link do serviço.
