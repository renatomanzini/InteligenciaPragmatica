# Inteligência Pragmática

Newsletter diária sobre IA, economia, negócios e marketing, escrita por IA só para você. Ela chega às 06:30.

Este guia explica como manter a newsletter funcionando sem precisar programar.

---

## 1. Como funciona, em uma frase
Toda madrugada, um Claude roda na nuvem da Anthropic e faz o trabalho todo. Seu Mac pode estar desligado.
1. Lê as fontes.
2. Escolhe o que importa para você.
3. Apura cada fato na fonte original.
4. Escreve a edição.
5. Manda um revisor independente conferir tudo.
6. Agenda o e-mail para as 06:30.

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
> *Esta seção vai ser preenchida na fase 1b, depois que você aprovar as edições de teste. Ela vai ter o passo a passo para criar a conta no GitHub e no Resend e para ligar a rotina.*

## 6. Problemas comuns
- **O e-mail não chegou:**
  - Olhe a pasta Spam ou Promoções.
  - Confira que o `config.yaml` está com `envio: ligado`.
  - Veja se a rotina rodou em [claude.ai/code/routines](https://claude.ai/code/routines). Clique na execução do dia e leia o que aconteceu.
- **Uma fonte parou de funcionar:** a coleta registra o problema em `dados/candidatos/AAAA-MM-DD-fontes.log`. Pause a fonte no `fontes.yaml` ou peça ao Claude para achar o endereço novo.
- **A edição veio com algo errado:** abra o `verificacao.md` daquele dia para ver o que o revisor conferiu, e me conte o erro. Dá para virar regra no manual.
