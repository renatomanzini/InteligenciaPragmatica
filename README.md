# Inteligência Pragmática

Newsletter diária sobre IA, economia, negócios e marketing, escrita por IA só para você. Ela chega às 06:00, junto com os cadernos do dia.

Este guia explica como manter a newsletter funcionando sem precisar programar.

---

## 1. Como funciona, em uma frase
Toda madrugada, um Claude roda na nuvem da Anthropic e faz o trabalho todo. Seu Mac pode estar desligado.
1. Lê as fontes.
2. Escolhe o que importa para você.
3. Apura cada fato na fonte original.
4. Escreve a edição.
5. Manda um revisor independente conferir tudo.
6. Deixa a edição pronta e publicada. Às 06:00, uma rotina de envio manda todas as newsletters do dia juntas.

O passo a passo que ele segue está em `manual/ROTINA.md`, e as regras de estilo e de rigor em `manual/MANUAL_DE_REDACAO.md`.

## 2. Os 3 arquivos que você pode editar sem medo
São arquivos de texto. Abra com o TextEdit ou edite direto no site do GitHub.

| Arquivo | Para quê | Exemplo |
|---|---|---|
| `preferencias.md` | O que você gosta e o que não gosta. **É aqui que entra o feedback.** | Em "Feedback recebido", escreva no topo: `2026-10-20 — mais disso: legaltechs brasileiras` |
| `fontes.yaml` | As fontes que a coleta lê. | Para pausar uma fonte, troque `ativo: true` por `ativo: false` |
| `config.yaml` | Configurações gerais. | `envio: ligado` ou `envio: desligado` |

A rotina relê esses arquivos toda madrugada, então a mudança vale a partir da edição seguinte.

## 3. Rodar no seu Mac (para testar)
Abra o **Terminal** (Cmd + Espaço, digite "Terminal", Enter) e cole um comando por vez:

```bash
cd ~/InteligenciaPragmatica
```

Para ver a coleta de hoje e a última edição no navegador, sem enviar nada:
```bash
.venv/bin/python main.py --dry-run
```

**Outros comandos úteis:**

| Comando | O que faz |
|---|---|
| `.venv/bin/python main.py coletar` | Junta os candidatos do dia em `dados/candidatos/` |
| `.venv/bin/python main.py historico` | Mostra as últimas edições e as histórias em andamento |
| `.venv/bin/python main.py montar` | Gera o e-mail e o site da edição mais recente |
| `.venv/bin/python main.py links` | Testa todos os links da edição mais recente |
| `.venv/bin/python main.py github dono/repo` | Mostra as estrelas e a data de um repositório do GitHub |

## 4. Onde ficam as coisas
- `edicoes/AAAA-MM-DD/` guarda cada edição:
  - `edicao.md`: o texto;
  - `email.html`: o e-mail;
  - `curta.txt`: a versão curta para mensageiro;
  - `pauta.md`: por que cada notícia entrou ou saiu;
  - `verificacao.md`: **o log de checagem**, com cada afirmação, a fonte e se foi confirmada.
- `docs/` é o site com todas as edições, que pode ser instalado no celular.
- `dados/historico.json` é a memória da newsletter: o que já saiu e as histórias em andamento.

## 5. Configuração da nuvem
Está tudo montado. Esta seção serve para você saber onde fica cada peça e como mexer nela.

| Peça | Onde fica | Para quê |
|---|---|---|
| Repositório | https://github.com/renatomanzini/InteligenciaPragmatica | Guarda o código, as edições e o histórico. É público. |
| Site | https://renatomanzini.github.io/InteligenciaPragmatica/ | O arquivo de todas as edições, que dá para instalar no celular como app. |
| App do Claude no GitHub | github.com → Settings → Applications → Claude | Deixa a rotina ler e gravar **só** neste repositório. |
| Ambiente "Default" | claude.ai/code → botão do ambiente embaixo da caixa de mensagem → engrenagem | Rede **Full** (para ler os sites de notícia), as variáveis `EMAIL_DESTINO`, `RESEND_VIA_PROXY=1` e `GITHUB_TOKEN_LEITURA` e o *network secret* do Resend. |
| Rotina | https://claude.ai/code/routines | Roda toda madrugada e segue o `manual/ROTINA.md`. |
| Resend | https://resend.com | Entrega o e-mail. A chave fica guardada no *network secret*, e a rotina usa sem enxergar. |

**O que fica fora do GitHub (de propósito):** o seu e-mail e a chave do Resend. No Mac, os dois ficam em `chave_resend.txt`, que o git ignora.

### Tarefas comuns
- **Pausar a newsletter:** em claude.ai/code/routines, abra a rotina e desligue a chave no topo. Para ligar de novo, é a mesma chave.
- **Gerar uma edição agora:** na mesma página, clique em **Run now**.
- **Ver o que a rotina fez:** cada execução aparece na lista da rotina. Clique nela para ver a conversa inteira. Verde só quer dizer que rodou, então confira o resultado lá dentro.
- **Mudar o horário:** peça ao Claude ("muda a rotina da newsletter para começar às 4h"). O cron da rotina usa o horário de Londres (UTC), que fica 3 h à frente de Brasília.
- **Trocar a chave do Resend:** crie uma chave nova no Resend. No ambiente, apague o secret antigo e adicione o novo: Bearer, `api.resend.com`, `Authorization`.
- **Trocar a chave do GitHub** (`GITHUB_TOKEN_LEITURA`, que dá as estrelas e o GitHub em alta na nuvem): em github.com/settings/personal-access-tokens, crie ou regenere a chave "Inteligencia Pragmatica - leitura", só com **Public repositories** e sem permissões. No ambiente, troque o valor da linha `GITHUB_TOKEN_LEITURA=`. Ela fica numa variável, e não num *network secret*, porque a nuvem nunca anexa secret a pedidos ao GitHub. Por isso a chave só lê o que é público.
- **Parar só o e-mail** (a edição continua saindo no site): troque `envio: ligado` por `envio: desligado` no `config.yaml`.
- **Quanto da assinatura isso gasta:** veja em https://claude.ai/settings/usage. A rotina usa o mesmo limite das suas conversas com o Claude.

## 6. Problemas comuns
- **O e-mail não chegou:**
  - Olhe a pasta Spam ou Promoções.
  - Confira que o `config.yaml` está com `envio: ligado`.
  - Veja se a rotina rodou em [claude.ai/code/routines](https://claude.ai/code/routines). Clique na execução do dia e leia o que aconteceu.
- **Uma fonte parou de funcionar:** a coleta registra o problema em `dados/candidatos/AAAA-MM-DD-fontes.log`. Pause a fonte no `fontes.yaml` ou peça ao Claude para achar o endereço novo.
- **A edição veio com algo errado:** abra o `verificacao.md` daquele dia para ver o que o revisor conferiu, e me conte o erro. Dá para virar regra no manual.

## 7. Cadernos (newsletters especializadas)
Além da geral, o projeto tem **cadernos**: newsletters com tema, frequência e site próprios. A lista está em `cadernos.yaml`.

**O desenho de hoje** (reorganizado em 22/10/2026 para gastar menos da assinatura):

| Newsletter | Quando sai | Quem escreve | Fontes | Manual e roteiro |
|---|---|---|---|---|
| **Geral** | Todos os dias, às 06:00. Na **terça e na quinta**, traz também a seção **MARKETING DIGITAL** (plataformas, tráfego e busca, criadores, um case e o "como isso vira serviço"). | **O Opus planeja, o Sonnet escreve.** O Opus faz a triagem, a pauta e a apuração (de 2 a 4 agentes Sonnet) e escreve um plano de redação detalhado. Um agente Sonnet escreve a edição, e o Opus revisa. Dois checadores Sonnet conferem tudo. | `fontes.yaml` (as fontes de marketing estão lá, no tema marketing) | `manual/MANUAL_DE_REDACAO.md` (marketing na seção 17) e `manual/ROTINA.md` |
| **Mercado e Economia** | Dias úteis, de manhã. Nas **segundas, quartas e sextas**, a edição ganha o bloco **ECONOMIA**: o painel oficial do Banco Central e do IBGE, o Brasil (macro), empresas e preços (micro), o mundo e um explicador. Sai também uma **edição extra** à noite, quando o pregão tem gatilho (o alarme das 18:37 continua). | Opus, com dois checadores Sonnet | `fontes_mercado.yaml` (as fontes da Economia estão lá) + o painel de cotações (B3, CNBC, AwesomeAPI, CNN, alternative.me) + o painel oficial do BC e do IBGE | `manual/MANUAL_MERCADO.md` (a Economia na seção 9) e `manual/ROTINA_MERCADO.md` |
| **Niterói** | **Segunda, quarta e sexta**, de manhã, com a edição completa (na sexta, com o bloco semanal de Vassouras e Búzios). **Terça, quinta, sábado e domingo**, só um **radar**: lê os títulos e publica uma edição extra se houver aviso urgente (falta d'água, interdição, alerta da Defesa Civil, prazo que vence). Sem aviso, não faz nada. | Segunda, quarta e sexta: **Sonnet**, com dois checadores Sonnet. Radar: **Haiku**, que chama um Sonnet para escrever e outro para conferir só se houver urgência. | `fontes_niteroi.yaml` (prefeituras, NitTrans, Águas de Niterói e a imprensa local) | `manual/MANUAL_NITEROI.md` e `manual/ROTINA_NITEROI.md` |

**Encerrados em 22/10/2026:**
- **Economia** virou o bloco do Mercado.
- **Marketing** virou a seção da geral.
- **IA** deixou de existir como caderno, porque a geral já cobre IA todo dia.

As edições antigas e as páginas deles continuam no site. O `envio: desligado` deles está no `cadernos.yaml`, e os manuais e as fontes ficam só como histórico. Para trazer um caderno de volta, é preciso ligar o envio de novo e criar a rotina dele.

**O envio é junto, às 06:00.** As rotinas de redação rodam de madrugada e deixam a edição pronta e publicada. Às 06:00, a rotina de envio (`python main.py enviar-pendentes`) manda tudo o que ficou pendente. A edição extra do Mercado (18:37) sai na hora.

**Como funciona por dentro:**
- As edições de um caderno ficam em `edicoes/<caderno>/AAAA-MM-DD/`. A edição extra do Mercado fica em `AAAA-MM-DD-extra/`. A extra do Niterói fica na pasta do dia, com `tipo: extra`, para a rotina de envio das 06:00 achá-la.
- No site, cada caderno tem o próprio arquivo (por exemplo, `docs/mercado.html`), com links entre a geral e os cadernos (os encerrados também, para ler as edições antigas).
- O histórico (`dados/historico.json`) é um só. Cada caderno tem a própria numeração e vê o que os outros publicaram, para não repetir.
- Todos os comandos aceitam `--caderno`. Por exemplo: `python main.py montar 2026-10-22 --caderno mercado`.
- Na coleta, o `janela_horas` do arquivo de fontes diz quantas horas olhar para trás. Aceita `padrao` e o nome de um dia (`segunda`, `terca`, `quarta`, `quinta`, `sexta`, `sabado`, `domingo`), e uma fonte pode ter a janela dela, como número ou como esse mesmo dicionário. No Niterói, a edição olha 48 horas (72 na segunda), e o radar olha 30.
- No `fontes_niteroi.yaml`, cada fonte pode ter um **filtro** (só entram as notícias que citam a cidade), uma **janela própria** (o bloco de Vassouras e Búzios olha a semana inteira) e **páginas** (quantas páginas do feed ler, para prefeituras que publicam muito).
- No Mercado, os números do painel de cotações vêm de `python main.py mercado-painel` e entram na edição por código, sem passar pela IA. O `python main.py mercado-alarme` confere os gatilhos da edição extra.
- No bloco ECONOMIA do Mercado, os números oficiais (Selic, IPCA, PIB, desemprego, dívida e Focus) vêm de `python main.py economia-painel AAAA-MM-DD --caderno mercado`, direto das APIs do Banco Central e do IBGE, e entram na edição por código, no lugar do marcador `<!-- painel-economia -->`. O 🆕 marca o dado que saiu desde o bloco anterior. O mesmo comando grava `oficiais.md`, com os releases e a agenda do IBGE, para a pauta. O `--caderno mercado` é o padrão; com `--caderno economia`, o comando grava na pasta do caderno Economia, encerrado (o jeito antigo).
- A coleta de "GitHub em alta" usa a página de tendências do GitHub quando a busca dá 403 (na nuvem, ela dá). E, no filtro de fonte, palavra de até 3 letras (como "IA") só conta inteira, para não pegar "dia" ou "mídia".
- **Cadernos com dias fixos** (`dias_envio` no bloco do caderno, em `cadernos.yaml`): o `python main.py historico --caderno X` diz se hoje é dia fixo e a data da última edição.

**Para pausar só o e-mail de um caderno:** troque `envio: ligado` por `envio: desligado` no bloco dele, em `cadernos.yaml`.
