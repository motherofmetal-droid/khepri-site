# -*- coding: utf-8 -*-
"""Gera a página de apresentação do Khepri (GitHub Pages) em 10 idiomas, a partir de core/idiomas/seo.py.

Uso, na raiz do projeto:   python gerar_site.py
Depois publique a pasta docs/ (veja o passo a passo). Rode de novo sempre que mudar o seo.py.
"""
import importlib.util
import json
import os
import shutil
from datetime import date
from html import escape as esc

RAIZ = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(RAIZ, "docs")
SITE = os.getenv("KHEPRI_SITE_URL", "https://motherofmetal-droid.github.io/khepri").rstrip("/")
APP = os.getenv("KHEPRI_APP_URL", "https://appkhepri.streamlit.app").rstrip("/")

BING_ID = "4E5C64C9F22B229C8AE3A5484F2D590C"                  # do seu BingSiteAuth.xml
GOOGLE_ARQUIVO = "googlefcdc17dfe842da1d.html"                # do seu arquivo de verificação
GOOGLE_META = ""                                              # se o Google der uma tag, cole só o "content" aqui

_spec = importlib.util.spec_from_file_location("khepri_seo", os.path.join(RAIZ, "core", "idiomas", "seo.py"))
seo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(seo)

def url_pagina(cod):
    return SITE + "/" if cod == "pt" else "%s/%s/" % (SITE, cod)

def lang_html(cod):
    return seo.HTML_LANG.get(cod, cod)

def alternativas():
    alts = ['<link rel="alternate" hreflang="%s" href="%s">' % (lang_html(c), url_pagina(c)) for c in seo.ORDEM]
    alts.append('<link rel="alternate" hreflang="x-default" href="%s">' % url_pagina("en"))
    return "\n".join(alts)

def pagina(cod):
    s = seo.SEO[cod]
    imagem = SITE + "/khepri-512.png"
    jsonld = {
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Khepri",
        "description": s["descricao"], "url": APP, "applicationCategory": "DesignApplication",
        "operatingSystem": "Web", "inLanguage": cod, "image": imagem, "keywords": s["palavras"],
        "author": {"@type": "Person", "name": "Larissa Moura Nascimento"},
    }
    ld = json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/")
    idiomas = " · ".join(
        ('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (url_pagina(c), lang_html(c), lang_html(c), esc(seo.NOMES[c])))
        if c != cod else "<strong>%s</strong>" % esc(seo.NOMES[c]) for c in seo.ORDEM)
    itens = "\n".join("      <li>%s</li>" % esc(r) for r in s["recursos"])
    google = ('<meta name="google-site-verification" content="%s">\n' % esc(GOOGLE_META)) if GOOGLE_META else ""
    direcao = "rtl" if cod in seo.RTL else "ltr"
    return f"""<!DOCTYPE html>
<html lang="{lang_html(cod)}" dir="{direcao}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(s["titulo"])}</title>
<meta name="description" content="{esc(s["descricao"])}">
<meta name="keywords" content="{esc(s["palavras"])}">
<meta name="author" content="Larissa Moura Nascimento">
<meta name="theme-color" content="#164B4B">
<meta name="msvalidate.01" content="{BING_ID}">
{google}<link rel="canonical" href="{url_pagina(cod)}">
{alternativas()}
<link rel="icon" href="khepri-512.png" type="image/png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Khepri">
<meta property="og:title" content="{esc(s["titulo"])}">
<meta property="og:description" content="{esc(s["descricao"])}">
<meta property="og:url" content="{url_pagina(cod)}">
<meta property="og:image" content="{imagem}">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{ld}</script>
<style>
body{{font-family:system-ui,Segoe UI,Roboto,Arial,sans-serif;background:#FBF6EC;color:#1d2b2b;margin:0;line-height:1.6}}
main{{max-width:760px;margin:0 auto;padding:24px 18px 48px}}
h1{{color:#164B4B;font-size:clamp(1.5rem,5vw,2.2rem);line-height:1.2}}
nav{{font-size:.9rem;margin-bottom:18px}} nav a{{color:#0B3D91}}
img{{width:96px;height:96px}}
.btn{{display:inline-block;background:#164B4B;color:#FBF6EC;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:600;margin:12px 0}}
.btn:hover,.btn:focus{{background:#F0B45A;color:#164B4B}}
footer{{font-size:.85rem;color:#4a4a4a;margin-top:32px}}
</style>
</head>
<body>
<main>
  <nav aria-label="Languages">{idiomas}</nav>
  <img src="khepri-512.png" alt="Khepri" width="96" height="96">
  <h1>{esc(s["h1"])}</h1>
  <p>{esc(s["intro"])}</p>
  <ul>
{itens}
  </ul>
  <a class="btn" href="{APP}/?lang={cod}">{esc(s["botao"])}</a>
  <footer>Khepri — Larissa Moura Nascimento. ABNT/NBR · Revit · pyRevit · Dynamo · BIM · .json</footer>
</main>
</body>
</html>
"""

def sitemap():
    hoje = date.today().isoformat()
    alts = "".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>\n' % (lang_html(c), url_pagina(c))
                   for c in seo.ORDEM)
    alts += '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n' % url_pagina("en")
    urls = "".join("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n%s  </url>\n" % (url_pagina(c), hoje, alts)
                   for c in seo.ORDEM)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")

def gravar(caminho, texto):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)

def main():
    for cod in seo.ORDEM:
        gravar(os.path.join(DOCS, "index.html") if cod == "pt" else os.path.join(DOCS, cod, "index.html"),
               pagina(cod))
    gravar(os.path.join(DOCS, "sitemap.xml"), sitemap())
    gravar(os.path.join(DOCS, GOOGLE_ARQUIVO), "google-site-verification: %s" % GOOGLE_ARQUIVO)
    gravar(os.path.join(DOCS, "BingSiteAuth.xml"),
           '<?xml version="1.0"?>\n<users>\n\t<user>%s</user>\n</users>\n' % BING_ID)
    gravar(os.path.join(DOCS, ".nojekyll"), "")
    logo = os.path.join(RAIZ, "static", "khepri-512.png")
    if os.path.exists(logo):
        shutil.copyfile(logo, os.path.join(DOCS, "khepri-512.png"))
    else:
        print("AVISO: static/khepri-512.png não encontrado; copie o logo para docs/khepri-512.png.")
    print("Pronto: %d páginas em docs/. Site: %s/" % (len(seo.ORDEM), SITE))

if __name__ == "__main__":
    main()
