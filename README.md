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
| Ambiente "Default" | claude.ai/code → botão do ambiente embaixo da caixa de mensagem → engrenagem | Rede **Full** (para ler os sites de notícia), as variáveis `EMAIL_DESTINO` e `RESEND_VIA_PROXY=1` e o *network secret* do Resend. |
| Rotina | https://claude.ai/code/routines | Roda toda madrugada e segue o `manual/ROTINA.md`. |
| Resend | https://resend.com | Entrega o e-mail. A chave fica guardada no *network secret*, e a rotina usa sem enxergar. |

**O que fica fora do GitHub (de propósito):** o seu e-mail e a chave do Resend. No Mac, os dois ficam em `chave_resend.txt`, que o git ignora.

### Tarefas comuns
- **Pausar a newsletter:** em claude.ai/code/routines, abra a rotina e desligue a chave no topo. Para ligar de novo, é a mesma chave.
- **Gerar uma edição agora:** na mesma página, clique em **Run now**.
- **Ver o que a rotina fez:** cada execução aparece na lista da rotina. Clique nela para ver a conversa inteira. Verde só quer dizer que rodou, então confira o resultado lá dentro.
- **Mudar o horário:** peça ao Claude ("muda a rotina da newsletter para começar às 4h"). O cron da rotina usa o horário de Londres (UTC), que fica 3 h à frente de Brasília.
- **Trocar a chave do Resend:** crie uma chave nova no Resend. No ambiente, apague o secret antigo e adicione o novo: Bearer, `api.resend.com`, `Authorization`.
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

| Caderno | Quando sai | Fontes | Manual e roteiro |
|---|---|---|---|
| **Mercado** | Dias úteis, de manhã. Sai também uma **edição extra** quando o pregão tem gatilho (ver o manual). | `fontes_mercado.yaml` + o painel de cotações (B3, CNBC, AwesomeAPI, CNN, alternative.me) | `manual/MANUAL_MERCADO.md` e `manual/ROTINA_MERCADO.md` |
| **Niterói** | Segunda, quarta e sexta, de manhã. Na sexta, traz também o **bloco semanal de Vassouras e Búzios**. | `fontes_niteroi.yaml` (prefeituras, NitTrans, Águas de Niterói e a imprensa local) | `manual/MANUAL_NITEROI.md` e `manual/ROTINA_NITEROI.md` |
| **IA** | Segunda e quinta, de manhã. Vai mais fundo que a geral: o que mudou de verdade, modelos novos, open source, ferramentas e agentes, regulação e o IA na prática. | `fontes_ia.yaml` (laboratórios, open source, ferramentas, regulação, China e Brasil) + Hacker News, GitHub em alta, Hugging Face e Reddit | `manual/MANUAL_IA.md` e `manual/ROTINA_IA.md` |

**Como funciona por dentro:**
- As edições de um caderno ficam em `edicoes/<caderno>/AAAA-MM-DD/`. A edição extra fica em `AAAA-MM-DD-extra/`.
- No site, cada caderno tem o próprio arquivo (por exemplo, `docs/mercado.html`), com links entre a geral e os cadernos.
- O histórico (`dados/historico.json`) é um só. Cada caderno tem a própria numeração e vê o que os outros publicaram, para não repetir.
- Todos os comandos aceitam `--caderno`. Por exemplo: `python main.py montar 2026-10-22 --caderno mercado`.
- No `fontes_niteroi.yaml`, cada fonte pode ter um **filtro** (só entram as notícias que citam a cidade), uma **janela própria** (o bloco de Vassouras e Búzios olha a semana inteira) e **páginas** (quantas páginas do feed ler, para prefeituras que publicam muito).
- No Mercado, os números do painel vêm de `python main.py mercado-painel` e entram na edição por código, sem passar pela IA. O `python main.py mercado-alarme` confere os gatilhos da edição extra.
- No IA, o caderno não repete a geral: antes da pauta, ele lê o que a geral publicou desde a última edição e só volta a um assunto com valor novo (manual, seção 2). Quando a busca do GitHub falha (na nuvem ela dá 403), o "GitHub em alta" usa a página de tendências do GitHub. E, no filtro de fonte, palavra de até 3 letras (como "IA") só conta inteira, para não pegar "dia" ou "mídia".

**Para pausar só o e-mail de um caderno:** troque `envio: ligado` por `envio: desligado` no bloco dele, em `cadernos.yaml`.
