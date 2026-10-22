"""Montagem: edicao.md → email.html, curta.txt e site PWA em docs/."""
import html
import json
import re
import struct
import zlib
from datetime import date
from math import ceil
from pathlib import Path
from typing import List, Tuple

import markdown

from . import cadernos
from .util import data_por_extenso, ler_front_matter

NOME_PADRAO = "Inteligência Pragmática"
MARCA_PAINEL = "<!-- painel -->"
RODAPE_IA = "Feita por IA para um leitor só. Fontes linkadas em cada afirmação."
LIMITE_CURTA = 900

# Paleta (claro). No escuro, o destaque clareia para manter o contraste.
C_FUNDO = "#FAF8F5"
C_TEXTO = "#1F1F1F"
C_DEST = "#0F5C6E"
C_SEC = "#6B6B6B"
C_LINHA = "#E3DED6"
C_CAIXA = "#E6F0F2"

F_CORPO = "-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
F_TITULO = "Georgia,'Times New Roman',serif"


# ───────────────────────── assunto ─────────────────────────

_RE_TACHADO = re.compile(r"~~(?=\S)(.+?)(?<=\S)~~")


def assunto_html(texto: str) -> str:
    """Assunto escapado, com ~~x~~ virando <del>x</del>."""
    return _RE_TACHADO.sub(r"<del>\1</del>", html.escape(str(texto or ""), quote=False))


def assunto_sem_marcas(texto: str) -> str:
    """Assunto puro: tira os ~~ e mantém o texto."""
    return _RE_TACHADO.sub(r"\1", str(texto or ""))


def assunto_tachado(texto: str) -> str:
    """Para texto puro (assunto de e-mail, curta.txt): ~~x~~ vira x com U+0336 em cada letra."""
    def riscar(m):
        return "".join(c if c.isspace() else c + "̶" for c in m.group(1))
    return _RE_TACHADO.sub(riscar, str(texto or ""))


# ───────────────────────── Markdown → HTML ─────────────────────────

_RE_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+")


def _tipo_linha(linha: str) -> str:
    s = linha.strip()
    recuo = len(linha) - len(linha.lstrip(" "))
    if not s:
        return "branco"
    if recuo >= 4 or linha.startswith("\t"):
        return "continuacao"
    if re.match(r"^#{1,6}\s", s):
        return "titulo"
    if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
        return "hr"
    if re.match(r"^→\s", s):
        return "seta"
    if re.match(r"^🔗\s", s):
        return "fonte"
    if s.startswith(">"):
        return "citacao"
    if _RE_ITEM.match(linha):
        return "item"
    return "texto"


def _preparar_markdown(corpo: str) -> str:
    """Põe linhas em branco onde o Markdown exige e converte o tachado em <del>.

    Cada título, `---`, linha `→` e linha `🔗` vira bloco próprio; citações e listas
    ganham a linha em branco que o Markdown pede antes e depois.
    """
    saida: List[str] = []
    anterior = "branco"
    em_codigo = False
    for linha in corpo.replace("\r\n", "\n").split("\n"):
        if linha.strip().startswith("```"):
            em_codigo = not em_codigo
            saida.append(linha)
            anterior = "codigo"
            continue
        if em_codigo:
            saida.append(linha)
            continue
        tipo = _tipo_linha(linha)
        precisa = False
        if tipo in ("titulo", "hr", "seta", "fonte"):
            precisa = anterior not in ("branco",)
        elif tipo == "citacao":
            precisa = anterior not in ("branco", "citacao")
        elif tipo == "item":
            precisa = anterior not in ("branco", "item", "continuacao")
        elif tipo == "texto":
            precisa = anterior in ("titulo", "hr", "seta", "fonte", "citacao", "item")
        if precisa and saida and saida[-1].strip():
            saida.append("")
        saida.append(linha)
        anterior = tipo
    texto = "\n".join(saida)
    return _RE_TACHADO.sub(r"<del>\1</del>", texto)


def _renderizar(corpo_md: str) -> str:
    return markdown.markdown(_preparar_markdown(corpo_md),
                             extensions=["extra", "sane_lists"], output_format="html")


def _semantico(h: str) -> str:
    """Põe classes nos elementos das convenções (rótulo, TL;DR, setas, fonte, opinião)."""
    h = h.replace("<h4>", '<h4 class="rotulo">')

    def citacao(m):
        miolo = m.group(1)
        tldr = bool(re.match(r"\s*<p>\s*<strong>\s*TL;?DR", miolo, re.I))
        contador = [0]

        def par(_):
            contador[0] += 1
            return '<p class="bq">' if contador[0] == 1 else '<p class="bq bq2">'
        miolo = re.sub(r"<p>", par, miolo)
        if tldr:
            miolo = re.sub(r"<strong>\s*TL;?DR\s*:?\s*</strong>:?\s*",
                           '<strong class="tldr-r">TL;DR:</strong> ', miolo, count=1, flags=re.I)
        return '<blockquote class="%s">%s</blockquote>' % ("tldr" if tldr else "cit", miolo)
    h = re.sub(r"<blockquote>(.*?)</blockquote>", citacao, h, flags=re.S)

    h = re.sub(r"<p>→\s*", '<p class="seta"><span class="seta-ic">→</span>', h)
    h = re.sub(r'((?:<p class="seta">.*?</p>\s*)+)',
               lambda m: '<div class="setas">\n%s\n</div>\n' % m.group(1).strip(), h, flags=re.S)
    h = h.replace("▲", '<span class="sobe">▲</span>').replace("▼", '<span class="desce">▼</span>')
    h = re.sub(r"<p>🔗\s*", '<p class="fonte"><span class="ico">🔗</span> ', h)
    h = re.sub(r"<p><strong>\s*Opini[ãa]o\s*:?\s*</strong>\s*:?\s*",
               '<p class="opiniao"><span class="selo">Opinião</span> ', h, flags=re.I)
    return h


# ───────────────────────── estilos inline (e-mail) ─────────────────────────

EST_TAG = {
    "p": "margin:0 0 16px 0;font-family:%s;font-size:16px;line-height:1.6;color:%s;" % (F_CORPO, C_TEXTO),
    "h1": "margin:0 0 14px 0;font-family:%s;font-size:29px;line-height:1.2;font-weight:700;color:%s;" % (F_TITULO, C_TEXTO),
    "h2": "margin:4px 0 14px 0;font-family:%s;font-size:25px;line-height:1.25;font-weight:700;color:%s;" % (F_TITULO, C_TEXTO),
    "h3": "margin:24px 0 8px 0;font-family:%s;font-size:19px;line-height:1.3;font-weight:700;color:%s;" % (F_TITULO, C_TEXTO),
    "h4": "margin:4px 0 10px 0;font-family:%s;font-size:12px;font-weight:700;color:%s;" % (F_CORPO, C_DEST),
    "hr": "border:0;border-top:1px solid %s;margin:30px 0 26px 0;height:0;" % C_LINHA,
    "a": "color:%s;text-decoration:underline;" % C_DEST,
    "ul": "margin:0 0 16px 0;padding-left:22px;",
    "ol": "margin:0 0 16px 0;padding-left:22px;",
    "li": "margin:0 0 6px 0;font-family:%s;font-size:16px;line-height:1.6;color:%s;" % (F_CORPO, C_TEXTO),
    "blockquote": "margin:0 0 20px 0;padding:0 0 0 16px;border-left:3px solid %s;" % C_LINHA,
    "del": "text-decoration:line-through;color:%s;" % C_SEC,
    "code": "font-family:Menlo,Consolas,monospace;font-size:14px;background:#EFEBE4;padding:1px 4px;border-radius:3px;",
    "pre": "margin:0 0 16px 0;padding:12px;background:#EFEBE4;overflow:auto;font-size:14px;",
    "table": "border-collapse:collapse;margin:0 0 16px 0;font-size:15px;",
    "th": "border:1px solid %s;padding:6px 10px;text-align:left;background:#EFEBE4;" % C_LINHA,
    "td": "border:1px solid %s;padding:6px 10px;vertical-align:top;" % C_LINHA,
}

EST_CLASSE = {
    "rotulo": "letter-spacing:0.16em;text-transform:uppercase;",
    "tldr": "padding:14px 18px;background:%s;border-left:4px solid %s;border-radius:0 6px 6px 0;" % (C_CAIXA, C_DEST),
    "bq": "margin:0;",
    "bq2": "margin:10px 0 0 0;",
    "tldr-r": "color:%s;letter-spacing:0.04em;" % C_DEST,
    "setas": "margin:0 0 18px 0;",
    "seta": "margin:0 0 10px 0;padding-left:24px;text-indent:-24px;",
    "seta-ic": "display:inline-block;width:24px;text-indent:0;color:%s;font-weight:700;" % C_DEST,
    "fonte": "margin:0 0 6px 0;font-size:13.5px;line-height:1.5;color:%s;" % C_SEC,
    "sobe": "color:#1E8E3E;",
    "desce": "color:#D93025;",
    "ico": "margin-right:3px;",
    "opiniao": "font-style:italic;color:%s;" % C_SEC,
    "selo": ("display:inline-block;font-style:normal;font-size:11px;font-weight:700;letter-spacing:0.1em;"
             "text-transform:uppercase;color:%s;border:1px solid %s;border-radius:3px;padding:0 6px;margin-right:4px;" % (C_DEST, C_DEST)),
}

_RE_ABERTURA = re.compile(r"<(h[1-6]|p|ul|ol|li|a|blockquote|hr|del|code|pre|table|th|td|span|strong)((?:\s[^>]*)?)>")


def _inlinar(h: str) -> str:
    """Troca cada tag por ela mesma com style="..." (o Gmail ignora boa parte do <style>)."""
    def troca(m):
        tag, attrs = m.group(1), m.group(2) or ""
        mc = re.search(r'class="([^"]*)"', attrs)
        classes = mc.group(1).split() if mc else []
        estilo = EST_TAG.get(tag, "") + "".join(EST_CLASSE.get(c, "") for c in classes)
        if not estilo or "style=" in attrs:
            return m.group(0)
        return '<%s%s style="%s">' % (tag, attrs, estilo)
    return _RE_ABERTURA.sub(troca, h)


# ───────────────────────── texto simples e curta.txt ─────────────────────────

def _texto_simples(md: str) -> str:
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", s)
    s = _RE_TACHADO.sub(r"\1", s).replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def _materias(corpo: str) -> List[Tuple[str, str]]:
    """Lista (título, TL;DR) das seções `##`. O TL;DR vem do primeiro blockquote da seção."""
    saida: List[Tuple[str, str]] = []
    linhas = corpo.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(linhas):
        m = re.match(r"^##\s+(.*\S)\s*$", linhas[i])
        if not m:
            i += 1
            continue
        titulo, tldr = _texto_simples(m.group(1)), ""
        j = i + 1
        while j < len(linhas) and not re.match(r"^(#{1,4}\s|-{3,}\s*$)", linhas[j]):
            if linhas[j].lstrip().startswith(">"):
                bloco = []
                while j < len(linhas) and linhas[j].lstrip().startswith(">"):
                    bloco.append(linhas[j].lstrip()[1:])
                    j += 1
                txt = _texto_simples(" ".join(bloco))
                tldr = re.sub(r"^TL;?DR\s*:?\s*", "", txt, flags=re.I)
                break
            j += 1
        saida.append((titulo, tldr))
        i = j if j > i else i + 1
    return saida


def _itens_indice(corpo: str) -> List[str]:
    """Bullets da lista 'Nesta edição' (plano B para o curta.txt)."""
    m = re.search(r"Nesta edi[çc][ãa]o.*?\n((?:\s*[-*+]\s+.*\n?)+)", corpo)
    if not m:
        return []
    return [_texto_simples(re.sub(r"^\s*[-*+]\s+", "", l)) for l in m.group(1).splitlines() if l.strip()]


def _setas(corpo: str) -> List[Tuple[str, str]]:
    """Linhas `→ **Rótulo**: texto (fontes)` das seções de notas curtas, como (rótulo, texto sem as fontes)."""
    saida: List[Tuple[str, str]] = []
    for linha in corpo.splitlines():
        m = re.match(r"^\s*→\s*\*\*(.+?)\*\*\s*:?\s*(.*)$", linha)
        if not m:
            continue
        resto = re.sub(r"\s*\((?:\s*;?\s*\[[^\]]*\]\([^)]*\))+\s*\)", "", m.group(2))
        # aceita também o rótulo com os dois-pontos dentro do negrito (**Rótulo:**)
        saida.append((_texto_simples(m.group(1)).rstrip(" :"), _texto_simples(resto)))
    return saida


def _cortar(txt: str, n: int) -> str:
    if len(txt) <= n:
        return txt
    corte = txt[:max(n - 1, 1)]
    if " " in corte:
        corte = corte.rsplit(" ", 1)[0]
    return corte.rstrip(" ,;:.-") + "…"


def _curta(assunto: str, data_ext: str, corpo: str, site_url: str, data: str, pagina: str = "") -> str:
    # O "Nesta edição" já é escrito como chamada; só sem ele usa títulos + TL;DR.
    indice = _itens_indice(corpo)
    materias = [(i, "") for i in indice] if len(indice) >= 3 else _materias(corpo)
    if len(materias) < 3:  # domingo: um ensaio só; completa com as linhas "→" do "Em 3 linhas"
        materias = materias + _setas(corpo)
    cabeca = [assunto_tachado(assunto), data_ext, ""]
    rodape = []
    if site_url:
        rodape = ["", "Edição completa: %s/%s" % (site_url.rstrip("/"), pagina or (data + ".html"))]
    melhor = ""
    for n_bullets in (5, 4, 3):
        for lim_tldr in (170, 130, 100, 70, 0):
            bullets = []
            for titulo, tldr in materias[:n_bullets]:
                if tldr and lim_tldr:
                    bullets.append("• %s: %s" % (titulo, _cortar(tldr, lim_tldr)))
                else:
                    bullets.append("• %s" % _cortar(titulo, 90))
            texto = "\n".join(cabeca + bullets + rodape)
            melhor = texto
            if len(texto) <= LIMITE_CURTA:
                return texto
    return melhor


# ───────────────────────── ícones do PWA ─────────────────────────

_GLIFO_I = ["XXX", ".X.", ".X.", ".X.", "XXX"]
_GLIFO_P = ["XXX", "X.X", "XXX", "X..", "X.."]
_LINHAS_IP = [i + "." + p for i, p in zip(_GLIFO_I, _GLIFO_P)]  # 7 colunas x 5 linhas
_RGB_FUNDO = (0x0F, 0x5C, 0x6E)
_RGB_LETRA = (0xFA, 0xF8, 0xF5)


def _chunk(tipo: bytes, dados: bytes) -> bytes:
    corpo = tipo + dados
    return struct.pack(">I", len(dados)) + corpo + struct.pack(">I", zlib.crc32(corpo) & 0xFFFFFFFF)


def gerar_png(tamanho: int) -> bytes:
    """PNG quadrado com 'IP' em blocos de pixel (zlib + struct, sem bibliotecas)."""
    cel = max(tamanho // 14, 1)
    x0 = (tamanho - 7 * cel) // 2
    y0 = (tamanho - 5 * cel) // 2
    fundo = bytes(_RGB_FUNDO)
    letra = bytes(_RGB_LETRA)
    linha_fundo = b"\x00" + fundo * tamanho
    brutas = []
    for y in range(tamanho):
        if y0 <= y < y0 + 5 * cel:
            padrao = _LINHAS_IP[(y - y0) // cel]
            miolo = b"".join((letra if c == "X" else fundo) * cel for c in padrao)
            resto = tamanho - x0 - 7 * cel
            brutas.append(b"\x00" + fundo * x0 + miolo + fundo * resto)
        else:
            brutas.append(linha_fundo)
    cabecalho = struct.pack(">IIBBBBB", tamanho, tamanho, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", cabecalho)
            + _chunk(b"IDAT", zlib.compress(b"".join(brutas), 9)) + _chunk(b"IEND", b""))


def gerar_svg() -> str:
    cel, x0, y0 = 10, 35, 45
    quadrados = []
    for r, padrao in enumerate(_LINHAS_IP):
        for c, ch in enumerate(padrao):
            if ch == "X":
                quadrados.append('<rect x="%d" y="%d" width="%d" height="%d"/>' % (x0 + c * cel, y0 + r * cel, cel, cel))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140">'
            '<rect width="140" height="140" fill="%s"/><g fill="%s">%s</g></svg>\n'
            % (C_DEST, C_FUNDO, "".join(quadrados)))


SW_JS = """// Service worker: guarda as páginas visitadas para ler offline.
const VERSAO = 'ip-v1';
const BASE = ['./', 'index.html', 'manifest.webmanifest', 'icon.svg', 'icon-192.png', 'icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSAO).then((c) => c.addAll(BASE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== VERSAO).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Rede primeiro (edição sempre fresca); sem rede, usa o que já foi visitado.
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  e.respondWith(
    fetch(req)
      .then((resp) => {
        if (resp && resp.ok) {
          const copia = resp.clone();
          caches.open(VERSAO).then((c) => c.put(req, copia));
        }
        return resp;
      })
      .catch(() => caches.match(req).then((r) => r || caches.match('index.html')))
  );
});
"""


def _manifest(nome: str) -> str:
    dados = {
        "name": nome,
        "short_name": "Pragmática",
        "description": "Newsletter diária feita por IA para um leitor só.",
        "lang": "pt-BR",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "background_color": C_FUNDO,
        "theme_color": C_DEST,
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
            {"src": "icon.svg", "sizes": "any", "type": "image/svg+xml"},
        ],
    }
    return json.dumps(dados, ensure_ascii=False, indent=2) + "\n"


# ───────────────────────── páginas ─────────────────────────

CSS_EMAIL_EXTRA = """
@media (max-width: 660px) {
  .pad { padding-left: 20px !important; padding-right: 20px !important; }
  h1 { font-size: 25px !important; }
  h2 { font-size: 22px !important; }
}
@media (prefers-color-scheme: dark) {
  body, .bg-page { background: #141414 !important; }
  p, li, h1, h2, h3, .tx { color: #EDEBE7 !important; }
  a, h4.rotulo, .acc, .tldr-r, .seta-ic { color: #6FC3D6 !important; }
  .sec, p.fonte, p.opiniao, del { color: #A3A3A3 !important; }
  blockquote.tldr { background: #17292E !important; border-left-color: #6FC3D6 !important; }
  blockquote.tldr p { color: #EDEBE7 !important; }
  blockquote.cit { border-left-color: #444 !important; }
  hr, .linha { border-color: #333 !important; }
  .selo { color: #6FC3D6 !important; border-color: #6FC3D6 !important; }
  code, pre { background: #222 !important; }
}
"""

CSS_SITE = """
.sobe { color: #1E8E3E; } .desce { color: #D93025; }
@media (prefers-color-scheme: dark) { .sobe { color: #5BD07A; } .desce { color: #FF7B72; } }
.cadernos { margin: 8px 0 0 0; font-size: 14px; color: var(--sec); }
.cadernos a { color: var(--dest); }
:root { --fundo: #FAF8F5; --texto: #1F1F1F; --dest: #0F5C6E; --sec: #6B6B6B;
        --linha: #E3DED6; --caixa: #E6F0F2; --codigo: #EFEBE4; }
@media (prefers-color-scheme: dark) {
  :root { --fundo: #141414; --texto: #EDEBE7; --dest: #6FC3D6; --sec: #A3A3A3;
          --linha: #333; --caixa: #17292E; --codigo: #222; }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--fundo); color: var(--texto);
       font: 17px/1.6 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
.pagina { max-width: 680px; margin: 0 auto; padding: 24px 20px 56px; }
a { color: var(--dest); text-decoration: underline; }
.voltar { font-size: 15px; text-decoration: none; }
.voltar:hover { text-decoration: underline; }
.marca { font: 700 26px/1.2 Georgia, "Times New Roman", serif; color: var(--dest); margin: 22px 0 4px; }
.meta { font-size: 14px; color: var(--sec); }
.topo { border-bottom: 2px solid var(--dest); padding-bottom: 18px; margin-bottom: 26px; }
h1, h2, h3 { font-family: Georgia, "Times New Roman", serif; line-height: 1.25; }
h1.assunto { font-size: 30px; margin: 18px 0 0; }
h2 { font-size: 26px; margin: 4px 0 14px; }
h3 { font-size: 20px; margin: 26px 0 8px; }
h4.rotulo { font-size: 12px; letter-spacing: .16em; text-transform: uppercase; color: var(--dest);
            font-weight: 700; margin: 4px 0 10px; }
p, li { margin: 0 0 16px; }
li { margin-bottom: 6px; }
ul, ol { margin: 0 0 16px; padding-left: 22px; }
hr { border: 0; border-top: 1px solid var(--linha); margin: 32px 0 28px; }
del { color: var(--sec); }
blockquote.tldr { margin: 0 0 20px; padding: 14px 18px; background: var(--caixa);
                  border-left: 4px solid var(--dest); border-radius: 0 6px 6px 0; }
blockquote.tldr p { margin: 0; }
blockquote.tldr p + p { margin-top: 10px; }
blockquote.cit { margin: 0 0 20px; padding-left: 16px; border-left: 3px solid var(--linha); }
.tldr-r { color: var(--dest); letter-spacing: .04em; }
.setas { margin: 0 0 18px; }
.seta { margin: 0 0 10px; padding-left: 24px; text-indent: -24px; }
.seta-ic { display: inline-block; width: 24px; text-indent: 0; color: var(--dest); font-weight: 700; }
p.fonte { font-size: 14px; line-height: 1.5; color: var(--sec); margin: 0 0 6px; }
.ico { margin-right: 3px; }
p.opiniao { font-style: italic; color: var(--sec); }
.selo { display: inline-block; font-style: normal; font-size: 11px; font-weight: 700; letter-spacing: .1em;
        text-transform: uppercase; color: var(--dest); border: 1px solid var(--dest); border-radius: 3px;
        padding: 0 6px; margin-right: 4px; }
code { font-family: Menlo, Consolas, monospace; font-size: .88em; background: var(--codigo);
       padding: 1px 4px; border-radius: 3px; }
pre { background: var(--codigo); padding: 12px; overflow: auto; border-radius: 6px; }
table { border-collapse: collapse; margin: 0 0 16px; font-size: 15px; display: block; overflow-x: auto; }
th, td { border: 1px solid var(--linha); padding: 6px 10px; text-align: left; vertical-align: top; }
th { background: var(--codigo); }
.rodape { border-top: 1px solid var(--linha); margin-top: 40px; padding-top: 18px; font-size: 13px; color: var(--sec); }
.rodape p { margin: 10px 0 0; }
.lista { list-style: none; padding: 0; margin: 0; }
.lista li { margin: 0; border-bottom: 1px solid var(--linha); }
.lista a.item { display: block; padding: 16px 2px; text-decoration: none; color: var(--texto); }
.lista a.item:hover .tit { text-decoration: underline; }
.lista .data { display: block; font-size: 13px; color: var(--sec); margin-bottom: 3px; }
.lista .tit { display: block; font: 700 19px/1.3 Georgia, "Times New Roman", serif; }
.lista .prev { display: block; font-size: 15px; color: var(--sec); margin-top: 3px; }
.lista .sem-pagina { display: block; padding: 16px 2px; color: var(--sec); }
.vazio { color: var(--sec); }
@media (max-width: 480px) {
  body { font-size: 16.5px; }
  h1.assunto { font-size: 26px; }
  h2 { font-size: 23px; }
}
"""

_HEAD_PWA = """<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="theme-color" content="#0F5C6E">
<meta name="color-scheme" content="light dark">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Pragmática">"""

_SCRIPT_SW = ("<script>if ('serviceWorker' in navigator) { window.addEventListener('load', function () {"
              " navigator.serviceWorker.register('sw.js'); }); }</script>")


def _esc(t) -> str:
    return html.escape(str(t if t is not None else ""), quote=True)


def _meta_linha(data_ext: str, numero, minutos: int) -> str:
    partes = [data_ext]
    if numero:
        partes.append("Edição nº %s" % numero)
    partes.append("%d min de leitura" % minutos)
    return " · ".join(partes)


def _html_email(nome, assunto, previa, data_ext, numero, minutos, corpo, site_url, indice="") -> str:
    meta = _meta_linha(data_ext, numero, minutos)
    enchimento = "&zwnj;&nbsp;" * 80
    rodape_site = ""
    if site_url:
        rodape_site = ('<p style="margin:0 0 8px 0;font-family:%s;font-size:13px;line-height:1.5;color:%s;" class="sec">'
                       '<a href="%s/%s" style="color:%s;text-decoration:underline;">Arquivo de edições</a></p>'
                       % (F_CORPO, C_SEC, _esc(site_url.rstrip("/")), _esc(indice), C_DEST))
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{titulo}</title>
<style>{css}</style>
</head>
<body class="bg-page" style="margin:0;padding:0;background:{fundo};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:{fundo};mso-hide:all;">{previa}{enchimento}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="bg-page" style="background:{fundo};">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:640px;">
<tr><td class="pad" style="padding:20px 32px 18px 32px;border-bottom:2px solid {dest};" >
<div class="acc" style="font-family:{f_titulo};font-size:26px;line-height:1.2;font-weight:700;color:{dest};">{nome}</div>
<div class="sec" style="font-family:{f_corpo};font-size:13px;line-height:1.5;color:{sec};margin-top:6px;">{meta}</div>
</td></tr>
<tr><td class="pad tx" style="padding:28px 32px 8px 32px;font-family:{f_corpo};font-size:16px;line-height:1.6;color:{texto};">
{corpo}
</td></tr>
<tr><td class="pad" style="padding:8px 32px 36px 32px;">
<div class="linha" style="border-top:1px solid {linha};padding-top:18px;">
{rodape_site}<p class="sec" style="margin:0;font-family:{f_corpo};font-size:13px;line-height:1.5;color:{sec};">{rodape_ia}</p>
</div>
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>
""".format(titulo=_esc(assunto_sem_marcas(assunto)), css=CSS_EMAIL_EXTRA, fundo=C_FUNDO,
           previa=_esc(previa), enchimento=enchimento, dest=C_DEST, nome=_esc(nome),
           f_titulo=F_TITULO, f_corpo=F_CORPO, sec=C_SEC, meta=_esc(meta), texto=C_TEXTO,
           corpo=corpo, linha=C_LINHA, rodape_site=rodape_site, rodape_ia=RODAPE_IA)


def _html_pagina_site(nome, assunto, previa, data_ext, numero, minutos, corpo, indice="index.html") -> str:
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {nome}</title>
<meta name="description" content="{previa}">
{head_pwa}
<style>{css}</style>
</head>
<body>
<div class="pagina">
<header class="topo">
<a class="voltar" href="{indice}">← todas as edições</a>
<div class="marca">{nome}</div>
<div class="meta">{meta}</div>
<h1 class="assunto">{assunto_html}</h1>
</header>
<main class="corpo">
{corpo}
</main>
<footer class="rodape">
<a class="voltar" href="{indice}">← todas as edições</a>
<p>{rodape_ia}</p>
</footer>
</div>
{script}
</body>
</html>
""".format(titulo=_esc(assunto_sem_marcas(assunto)), nome=_esc(nome), previa=_esc(previa),
           head_pwa=_HEAD_PWA, css=CSS_SITE, meta=_esc(_meta_linha(data_ext, numero, minutos)),
           assunto_html=assunto_html(assunto), corpo=corpo, rodape_ia=RODAPE_IA, script=_SCRIPT_SW,
           indice=indice)


def _html_indice(nome, edicoes: List[dict], nav: str = "") -> str:
    if edicoes:
        itens = []
        for e in edicoes:
            rotulo = data_por_extenso(date.fromisoformat(e["data"]))
            if e.get("numero"):
                rotulo += " · nº %s" % e["numero"]
            if e.get("extra"):
                rotulo += " · edição extra"
            previa = '<span class="prev">%s</span>' % _esc(e["previa"]) if e.get("previa") else ""
            miolo = ('<span class="data">%s</span><span class="tit">%s</span>%s'
                     % (_esc(rotulo), assunto_html(e.get("assunto") or e["data"]), previa))
            if e["tem_pagina"]:
                itens.append('<li><a class="item" href="%s">%s</a></li>' % (e["pagina"], miolo))
            else:
                itens.append('<li><span class="sem-pagina">%s</span></li>' % miolo)
        lista = '<ul class="lista">\n%s\n</ul>' % "\n".join(itens)
    else:
        lista = '<p class="vazio">Nenhuma edição publicada ainda.</p>'
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{nome} · todas as edições</title>
<meta name="description" content="Newsletter diária feita por IA para um leitor só.">
{head_pwa}
<style>{css}</style>
</head>
<body>
<div class="pagina">
<header class="topo">
<div class="marca" style="margin-top:0">{nome}</div>
<div class="meta">Arquivo de edições · {total} no total</div>
{nav}
</header>
<main>
{lista}
</main>
<footer class="rodape"><p>{rodape_ia}</p></footer>
</div>
{script}
</body>
</html>
""".format(nome=_esc(nome), head_pwa=_HEAD_PWA, css=CSS_SITE, total=len(edicoes), lista=lista,
           rodape_ia=RODAPE_IA, script=_SCRIPT_SW, nav=nav)


# ───────────────────────── montagem ─────────────────────────

def _listar_edicoes(raiz: Path, docs: Path, caderno: str = cadernos.GERAL) -> List[dict]:
    """Todas as edições do caderno, da mais nova para a mais antiga (a extra vem antes da do dia)."""
    saida = []
    base = cadernos.pasta_edicoes(raiz, caderno)
    for pasta in sorted(base.glob(cadernos.padrao_pastas(caderno)), reverse=True):
        arq = pasta / "edicao.md"
        if not arq.exists():
            continue
        try:
            date.fromisoformat(pasta.name[:10])
            meta, _ = ler_front_matter(arq)
        except Exception:
            continue
        pagina = "%s%s.html" % (cadernos.prefixo(caderno), pasta.name)
        saida.append({
            "data": pasta.name[:10],
            "numero": meta.get("numero"),
            "assunto": meta.get("assunto"),
            "previa": meta.get("previa"),
            "extra": pasta.name.endswith("-extra"),
            "pagina": pagina,
            "tem_pagina": (docs / pagina).exists(),
        })
    return saida


def _nav(raiz: Path, caderno: str) -> str:
    """Linha com os links entre a geral e os cadernos."""
    especiais = cadernos.nomes(raiz)
    if not especiais:
        return ""
    links = []
    for c in [cadernos.GERAL] + especiais:
        nome = cadernos.config(raiz, c).get("nome") or NOME_PADRAO
        rotulo = nome.split("·")[-1].strip() if c != cadernos.GERAL else "Geral"
        if c == caderno:
            links.append("<strong>%s</strong>" % _esc(rotulo))
        else:
            links.append('<a href="%s">%s</a>' % (cadernos.indice_site(c), _esc(rotulo)))
    return '<div class="cadernos">Cadernos: %s</div>' % " · ".join(links)


def _escrever_indices(raiz: Path, docs: Path) -> None:
    """Regrava o arquivo de edições da geral e de cada caderno (a navegação entre eles muda junto)."""
    for c in [cadernos.GERAL] + cadernos.nomes(raiz):
        nome = cadernos.config(raiz, c).get("nome") or NOME_PADRAO
        (docs / cadernos.indice_site(c)).write_text(
            _html_indice(nome, _listar_edicoes(raiz, docs, c), _nav(raiz, c)), encoding="utf-8")


def _rel(p: Path, raiz: Path) -> str:
    return p.relative_to(raiz).as_posix()


def montar(data: str, raiz: Path, config: dict, caderno: str = cadernos.GERAL) -> dict:
    """Gera email.html, curta.txt e o site em docs/. Devolve um resumo do que foi feito.

    DATA é o nome da pasta da edição: AAAA-MM-DD, ou AAAA-MM-DD-extra nos cadernos.
    """
    data = str(data)
    arq = cadernos.pasta_edicoes(raiz, caderno) / data / "edicao.md"
    if not arq.exists():
        raise FileNotFoundError("Não achei %s" % _rel(arq, raiz))
    config = config or {}
    d = date.fromisoformat(data[:10])
    meta, corpo = ler_front_matter(arq)
    # O painel de números (cotações) é gerado por código e entra no lugar do marcador, sem passar pela IA.
    painel = arq.parent / "painel.md"
    avisos_painel = []
    if MARCA_PAINEL in corpo:
        if painel.exists():
            corpo = corpo.replace(MARCA_PAINEL, painel.read_text(encoding="utf-8").strip())
        else:
            avisos_painel.append("a edição tem o marcador do painel, mas falta painel.md na pasta")
    nome = config.get("nome") or NOME_PADRAO
    site_url = str(config.get("site_url") or "").strip()
    avisos: List[str] = list(avisos_painel)

    if not meta:
        avisos.append("a edição não tem front matter (o bloco entre ---)")
    for campo in ("assunto", "previa", "numero"):
        if not meta.get(campo):
            avisos.append("falta `%s` no front matter" % campo)
    if meta.get("data") and str(meta["data"]) != data:
        avisos.append("a `data` do front matter (%s) é diferente da pasta (%s)" % (meta["data"], data))

    assunto = str(meta.get("assunto") or data)
    previa = str(meta.get("previa") or "")
    numero = meta.get("numero")
    data_ext = data_por_extenso(d)
    minutos = meta.get("tempo_leitura_min")
    if not minutos:
        minutos = max(1, int(ceil(len(re.findall(r"\w+", _texto_simples(corpo))) / 220.0)))
    minutos = int(minutos)

    for titulo, tldr in _materias(corpo):
        if not tldr and meta.get("tipo") != "domingo":  # o ensaio não tem TL;DR
            avisos.append("a matéria \"%s\" não tem TL;DR" % titulo)

    corpo_html = _semantico(_renderizar(corpo))

    pasta = arq.parent
    nome_pagina = "%s%s.html" % (cadernos.prefixo(caderno), data)
    nome_indice = cadernos.indice_site(caderno)
    email = pasta / "email.html"
    email.write_text(_html_email(nome, assunto, previa, data_ext, numero, minutos,
                                 _inlinar(corpo_html), site_url,
                                 "" if caderno == cadernos.GERAL else nome_indice), encoding="utf-8")
    curta = pasta / "curta.txt"
    texto_curta = _curta(assunto, data_ext, corpo, site_url, data, nome_pagina)
    curta.write_text(texto_curta + "\n", encoding="utf-8")

    docs = raiz / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    pagina = docs / nome_pagina
    pagina.write_text(_html_pagina_site(nome, assunto, previa, data_ext, numero, minutos, corpo_html,
                                        nome_indice), encoding="utf-8")
    _escrever_indices(raiz, docs)
    indice = docs / nome_indice

    (docs / "manifest.webmanifest").write_text(_manifest(nome), encoding="utf-8")
    (docs / "sw.js").write_text(SW_JS, encoding="utf-8")
    (docs / "icon.svg").write_text(gerar_svg(), encoding="utf-8")
    (docs / "icon-192.png").write_bytes(gerar_png(192))
    (docs / "icon-512.png").write_bytes(gerar_png(512))
    (docs / ".nojekyll").write_text("", encoding="utf-8")

    return {
        "data": data,
        "email": _rel(email, raiz),
        "curta": _rel(curta, raiz),
        "pagina": _rel(pagina, raiz),
        "indice": _rel(indice, raiz),
        "pwa": ["docs/manifest.webmanifest", "docs/sw.js", "docs/icon.svg",
                "docs/icon-192.png", "docs/icon-512.png"],
        "caracteres_curta": len(texto_curta),
        "minutos": minutos,
        "avisos": avisos,
    }
