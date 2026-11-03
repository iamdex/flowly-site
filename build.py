#!/usr/bin/env python3
"""Flowly website: four static pages per language (Italian at /, English at /en/).

    python3 build.py

All copy lives in CONTENT below; one template renders every page. Keep the privacy and
terms text in sync with what the app actually does.
"""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "hellodave@espertini.com"
STORE = "https://apps.apple.com/app/id6829690402"

CONTENT = {
    "it": {
        "dir": ROOT,
        "other": ("en/", "English"),
        "store": "Scarica sull’App Store",
        "nav": [("privacy.html", "Privacy"), ("terms.html", "Termini"), ("support.html", "Supporto")],
        "home": {
            "title": "Flowly",
            "lead": "Un timer per concentrarsi, per iPhone.",
            "features": [
                ("lock", "Schermata di blocco", "Il tempo che manca, senza aprire l’app."),
                ("sounds", "Scene sonore", "Pioggia, bosco, mare. Anche offline."),
                ("block", "Blocco delle app", "Le app che distraggono restano chiuse durante il focus."),
            ],
            "privacy": "Nessun account, nessuna pubblicità, nessun tracciamento.",
        },
        "privacy": ("Privacy", [
            ("", "Aggiornata il 3 novembre 2026. Titolare: Davide Espertini, " + f'<a href="mailto:{EMAIL}">{EMAIL}</a>.'),
            ("Sul tuo iPhone", "Sessioni, storico, intenzioni e impostazioni restano sul dispositivo e non vengono inviati a nessuno. Li cancelli da Impostazioni › Cancella i dati locali o eliminando l’app."),
            ("Blocco delle app", "Le app si scelgono nell’elenco di sistema di iOS. Flowly riceve solo riferimenti anonimi e non sa quali app hai scelto."),
            ("Acquisti", "I pagamenti passano da Apple. Per verificare acquisti e abbonamenti uso RevenueCat, Inc., che riceve un identificativo anonimo, lo storico acquisti e dati tecnici del dispositivo. Base giuridica: esecuzione del contratto. " + '<a href="https://www.revenuecat.com/privacy">Privacy di RevenueCat</a>.'),
            ("Notifiche", "Solo notifiche locali, programmate sul dispositivo. Nessun server."),
            ("Diritti", f'Per accesso o cancellazione dei dati di acquisto scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a> con l’ID di supporto che trovi in fondo alle Impostazioni dell’app. Puoi anche rivolgerti al Garante per la protezione dei dati personali.'),
        ]),
        "terms": ("Termini", [
            ("", 'Aggiornati il 3 novembre 2026. Valgono questi termini e la <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">licenza standard di Apple</a>.'),
            ("Flowly", "Un timer per organizzare lavoro e pause. Non è un dispositivo medico."),
            ("Flowly Plus", "Si acquista solo dall’App Store: abbonamento annuale, con eventuale prova gratuita, oppure acquisto unico. L’abbonamento si rinnova automaticamente salvo disdetta almeno 24 ore prima, da Impostazioni › il tuo nome › Abbonamenti. Pagamenti e rimborsi sono gestiti da Apple."),
            ("Responsabilità", "L’app è fornita così com’è. Notifiche, Attività in tempo reale e blocco delle app dipendono anche da iOS."),
            ("Contatti", f'<a href="mailto:{EMAIL}">{EMAIL}</a>. Legge italiana, salvi i diritti del consumatore.'),
        ]),
        "support": ("Supporto", [
            ("Recuperare Plus", "Flowly › Impostazioni › Ripristina acquisti, con lo stesso ID Apple."),
            ("Disdire l’abbonamento", "Impostazioni dell’iPhone › il tuo nome › Abbonamenti › Flowly."),
            ("Il tempo non compare sulla schermata di blocco", "Impostazioni › Flowly Focus › Attività in tempo reale."),
            ("Il blocco delle app non parte", "Serve Plus. In Impostazioni › Focus profondo scegli le app e attiva il blocco. Le app si bloccano solo durante un focus."),
            ("Notifiche delle app bloccate", "Durante il blocco potrebbero non arrivare: lo decide iOS."),
            ("Scrivimi", f'<a href="mailto:{EMAIL}?subject=Flowly">{EMAIL}</a>'),
        ]),
        "rights": "© 2026 Davide Espertini",
    },
    "en": {
        "dir": ROOT / "en",
        "other": ("../", "Italiano"),
        "store": "Download on the App Store",
        "nav": [("privacy.html", "Privacy"), ("terms.html", "Terms"), ("support.html", "Support")],
        "home": {
            "title": "Flowly",
            "lead": "A focus timer for iPhone.",
            "features": [
                ("lock", "Lock screen", "The time left, without opening the app."),
                ("sounds", "Soundscapes", "Rain, forest, sea. Offline too."),
                ("block", "App blocking", "Distracting apps stay closed during focus."),
            ],
            "privacy": "No account, no ads, no tracking.",
        },
        "privacy": ("Privacy", [
            ("", "Updated November 3, 2026. Controller: Davide Espertini, " + f'<a href="mailto:{EMAIL}">{EMAIL}</a>.'),
            ("On your iPhone", "Sessions, history, intentions and settings stay on the device and are sent to no one. Delete them in Settings › Delete local data, or by deleting the app."),
            ("App blocking", "Apps are chosen in iOS’s own list. Flowly gets only anonymous references and can’t see which apps you chose."),
            ("Purchases", "Payments go through Apple. To verify purchases and subscriptions I use RevenueCat, Inc., which receives an anonymous identifier, purchase history and technical device data. Legal basis: performance of the contract. " + '<a href="https://www.revenuecat.com/privacy">RevenueCat privacy</a>.'),
            ("Notifications", "Local notifications only, scheduled on the device. No server."),
            ("Your rights", f'For access to or deletion of purchase data, write to <a href="mailto:{EMAIL}">{EMAIL}</a> with the Support ID at the bottom of the app’s Settings. You may also contact your data protection authority.'),
        ]),
        "terms": ("Terms", [
            ("", 'Updated November 3, 2026. These terms and <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple’s standard license</a> apply.'),
            ("Flowly", "A timer for organizing work and breaks. Not a medical device."),
            ("Flowly Plus", "Bought only through the App Store: a yearly subscription, possibly with a free trial, or a one-time purchase. The subscription renews automatically unless cancelled at least 24 hours before, in Settings › your name › Subscriptions. Payments and refunds are handled by Apple."),
            ("Liability", "The app is provided as is. Notifications, Live Activities and app blocking also depend on iOS."),
            ("Contact", f'<a href="mailto:{EMAIL}">{EMAIL}</a>. Italian law, without prejudice to consumer rights.'),
        ]),
        "support": ("Support", [
            ("Restore Plus", "Flowly › Settings › Restore purchases, with the same Apple ID."),
            ("Cancel the subscription", "iPhone Settings › your name › Subscriptions › Flowly."),
            ("The time isn’t on the lock screen", "Settings › Flowly Focus › Live Activities."),
            ("App blocking doesn’t start", "It needs Plus. In Settings › Deep focus, choose the apps and turn blocking on. Apps are blocked only during a focus."),
            ("Notifications from blocked apps", "They may not arrive while blocked: iOS decides that."),
            ("Write to me", f'<a href="mailto:{EMAIL}?subject=Flowly">{EMAIL}</a>'),
        ]),
        "rights": "© 2026 Davide Espertini",
    },
}


def page(lang, c, title, main):
    up = "" if lang == "it" else "../"
    other_href, other_label = c["other"]
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in c["nav"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{c['home']['lead']}">
<meta name="apple-itunes-app" content="app-id=6829690402">
<link rel="icon" href="{up}assets/favicon.png">
<link rel="apple-touch-icon" href="{up}assets/icon.png">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<div class="wrap">
<header><a class="brand" href="index.html"><img src="{up}assets/mark.svg" alt="">Flowly</a><nav><a href="{STORE}">App Store</a></nav></header>
<main>{main}</main>
<footer><span>{c['rights']}</span><nav>{nav}<a href="{other_href}" hreflang="{'en' if lang == 'it' else 'it'}">{other_label}</a></nav></footer>
</div>
</body>
</html>
"""


def picture(up, name, alt):
    """Light and dark image (assets/<name>.jpg and assets/<name>-night.jpg)."""
    return (f'<img class="light-only" src="{up}assets/{name}.jpg" alt="{alt}">'
            f'<img class="dark-only" src="{up}assets/{name}-night.jpg" alt="{alt}">')


def home(lang, c):
    up = "" if lang == "it" else "../"
    h = c["home"]
    feats = "".join(f"<div>{picture(up, img, t)}<h2>{t}</h2><p>{p}</p></div>" for img, t, p in h["features"])
    main = f"""
<section class="hero">
  <h1>{h['title']}</h1>
  <p>{h['lead']}</p>
  <a class="cta" href="{STORE}">{c['store']}</a>
  <div class="shot">{picture(up, 'session', h['lead'])}</div>
</section>
<section class="features">{feats}</section>
<p class="note">{h['privacy']}</p>
"""
    return page(lang, c, f"Flowly — {h['lead']}", main)


def doc(lang, c, key):
    title, parts = c[key]
    body = "".join((f"<h2>{h}</h2>" if h else "") + f"<p>{p}</p>" for h, p in parts)
    return page(lang, c, f"{title} — Flowly", f'<article class="doc"><h1>{title}</h1>{body}</article>')


def main():
    for lang, c in CONTENT.items():
        c["dir"].mkdir(exist_ok=True)
        (c["dir"] / "index.html").write_text(home(lang, c), encoding="utf-8")
        for key in ("privacy", "terms", "support"):
            (c["dir"] / f"{key}.html").write_text(doc(lang, c, key), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    print("built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))


if __name__ == "__main__":
    main()
