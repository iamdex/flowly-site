#!/usr/bin/env python3
"""Builds the static Flowly site (Italian at /, English at /en/). Run: python3 build.py

Content mirrors what the app actually does (no analytics, data on device, RevenueCat for
purchases). Keep it in sync with the app's privacy screen and docs.
"""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "hellodave@espertini.com"
DEV = "Davide Espertini"
APP_STORE = "https://apps.apple.com/app/id6829690402"
UPDATED = {"it": "3 novembre 2026", "en": "November 3, 2026"}

T = {
    "it": {
        "lang": "it", "other": "en", "other_label": "English", "base": "",
        "nav": [("index.html#funzioni", "Funzioni"), ("index.html#plus", "Plus"), ("support.html", "Supporto")],
        "title": "Flowly — timer per concentrarsi, con calma",
        "desc": "Un timer Pomodoro calmo e privato: pause vere, scene sonore offline, blocco delle app durante il focus. Niente pubblicità, niente tracciamento.",
        "h1": "Concentrati.<br>Poi riposa davvero.",
        "lead": "Un timer calmo e privato per lavorare a blocchi: pause vere, scene sonore che funzionano offline e, se vuoi, le app che ti distraggono in pausa finché il focus non finisce.",
        "store": "Scarica sull’App Store", "soon": "In arrivo sull’App Store per iPhone.",
        "feat_h": "Cosa fa", "feat_sub": "Poche cose, fatte con cura. Il timer, le pause e lo storico sono gratuiti, per sempre.",
        "features": [
            ("Gratis", "Pomodoro o su misura", "25/5 con una pausa lunga ogni 4 focus, oppure le tue durate. La fase successiva parte solo quando lo decidi tu."),
            ("Gratis", "Sempre sotto gli occhi", "Il tempo che manca resta sulla schermata di blocco e nella Dynamic Island. Widget per Home e schermata di blocco."),
            ("Gratis", "Scene sonore offline", "Pioggia, bosco, mare, rumore marrone: illustrazioni di giorno e di notte e suoni che non hanno bisogno di rete."),
            ("Plus", "Blocco delle app", "Scegli le app che ti distraggono: restano in pausa solo durante il focus e si sbloccano da sole, anche se Flowly è chiusa."),
            ("Plus", "Mix di scene", "Aggiungi un sottofondo più basso sotto la scena principale. Pioggia e camino, caffè e rumore marrone."),
            ("Plus", "Schermo sempre acceso", "Durante la sessione lo schermo non si spegne, per tenere il tempo a portata di sguardo."),
        ],
        "plus_h": "Flowly Plus", "plus_sub": "Due modi per sbloccare le stesse funzioni. I prezzi nella tua valuta sono sull’App Store.",
        "plans": [("Annuale", "con 7 giorni gratis", "Si rinnova ogni anno, disdici quando vuoi dalle impostazioni dell’iPhone."), ("Per sempre", "una volta sola", "Un unico acquisto, nessun rinnovo.")],
        "privacy_h": "Privata per scelta", "privacy_p": "Niente account, niente pubblicità, niente statistiche. Sessioni, intenzioni e impostazioni restano sul tuo iPhone. Le app che scegli di bloccare le gestisce iOS: Flowly non sa quali sono.",
        "dev_h": f"Ciao, sono {DEV}", "dev_p": ["Ho creato Flowly perché volevo un timer per concentrarmi che fosse calmo: niente pubblicità, niente punteggi, niente notifiche per farti tornare nell’app.", "È un progetto indipendente: lo progetto, lo sviluppo e lo curo personalmente. Se hai un’idea o un problema, scrivimi: leggo tutto."],
        "write": "Scrivimi",
        "footer": ["Privacy", "Termini", "Supporto"],
        "rights": f"© 2026 {DEV}",
    },
    "en": {
        "lang": "en", "other": "it", "other_label": "Italiano", "base": "../",
        "nav": [("index.html#features", "Features"), ("index.html#plus", "Plus"), ("support.html", "Support")],
        "title": "Flowly — a calm focus timer",
        "desc": "A calm, private Pomodoro timer: real breaks, offline soundscapes, app blocking during focus. No ads, no tracking.",
        "h1": "Focus.<br>Then really rest.",
        "lead": "A calm, private timer for working in blocks: real breaks, soundscapes that work offline and, if you want, the apps that distract you paused until the focus ends.",
        "store": "Download on the App Store", "soon": "Coming soon to the App Store for iPhone.",
        "feat_h": "What it does", "feat_sub": "A few things, done with care. The timer, breaks and history are free, forever.",
        "features": [
            ("Free", "Pomodoro or your own", "25/5 with a long break every 4 focuses, or your own durations. The next phase starts only when you decide."),
            ("Free", "Always in sight", "The time left stays on the lock screen and in the Dynamic Island. Widgets for Home and lock screen."),
            ("Free", "Offline soundscapes", "Rain, forest, sea, brown noise: day and night illustrations and sounds that need no network."),
            ("Plus", "App blocking", "Choose the apps that distract you: they’re paused only during focus and unlock by themselves, even if Flowly is closed."),
            ("Plus", "Mix scenes", "Add a quieter layer under the main scene. Rain and fireplace, café and brown noise."),
            ("Plus", "Keep the screen on", "During a session the screen stays on, so the time is always a glance away."),
        ],
        "plus_h": "Flowly Plus", "plus_sub": "Two ways to unlock the same features. Prices in your currency are on the App Store.",
        "plans": [("Yearly", "with a 7-day free trial", "Renews every year; cancel any time in your iPhone settings."), ("Lifetime", "one-time", "A single purchase, no renewals.")],
        "privacy_h": "Private by design", "privacy_p": "No account, no ads, no analytics. Sessions, intentions and settings stay on your iPhone. The apps you choose to block are handled by iOS: Flowly can’t see which ones they are.",
        "dev_h": f"Hi, I’m {DEV}", "dev_p": ["I made Flowly because I wanted a calm focus timer: no ads, no scores, no notifications to pull you back into the app.", "It’s an independent project: I design, build and look after it myself. If you have an idea or a problem, write to me: I read everything."],
        "write": "Write to me",
        "footer": ["Privacy", "Terms", "Support"],
        "rights": f"© 2026 {DEV}",
    },
}


def page(lang, name, title, body, desc=None):
    t = T[lang]
    b = t["base"]
    other_href = ("en/" if lang == "it" else "../") + name
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in t["nav"])
    foot = "".join(f'<a href="{h}">{l}</a>' for h, l in zip(["privacy.html", "terms.html", "support.html"], t["footer"]))
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc or t['desc']}">
<meta name="theme-color" content="#F7F5F0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131517" media="(prefers-color-scheme: dark)">
<meta name="apple-itunes-app" content="app-id=6829690402">
<link rel="icon" href="{b}assets/favicon.png">
<link rel="apple-touch-icon" href="{b}assets/icon.png">
<link rel="alternate" hreflang="{t['other']}" href="{other_href}">
<link rel="stylesheet" href="{b}assets/style.css">
</head>
<body>
<header class="wrap top">
  <a class="brand" href="index.html"><img src="{b}assets/mark.svg" alt="">Flowly</a>
  <nav class="top">{nav}<a href="{other_href}" hreflang="{t['other']}">{t['other_label']}</a></nav>
</header>
<main>
{body}
</main>
<footer class="bottom"><div class="wrap"><span>{t['rights']} · <a href="mailto:{EMAIL}">{EMAIL}</a></span><nav>{foot}</nav></div></footer>
</body>
</html>
"""


def index(lang):
    t = T[lang]
    b = t["base"]
    feats = "".join(
        f'<div class="card"><span class="tag{" plus" if tag in ("Plus",) else ""}">{tag}</span><h3>{h}</h3><p>{p}</p></div>' for tag, h, p in t["features"]
    )
    plans = "".join(f'<div class="card"><h3>{n}</h3><p class="price">{s}</p><p>{d}</p></div>' for n, s, d in t["plans"])
    phones = "".join(
        f'<img class="day" src="{b}assets/{s}.jpg" alt=""><img class="night" src="{b}assets/{s}-night.jpg" alt="">' for s in ("rain", "forest", "sea")
    )
    dev = "".join(f"<p>{p}</p>" for p in t["dev_p"])
    feat_id = "funzioni" if lang == "it" else "features"
    body = f"""
<div class="wrap hero">
  <div>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <a class="badge-store" href="{APP_STORE}">{t["store"]}</a>
    <span class="soon">{t['soon']}</span>
  </div>
  <div class="phones" aria-hidden="true">{phones}</div>
</div>
<section id="{feat_id}"><div class="wrap"><h2>{t['feat_h']}</h2><p class="sub">{t['feat_sub']}</p><div class="grid">{feats}</div></div></section>
<section id="plus"><div class="wrap"><h2>{t['plus_h']}</h2><p class="sub">{t['plus_sub']}</p><div class="pricing">{plans}</div></div></section>
<section><div class="wrap"><h2>{t['privacy_h']}</h2><p class="sub">{t['privacy_p']}</p></div></section>
<section><div class="wrap dev"><img src="{b}assets/mark.svg" alt=""><div><h2>{t['dev_h']}</h2>{dev}<p><a href="mailto:{EMAIL}?subject=Flowly">{t['write']} → {EMAIL}</a></p></div></div></section>
"""
    return page(lang, "index.html", t["title"], body)


PRIVACY = {
    "it": f"""<article class="doc">
<h1>Informativa sulla privacy</h1>
<p class="updated">Aggiornata il {UPDATED['it']}</p>
<p>Flowly è un timer per la concentrazione per iPhone, sviluppato da {DEV} («io»). Questa informativa spiega quali dati tratta l’app e perché. In breve: Flowly non ha account, non mostra pubblicità e non raccoglie statistiche d’uso.</p>
<h2>Titolare e contatti</h2>
<p>{DEV} — <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Dati che restano sul tuo iPhone</h2>
<p>Sessioni, storico, intenzioni che scrivi, preferenze e scene scelte sono salvati solo sul dispositivo. Non vengono inviati a me né a terzi. Puoi cancellarli in qualsiasi momento da Impostazioni › Cancella i dati locali, oppure eliminando l’app.</p>
<p>L’intenzione compare sulla schermata di blocco e nei widget solo se lo attivi tu.</p>
<h2>Blocco delle app (Tempo di utilizzo)</h2>
<p>Se usi il blocco delle app, scegli le app nell’elenco di sistema di iOS. iOS restituisce a Flowly solo dei riferimenti anonimi: Flowly non sa quali app hai scelto e non riceve dati su come usi il telefono. La selezione resta sul dispositivo.</p>
<h2>Acquisti (Flowly Plus)</h2>
<p>I pagamenti sono gestiti da Apple tramite l’App Store: non ricevo i tuoi dati di pagamento. Per verificare gli acquisti e gli abbonamenti uso RevenueCat, Inc., che riceve un identificativo anonimo generato dall’app, lo storico degli acquisti e dati tecnici come modello del dispositivo, versione di iOS e dell’app. Nessun nome, email o dato delle tue sessioni viene condiviso. La base giuridica è l’esecuzione del contratto di acquisto. Informativa di RevenueCat: <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a>.</p>
<h2>Notifiche</h2>
<p>Gli avvisi di fine fase sono notifiche locali, programmate sul dispositivo. Flowly non usa notifiche push e non ha un server.</p>
<h2>Conservazione e diritti</h2>
<p>I dati locali restano finché non li cancelli. I dati di acquisto presso RevenueCat sono conservati finché servono a gestire i tuoi acquisti. Puoi chiedere accesso, rettifica o cancellazione scrivendo a <a href="mailto:{EMAIL}">{EMAIL}</a>, indicando l’«ID di supporto» che trovi in fondo alle Impostazioni dell’app. Hai anche diritto di reclamo al Garante per la protezione dei dati personali.</p>
<h2>Minori</h2>
<p>Flowly non è rivolta in modo specifico ai minori e non raccoglie consapevolmente dati che li riguardano.</p>
<h2>Modifiche</h2>
<p>Se questa informativa cambia, aggiornerò questa pagina e la data in alto.</p>
</article>""",
    "en": f"""<article class="doc">
<h1>Privacy policy</h1>
<p class="updated">Updated {UPDATED['en']}</p>
<p>Flowly is a focus timer for iPhone made by {DEV} (“I”). This policy explains which data the app processes and why. In short: Flowly has no accounts, shows no ads and collects no usage analytics.</p>
<h2>Controller and contact</h2>
<p>{DEV} — <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Data that stays on your iPhone</h2>
<p>Sessions, history, the intentions you write, preferences and chosen scenes are stored only on the device. They are not sent to me or to anyone else. You can delete them at any time in Settings › Delete local data, or by deleting the app.</p>
<p>Your intention appears on the lock screen and in widgets only if you turn that on.</p>
<h2>App blocking (Screen Time)</h2>
<p>If you use app blocking, you pick apps in iOS’s own system list. iOS gives Flowly only anonymous references: Flowly can’t see which apps you chose and receives no data about how you use your phone. The selection stays on the device.</p>
<h2>Purchases (Flowly Plus)</h2>
<p>Payments are handled by Apple through the App Store: I never receive your payment details. To verify purchases and subscriptions I use RevenueCat, Inc., which receives an anonymous identifier generated by the app, your purchase history and technical data such as device model, iOS and app version. No name, email or session data is shared. The legal basis is the performance of the purchase contract. RevenueCat’s policy: <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a>.</p>
<h2>Notifications</h2>
<p>End-of-phase alerts are local notifications scheduled on the device. Flowly uses no push notifications and has no server.</p>
<h2>Retention and your rights</h2>
<p>Local data stays until you delete it. Purchase data at RevenueCat is kept as long as needed to manage your purchases. You can ask for access, correction or deletion by writing to <a href="mailto:{EMAIL}">{EMAIL}</a> with the “Support ID” shown at the bottom of the app’s Settings. You may also lodge a complaint with your data protection authority.</p>
<h2>Children</h2>
<p>Flowly is not specifically directed at children and does not knowingly collect their data.</p>
<h2>Changes</h2>
<p>If this policy changes, I will update this page and the date above.</p>
</article>""",
}

TERMS = {
    "it": f"""<article class="doc">
<h1>Termini d’uso</h1>
<p class="updated">Aggiornati il {UPDATED['it']}</p>
<p>Usando Flowly accetti questi termini e la <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">licenza d’uso standard di Apple (EULA)</a>, che regola le app scaricate dall’App Store.</p>
<h2>L’app</h2>
<p>Flowly è un timer per organizzare lavoro e pause. Non è un dispositivo medico e non promette risultati su concentrazione o salute.</p>
<h2>Flowly Plus</h2>
<p>Plus sblocca funzioni aggiuntive e si acquista solo tramite l’App Store, con due opzioni: un abbonamento annuale, con eventuale prova gratuita, oppure un acquisto unico per sempre. Prezzi e condizioni sono mostrati nell’app prima dell’acquisto.</p>
<p>L’abbonamento si rinnova automaticamente alla fine di ogni periodo, salvo disdetta almeno 24 ore prima del rinnovo da Impostazioni › il tuo nome › Abbonamenti. Se disdici durante la prova gratuita non ti viene addebitato nulla. Rimborsi e pagamenti sono gestiti da Apple secondo le sue condizioni.</p>
<h2>Responsabilità</h2>
<p>L’app è fornita «così com’è». Faccio del mio meglio perché funzioni bene, ma non posso garantire che sia sempre priva di errori. Alcune funzioni, come notifiche, Attività in tempo reale e blocco delle app, dipendono da iOS e dalle impostazioni del tuo dispositivo.</p>
<h2>Contatti</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a>. Questi termini sono regolati dalla legge italiana, fatti salvi i diritti inderogabili del consumatore.</p>
</article>""",
    "en": f"""<article class="doc">
<h1>Terms of use</h1>
<p class="updated">Updated {UPDATED['en']}</p>
<p>By using Flowly you accept these terms and <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple’s standard licensed application end user license agreement (EULA)</a>, which governs apps downloaded from the App Store.</p>
<h2>The app</h2>
<p>Flowly is a timer for organizing work and breaks. It is not a medical device and makes no promises about focus or health outcomes.</p>
<h2>Flowly Plus</h2>
<p>Plus unlocks extra features and is purchased only through the App Store, with two options: a yearly subscription, possibly with a free trial, or a one-time lifetime purchase. Prices and terms are shown in the app before you buy.</p>
<p>The subscription renews automatically at the end of each period unless cancelled at least 24 hours before renewal in Settings › your name › Subscriptions. If you cancel during the free trial you are not charged. Payments and refunds are handled by Apple under its terms.</p>
<h2>Liability</h2>
<p>The app is provided “as is”. I do my best to make it work well, but I can’t guarantee it will always be error-free. Some features, such as notifications, Live Activities and app blocking, depend on iOS and your device settings.</p>
<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a>. These terms are governed by Italian law, without prejudice to mandatory consumer rights.</p>
</article>""",
}

FAQ = {
    "it": [
        ("Ho cambiato iPhone: come recupero Plus?", "Apri Flowly › Impostazioni › Ripristina acquisti, con lo stesso ID Apple usato per l’acquisto."),
        ("Come disdico l’abbonamento?", "Dall’iPhone: Impostazioni › il tuo nome › Abbonamenti › Flowly. La disdetta va fatta almeno 24 ore prima del rinnovo."),
        ("Non vedo il tempo sulla schermata di blocco.", "Controlla in Impostazioni › Flowly Focus che le Attività in tempo reale siano attive. Il tempo compare quando una fase è in corso."),
        ("Il blocco delle app non si attiva.", "Serve Plus e il permesso di Tempo di utilizzo. In Flowly › Impostazioni › Focus profondo scegli le app e attiva il blocco: la riga sotto l’interruttore mostra lo stato. Le app si bloccano solo durante un focus in corso."),
        ("Le notifiche delle app bloccate arrivano?", "Mentre un’app è bloccata, le sue notifiche potrebbero non arrivare: lo decide iOS. Per silenziare tutto usa una modalità Full immersione e aggiungi Flowly Focus alle app consentite."),
        ("Come cancello i miei dati?", "In Flowly › Impostazioni › Cancella i dati locali. I dati sono solo sul tuo iPhone. Per i dati di acquisto scrivimi indicando l’ID di supporto che trovi in fondo alle Impostazioni."),
    ],
    "en": [
        ("New iPhone: how do I get Plus back?", "Open Flowly › Settings › Restore purchases, with the same Apple ID you bought it with."),
        ("How do I cancel the subscription?", "On your iPhone: Settings › your name › Subscriptions › Flowly. Cancel at least 24 hours before renewal."),
        ("I don’t see the time on the lock screen.", "Check that Live Activities are on in Settings › Flowly Focus. The time appears while a phase is running."),
        ("App blocking doesn’t turn on.", "It needs Plus and Screen Time permission. In Flowly › Settings › Deep focus, choose the apps and turn blocking on: the line under the switch shows the state. Apps are blocked only while a focus is running."),
        ("Do notifications from blocked apps arrive?", "While an app is blocked its notifications may not arrive: iOS decides that. To silence everything, use a Focus mode and add Flowly Focus to the allowed apps."),
        ("How do I delete my data?", "In Flowly › Settings › Delete local data. Your data is only on your iPhone. For purchase data, write to me with the Support ID at the bottom of Settings."),
    ],
}
SUPPORT_H = {"it": ("Supporto", "Domande frequenti. Non trovi la risposta? Scrivimi: rispondo personalmente.", "Scrivimi"), "en": ("Support", "Frequently asked questions. Can’t find your answer? Write to me: I reply personally.", "Write to me")}


def support(lang):
    h, sub, w = SUPPORT_H[lang]
    qs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ[lang])
    body = f'<article class="doc"><h1>{h}</h1><p>{sub}</p>{qs}<p><a href="mailto:{EMAIL}?subject=Flowly%20support">{w} → {EMAIL}</a></p></article>'
    return page(lang, "support.html", f"{h} — Flowly", body)


def main():
    for lang in ("it", "en"):
        out = ROOT if lang == "it" else ROOT / "en"
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(index(lang), encoding="utf-8")
        title_p = "Informativa sulla privacy — Flowly" if lang == "it" else "Privacy policy — Flowly"
        title_t = "Termini d’uso — Flowly" if lang == "it" else "Terms of use — Flowly"
        (out / "privacy.html").write_text(page(lang, "privacy.html", title_p, PRIVACY[lang]), encoding="utf-8")
        (out / "terms.html").write_text(page(lang, "terms.html", title_t, TERMS[lang]), encoding="utf-8")
        (out / "support.html").write_text(support(lang), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    print("built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))


if __name__ == "__main__":
    main()
