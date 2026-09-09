#!/usr/bin/env python3
"""One template, three languages. Run after editing STRINGS; commits the generated HTML."""
import os, html
ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "es", "ca"]
CSS_VERSION = 9          # bump whenever style.css changes; every generated page picks it up
S = {
"en": dict(lang="en",
  swipe_h="Swipe, like a deck of cards", swipe_k="One card, one decision, one thumb. Tinder for the junk on your Mac — except nothing is ever lost.",
  swipe_keep="Swipe right to keep", swipe_keep_p="The card turns green and stays where it is. Use it for anything you're not sure about — keeping is always free.",
  swipe_trash="Swipe left to trash", swipe_trash_p="The card turns red and joins the review list. It moves to the Trash only when you tap Commit, and undo works even after that.",
  swipe_more="Swipe down to decide later; it comes back at the end of the deck. Tap a card to see it full size. Shake to undo the last swipe.", title="DeckSweep — swipe your Mac clean from your iPhone",
  desc="A Mac helper finds old screenshots, duplicates and forgotten downloads; you swipe through them on your iPhone. Files go to the Trash, nothing leaves your Mac.",
  nav_how="How it works", nav_feat="Features", nav_install="Install", nav_price="Price", nav_faq="FAQ", nav_dl="Download for Mac",
  h1a="Swipe your Mac clean ", h1b="from your iPhone.",
  sub="Old screenshots, duplicate photos, forgotten downloads. DeckSweep finds them on your Mac and deals them to your iPhone as a deck: swipe right to keep, left to trash. Files go to the Trash — never anywhere else.",
  cta_ios="iPhone app · coming to the App Store", note="macOS 14 or later · free · notarized by Apple · iPhone app free for your first 50 files",
  how="How it works", how_k="Four steps. The Mac does the finding, the phone does the deciding, the Trash does the rest.",
  steps=[("The Mac scans","A menu-bar helper looks through Desktop, Downloads, Pictures, Documents and Movies — you choose the folders — and ranks what it finds."),
         ("Pair once","Scan the QR code in that menu with the iPhone app. Phone and Mac talk directly over your Wi‑Fi, encrypted. No account, no cloud."),
         ("Swipe","Right keeps, left trashes, down decides later. Tap for a full-size preview. Duplicate groups show every copy side by side."),
         ("Review, then commit","A list shows exactly what will move, with a toggle to change your mind. Then the files go to the Trash. Undo works even after.")],
  feats=[("See what's reclaimable, by deck","One number for the whole Mac, then decks by kind: screenshots, duplicates, similar photos, large downloads, old installers. Each shows how many files and how much space, and how far you've got."),
         ("Decide in a second","Every card says why it's there — \"Screenshot · 14 months old\" — with the file name, size and folder. Swipe with your thumb or use the buttons; shake to undo."),
         ("Duplicates side by side","Exact copies and near-identical bursts come as one card with every copy visible. The one that stays is marked; tap another to keep that one instead."),
         ("Nothing moves until you say so","Before anything happens you get the full list with a switch per file. Commit sends them to your Mac's Trash and tells you exactly what moved — and what it left alone.")],
  safe="Built to be safe", safe_k="Deleting other people's files is a responsibility. These are the rules the Mac helper enforces, not suggestions.",
  cards=[("Only the folders you choose","Never system files, never other apps' data, never your Photos library, never anything you didn't point it at."),
         ("Trash, never delete","Every file goes to the Trash. Emptying it is a separate step you confirm on the Mac, only within minutes of a commit."),
         ("Nothing leaves your Mac","The phone gets small previews; the Mac gets verdicts. No account, no analytics, no third-party code in either app. <a href=\"privacy/\">Privacy policy</a>."),
         ("Changed files are left alone","Anything modified after the scan is skipped and reported, so a file you just edited can't be swept by an old verdict.")],
  install="Install", install_k="Two apps, two minutes.", mac="Mac helper", iphone="iPhone app",
  mac_steps=["<a href=\"DeckSweep-1.0.dmg\">Download DeckSweep-1.0.dmg</a> and open it.",
             "Drag <b>DeckSweepAgent</b> to <b>Applications</b> and open it from there. It's notarized by Apple, so it opens without warnings.",
             "Find ✦ at the top right of your screen. The first scan runs on its own; the menu shows a QR code.",
             "Optional: <i>Launch at login</i>, and <i>Full Disk Access</i> in System Settings for accurate \"last opened\" dates."],
  ios_steps=["Install DeckSweep from the App Store (link here as soon as it's live).",
             "Open it on the same Wi‑Fi as the Mac and allow <i>Local Network</i> when iOS asks — that's how it finds the Mac.",
             "Tap your Mac, then <b>Scan QR</b> and point the camera at the menu. It reconnects by itself from then on.",
             "No Mac nearby? <b>Try without a Mac</b> runs the whole flow on sample data."],
  price="Price", price_k="The Mac helper is free. The iPhone app is free to try, then one payment.", once="one-time",
  price_p="<b>DeckSweep Unlimited</b> — no limit on files, every Mac you pair, Family Sharing. No subscription.", price_n="Your first 50 files are free. Bought inside the app through your Apple ID.",
  faq="Questions", faq_k="Short answers; more on the <a href=\"support/\">support page</a>.",
  faqs=[("The phone can't find my Mac","Both on the same Wi‑Fi, ✦ in the Mac's menu bar, and <i>Local Network</i> allowed for DeckSweep in iOS Settings."),
        ("Where did the files go?","The Trash on your Mac. Finder → Trash, or <i>Show Trash</i> in the menu. Nothing is deleted until you empty the Trash yourself."),
        ("Can I undo?","Shake the phone for the last swipe; use the review list before committing; after committing, the Mac's menu puts files back as long as they're still in the Trash."),
        ("Does it touch my Photos library?","No. Photo libraries, apps and other packages are never entered."),
        ("Which devices?","macOS 14 Sonoma or later, Apple silicon or Intel. iPhone with iOS 17 or later.")],
  f_privacy="Privacy", f_support="Support", f_contact="Contact",
  privacy_t="DeckSweep privacy policy",
  privacy="DeckSweep does not collect, store or transmit any personal data. The iPhone app and the DeckSweep agent on your Mac talk to each other directly over your own local network, encrypted, and nothing about you or your files leaves your Mac: no file names, no images, no usage data, no identifiers — not to us, not to anyone. There is no account, no analytics and no third-party code in either app. The only information kept on the phone is a pairing key for your Mac, stored in the iOS Keychain, which you can delete by removing the app or by choosing Forget on the Mac. Files the app moves go to your Mac's Trash and nowhere else. Questions: <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>.",
  privacy_d="Last updated 8 September 2026.",
  support_t="DeckSweep support",
  support="Email <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>. Include your macOS and iOS versions and what you were doing; nothing about your files is ever sent to us, so please describe them in your own words.",
  support_h="Common questions",
  support_faq=[("The phone can't find my Mac.","Both must be on the same Wi‑Fi, the DeckSweep icon must be in the Mac's menu bar, and iOS must have allowed <i>Local Network</i> for DeckSweep (Settings → DeckSweep)."),
               ("Where did my files go?","The Trash on your Mac. Nothing is deleted until you empty the Trash yourself."),
               ("How do I unpair a phone?","Click the ✕ next to it in the Mac's menu."),
               ("How do I stop the Mac app?","Menu → Quit, and untick \"Launch at login\".")],
  home="Home"),
"es": dict(lang="es",
  swipe_h="Desliza, como una baraja", swipe_k="Una tarjeta, una decisión, un pulgar. Tinder para lo que sobra en tu Mac, salvo que aquí nunca se pierde nada.",
  swipe_keep="Desliza a la derecha para conservar", swipe_keep_p="La tarjeta se pone verde y el archivo se queda donde está. Úsalo para todo lo que no tengas claro: conservar siempre es gratis.",
  swipe_trash="Desliza a la izquierda para tirar", swipe_trash_p="La tarjeta se pone roja y entra en la lista de revisión. Solo va a la Papelera cuando pulsas Aplicar, y deshacer funciona incluso después.",
  swipe_more="Desliza hacia abajo para decidirlo luego; vuelve al final de la baraja. Toca una tarjeta para verla a tamaño completo. Agita para deshacer el último deslizamiento.", title="DeckSweep — limpia tu Mac deslizando desde el iPhone",
  desc="Un ayudante en el Mac encuentra capturas antiguas, duplicados y descargas olvidadas; tú los repasas deslizando en el iPhone. Los archivos van a la Papelera; nada sale de tu Mac.",
  nav_how="Cómo funciona", nav_feat="Funciones", nav_install="Instalar", nav_price="Precio", nav_faq="Preguntas", nav_dl="Descargar para Mac",
  h1a="Limpia tu Mac ", h1b="desde tu iPhone.",
  sub="Capturas antiguas, fotos duplicadas, descargas olvidadas. DeckSweep las encuentra en tu Mac y te las reparte en el iPhone como una baraja: desliza a la derecha para conservar, a la izquierda para tirar. Los archivos van a la Papelera, nunca a otro sitio.",
  cta_ios="App para iPhone · próximamente en el App Store", note="macOS 14 o posterior · gratis · notarizado por Apple · app de iPhone gratis para tus primeros 50 archivos",
  how="Cómo funciona", how_k="Cuatro pasos. El Mac busca, el teléfono decide, la Papelera hace el resto.",
  steps=[("El Mac analiza","Un ayudante en la barra de menús revisa Escritorio, Descargas, Imágenes, Documentos y Películas (tú eliges las carpetas) y ordena lo que encuentra."),
         ("Vincula una vez","Escanea el código QR de ese menú con la app del iPhone. Teléfono y Mac hablan directamente por tu Wi‑Fi, cifrado. Sin cuenta, sin nube."),
         ("Desliza","Derecha conserva, izquierda tira, abajo lo decides luego. Toca para ver a tamaño completo. Los duplicados salen con todas las copias lado a lado."),
         ("Revisa y aplica","Una lista muestra exactamente qué se moverá, con un interruptor por si cambias de idea. Luego los archivos van a la Papelera. Deshacer funciona incluso después.")],
  feats=[("Cuánto puedes recuperar, por baraja","Un número para todo el Mac y luego barajas por tipo: capturas, duplicados, fotos similares, descargas grandes, instaladores antiguos. Cada una muestra cuántos archivos, cuánto espacio y hasta dónde has llegado."),
         ("Decide en un segundo","Cada tarjeta dice por qué está ahí — «Captura · hace 14 meses» — con nombre, tamaño y carpeta. Desliza con el pulgar o usa los botones; agita para deshacer."),
         ("Duplicados lado a lado","Las copias exactas y las ráfagas casi idénticas llegan como una sola tarjeta con todas las copias visibles. La que se queda está marcada; toca otra para conservar esa."),
         ("Nada se mueve hasta que tú lo digas","Antes de que pase nada tienes la lista completa con un interruptor por archivo. Aplicar los envía a la Papelera del Mac y te dice exactamente qué se movió y qué se dejó en su sitio.")],
  safe="Hecho para ser seguro", safe_k="Borrar archivos ajenos es una responsabilidad. Estas son las reglas que el ayudante del Mac impone, no sugerencias.",
  cards=[("Solo las carpetas que tú eliges","Nunca archivos del sistema, nunca datos de otras apps, nunca tu fototeca, nunca nada que no hayas señalado."),
         ("Papelera, nunca borrar","Todo archivo va a la Papelera. Vaciarla es un paso aparte que confirmas en el Mac, solo en los minutos siguientes a aplicar."),
         ("Nada sale de tu Mac","El teléfono recibe miniaturas; el Mac recibe decisiones. Sin cuenta, sin analíticas, sin código de terceros en ninguna de las dos apps. <a href=\"privacy/\">Política de privacidad</a>."),
         ("Los archivos modificados se respetan","Lo que haya cambiado después del análisis se omite y se avisa, así un archivo que acabas de editar no puede irse por una decisión antigua.")],
  install="Instalar", install_k="Dos apps, dos minutos.", mac="Ayudante para Mac", iphone="App para iPhone",
  mac_steps=["<a href=\"../DeckSweep-1.0.dmg\">Descarga DeckSweep-1.0.dmg</a> y ábrelo.",
             "Arrastra <b>DeckSweepAgent</b> a <b>Aplicaciones</b> y ábrelo desde ahí. Está notarizado por Apple, así que abre sin avisos.",
             "Busca ✦ arriba a la derecha de la pantalla. El primer análisis arranca solo; el menú muestra un código QR.",
             "Opcional: <i>Abrir al iniciar sesión</i>, y <i>Acceso total al disco</i> en Ajustes del Sistema para fechas de «última apertura» exactas."],
  ios_steps=["Instala DeckSweep desde el App Store (el enlace estará aquí en cuanto se publique).",
             "Ábrela en la misma Wi‑Fi que el Mac y permite <i>Red local</i> cuando iOS lo pida: así encuentra el Mac.",
             "Toca tu Mac, luego <b>Escanear QR</b> y apunta la cámara al menú. A partir de ahí se reconecta sola.",
             "¿Sin Mac a mano? <b>Probar sin Mac</b> recorre todo el flujo con datos de ejemplo."],
  price="Precio", price_k="El ayudante para Mac es gratis. La app de iPhone es gratis para probar, y luego un solo pago.", once="pago único",
  price_p="<b>DeckSweep Unlimited</b>: sin límite de archivos, todos los Mac que vincules, En familia. Sin suscripción.", price_n="Tus primeros 50 archivos son gratis. Se compra dentro de la app con tu ID de Apple.",
  faq="Preguntas", faq_k="Respuestas cortas; más en la <a href=\"support/\">página de soporte</a>.",
  faqs=[("El teléfono no encuentra mi Mac","Los dos en la misma Wi‑Fi, ✦ en la barra de menús del Mac, y <i>Red local</i> permitida para DeckSweep en Ajustes de iOS."),
        ("¿Adónde fueron los archivos?","A la Papelera de tu Mac. Finder → Papelera, o <i>Mostrar la Papelera</i> en el menú. Nada se borra hasta que vacíes la Papelera tú mismo."),
        ("¿Puedo deshacer?","Agita el teléfono para el último deslizamiento; usa la lista de revisión antes de aplicar; después de aplicar, el menú del Mac devuelve los archivos mientras sigan en la Papelera."),
        ("¿Toca mi fototeca?","No. Nunca entra en fototecas, apps ni otros paquetes."),
        ("¿En qué dispositivos?","macOS 14 Sonoma o posterior, Apple silicon o Intel. iPhone con iOS 17 o posterior.")],
  f_privacy="Privacidad", f_support="Soporte", f_contact="Contacto",
  privacy_t="Política de privacidad de DeckSweep",
  privacy="DeckSweep no recopila, almacena ni transmite ningún dato personal. La app del iPhone y el agente DeckSweep de tu Mac se comunican directamente a través de tu propia red local, cifrada, y nada sobre ti ni sobre tus archivos sale de tu Mac: ni nombres de archivo, ni imágenes, ni datos de uso, ni identificadores; ni a nosotros ni a nadie. No hay cuenta, ni analíticas, ni código de terceros en ninguna de las dos apps. La única información que guarda el teléfono es una clave de vinculación con tu Mac, en el Llavero de iOS, que puedes eliminar borrando la app o eligiendo «Olvidar» en el Mac. Los archivos que la app mueve van a la Papelera de tu Mac y a ningún otro sitio. Preguntas: <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>.",
  privacy_d="Última actualización: 8 de septiembre de 2026.",
  support_t="Soporte de DeckSweep",
  support="Escribe a <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>. Indica tus versiones de macOS e iOS y qué estabas haciendo; nunca se nos envía nada sobre tus archivos, así que descríbelos con tus palabras.",
  support_h="Preguntas frecuentes",
  support_faq=[("El teléfono no encuentra mi Mac.","Los dos deben estar en la misma Wi‑Fi, el icono de DeckSweep en la barra de menús del Mac, y iOS debe tener permitida la <i>Red local</i> para DeckSweep (Ajustes → DeckSweep)."),
               ("¿Adónde fueron mis archivos?","A la Papelera de tu Mac. Nada se borra hasta que vacíes la Papelera tú mismo."),
               ("¿Cómo desvinculo un teléfono?","Pulsa la ✕ junto a él en el menú del Mac."),
               ("¿Cómo detengo la app del Mac?","Menú → Salir, y desmarca «Abrir al iniciar sesión».")],
  home="Inicio"),
"ca": dict(lang="ca",
  swipe_h="Llisca, com una baralla de cartes", swipe_k="Una targeta, una decisió, un polze. Tinder per al que sobra al teu Mac, només que aquí mai no es perd res.",
  swipe_keep="Llisca a la dreta per conservar", swipe_keep_p="La targeta es torna verda i el fitxer es queda on és. Fes-ho servir per a tot el que no tinguis clar: conservar sempre és gratis.",
  swipe_trash="Llisca a l'esquerra per llençar", swipe_trash_p="La targeta es torna vermella i entra a la llista de revisió. Només va a la Paperera quan prems Aplica, i desfer funciona fins i tot després.",
  swipe_more="Llisca cap avall per decidir-ho després; torna al final de la baralla. Toca una targeta per veure-la a mida completa. Sacseja per desfer l'últim lliscament.", title="DeckSweep — neteja el teu Mac lliscant des de l'iPhone",
  desc="Un ajudant al Mac troba captures antigues, duplicats i baixades oblidades; tu els repasses lliscant a l'iPhone. Els fitxers van a la Paperera; res no surt del teu Mac.",
  nav_how="Com funciona", nav_feat="Funcions", nav_install="Instal·lar", nav_price="Preu", nav_faq="Preguntes", nav_dl="Baixa per a Mac",
  h1a="Neteja el teu Mac ", h1b="des del teu iPhone.",
  sub="Captures antigues, fotos duplicades, baixades oblidades. DeckSweep les troba al teu Mac i te les reparteix a l'iPhone com una baralla: llisca a la dreta per conservar, a l'esquerra per llençar. Els fitxers van a la Paperera, mai enlloc més.",
  cta_ios="App per a iPhone · aviat a l'App Store", note="macOS 14 o posterior · gratuït · notaritzat per Apple · app d'iPhone gratuïta per als teus primers 50 fitxers",
  how="Com funciona", how_k="Quatre passos. El Mac cerca, el telèfon decideix, la Paperera fa la resta.",
  steps=[("El Mac analitza","Un ajudant a la barra de menús revisa Escriptori, Baixades, Imatges, Documents i Pel·lícules (tu tries les carpetes) i ordena el que troba."),
         ("Vincula un cop","Escaneja el codi QR d'aquest menú amb l'app de l'iPhone. Telèfon i Mac parlen directament per la teva Wi‑Fi, xifrat. Sense compte, sense núvol."),
         ("Llisca","Dreta conserva, esquerra llença, avall ho decideixes després. Toca per veure-ho a mida completa. Els duplicats surten amb totes les còpies costat per costat."),
         ("Revisa i aplica","Una llista mostra exactament què es mourà, amb un interruptor per si canvies d'idea. Després els fitxers van a la Paperera. Desfer funciona fins i tot després.")],
  feats=[("Quant pots recuperar, per baralla","Un número per a tot el Mac i després baralles per tipus: captures, duplicats, fotos similars, baixades grans, instal·ladors antics. Cadascuna mostra quants fitxers, quant espai i fins on has arribat."),
         ("Decideix en un segon","Cada targeta diu per què hi és — «Captura · fa 14 mesos» — amb nom, mida i carpeta. Llisca amb el polze o fes servir els botons; sacseja per desfer."),
         ("Duplicats costat per costat","Les còpies exactes i les ràfegues gairebé idèntiques arriben com una sola targeta amb totes les còpies visibles. La que es queda està marcada; toca'n una altra per conservar aquella."),
         ("Res no es mou fins que tu ho diguis","Abans que passi res tens la llista completa amb un interruptor per fitxer. Aplicar els envia a la Paperera del Mac i et diu exactament què s'ha mogut i què s'ha deixat al seu lloc.")],
  safe="Fet per ser segur", safe_k="Esborrar fitxers d'altri és una responsabilitat. Aquestes són les regles que l'ajudant del Mac imposa, no suggeriments.",
  cards=[("Només les carpetes que tu tries","Mai fitxers del sistema, mai dades d'altres apps, mai la teva fototeca, mai res que no hagis assenyalat."),
         ("Paperera, mai esborrar","Tot fitxer va a la Paperera. Buidar-la és un pas a part que confirmes al Mac, només als minuts següents d'aplicar."),
         ("Res no surt del teu Mac","El telèfon rep miniatures; el Mac rep decisions. Sense compte, sense analítiques, sense codi de tercers a cap de les dues apps. <a href=\"privacy/\">Política de privadesa</a>."),
         ("Els fitxers modificats es respecten","El que hagi canviat després de l'anàlisi s'omet i s'avisa, així un fitxer que acabes d'editar no pot marxar per una decisió antiga.")],
  install="Instal·lar", install_k="Dues apps, dos minuts.", mac="Ajudant per a Mac", iphone="App per a iPhone",
  mac_steps=["<a href=\"../DeckSweep-1.0.dmg\">Baixa DeckSweep-1.0.dmg</a> i obre'l.",
             "Arrossega <b>DeckSweepAgent</b> a <b>Aplicacions</b> i obre'l des d'allà. Està notaritzat per Apple, així que s'obre sense avisos.",
             "Busca ✦ a dalt a la dreta de la pantalla. La primera anàlisi arrenca sola; el menú mostra un codi QR.",
             "Opcional: <i>Obre en iniciar sessió</i>, i <i>Accés total al disc</i> a Configuració del Sistema per a dates d'«última obertura» exactes."],
  ios_steps=["Instal·la DeckSweep des de l'App Store (l'enllaç serà aquí quan es publiqui).",
             "Obre-la a la mateixa Wi‑Fi que el Mac i permet <i>Xarxa local</i> quan iOS ho demani: així troba el Mac.",
             "Toca el teu Mac, després <b>Escaneja el QR</b> i apunta la càmera al menú. A partir d'aquí es reconnecta sola.",
             "Sense Mac a mà? <b>Prova sense Mac</b> recorre tot el flux amb dades d'exemple."],
  price="Preu", price_k="L'ajudant per a Mac és gratuït. L'app d'iPhone és gratuïta per provar, i després un sol pagament.", once="pagament únic",
  price_p="<b>DeckSweep Unlimited</b>: sense límit de fitxers, tots els Mac que vinculis, En família. Sense subscripció.", price_n="Els teus primers 50 fitxers són gratuïts. Es compra dins de l'app amb el teu ID d'Apple.",
  faq="Preguntes", faq_k="Respostes curtes; més a la <a href=\"support/\">pàgina de suport</a>.",
  faqs=[("El telèfon no troba el meu Mac","Tots dos a la mateixa Wi‑Fi, ✦ a la barra de menús del Mac, i <i>Xarxa local</i> permesa per a DeckSweep a la Configuració d'iOS."),
        ("On han anat els fitxers?","A la Paperera del teu Mac. Finder → Paperera, o <i>Mostra la Paperera</i> al menú. Res no s'esborra fins que buidis la Paperera tu mateix."),
        ("Puc desfer?","Sacseja el telèfon per a l'últim lliscament; fes servir la llista de revisió abans d'aplicar; després d'aplicar, el menú del Mac retorna els fitxers mentre encara siguin a la Paperera."),
        ("Toca la meva fototeca?","No. Mai no entra a fototeques, apps ni altres paquets."),
        ("En quins dispositius?","macOS 14 Sonoma o posterior, Apple silicon o Intel. iPhone amb iOS 17 o posterior.")],
  f_privacy="Privadesa", f_support="Suport", f_contact="Contacte",
  privacy_t="Política de privadesa de DeckSweep",
  privacy="DeckSweep no recull, emmagatzema ni transmet cap dada personal. L'app de l'iPhone i l'agent DeckSweep del teu Mac es comuniquen directament a través de la teva pròpia xarxa local, xifrada, i res sobre tu ni sobre els teus fitxers no surt del teu Mac: ni noms de fitxer, ni imatges, ni dades d'ús, ni identificadors; ni a nosaltres ni a ningú. No hi ha compte, ni analítiques, ni codi de tercers a cap de les dues apps. L'única informació que guarda el telèfon és una clau de vinculació amb el teu Mac, al Clauer d'iOS, que pots eliminar esborrant l'app o triant «Oblida» al Mac. Els fitxers que l'app mou van a la Paperera del teu Mac i enlloc més. Preguntes: <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>.",
  privacy_d="Última actualització: 8 de setembre de 2026.",
  support_t="Suport de DeckSweep",
  support="Escriu a <a href=\"mailto:a.estevez@gmail.com\">a.estevez@gmail.com</a>. Indica les teves versions de macOS i iOS i què estaves fent; mai no se'ns envia res sobre els teus fitxers, així que descriu-los amb les teves paraules.",
  support_h="Preguntes freqüents",
  support_faq=[("El telèfon no troba el meu Mac.","Tots dos han de ser a la mateixa Wi‑Fi, la icona de DeckSweep a la barra de menús del Mac, i iOS ha de tenir permesa la <i>Xarxa local</i> per a DeckSweep (Configuració → DeckSweep)."),
               ("On han anat els meus fitxers?","A la Paperera del teu Mac. Res no s'esborra fins que buidis la Paperera tu mateix."),
               ("Com desvinculo un telèfon?","Prem la ✕ al costat seu al menú del Mac."),
               ("Com aturo l'app del Mac?","Menú → Surt, i desmarca «Obre en iniciar sessió».")],
  home="Inici"),
}
NAMES = {"en": "English", "es": "Español", "ca": "Català"}

def prefix(lang): return "" if lang == "en" else "../"      # asset paths from /es/ and /ca/
def href(lang, page=""):                                     # absolute-ish link to a page in a language
    base = "/" if lang == "en" else f"/{lang}/"
    return base + page

def head(t, lang, page):
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="https://decksweep.securlabs.net{href(l, page)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="https://decksweep.securlabs.net{href("en", page)}">'
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{t["title"]}</title><meta name="description" content="{html.escape(t["desc"])}">{alts}'
            f'<link rel="icon" href="{prefix(lang)}img/icon.png"><link rel="stylesheet" href="{prefix(lang)}style.css?v={CSS_VERSION}"></head><body>')

def nav(t, lang, page, doc=False):
    p = prefix(lang)
    switch = "".join(f'<a class="{"on" if l == lang else ""}" href="{href(l, page)}" lang="{l}" hreflang="{l}" title="{NAMES[l]}" aria-label="{NAMES[l]}">{l.upper()}</a>' for l in LANGS)
    links = "" if doc else (f'<div class="links"><a href="#how">{t["nav_how"]}</a><a href="#features">{t["nav_feat"]}</a>'
                            f'<a href="#install">{t["nav_install"]}</a><a href="#price">{t["nav_price"]}</a><a href="#faq">{t["nav_faq"]}</a></div>')
    dl = "" if doc else f'<a class="btn small dl" href="{p}DeckSweep-1.0.dmg" aria-label="{t["nav_dl"]}"><span class="full">{t["nav_dl"]}</span><span class="short">Mac ↓</span></a>'
    # Phones: the section links live in a hamburger (a <details>, no JavaScript needed).
    menu = "" if doc else (f'<details class="menu"><summary aria-label="Menu">☰</summary><div>'
                           f'<a href="#how">{t["nav_how"]}</a><a href="#swipe">{t["swipe_h"]}</a><a href="#features">{t["nav_feat"]}</a>'
                           f'<a href="#install">{t["nav_install"]}</a><a href="#price">{t["nav_price"]}</a><a href="#faq">{t["nav_faq"]}</a></div></details>')
    return f'<nav><div class="wrap">{menu}<a class="brand" href="{href(lang)}"><img src="{p}img/icon.png" alt=""><span>DeckSweep</span></a>{links}<div class="langs">{switch}</div>{dl}</div></nav>'

def footer(t, lang):
    return (f'<footer><div class="wrap"><span>© 2026 Securlabs</span><a href="{href(lang,"privacy/")}">{t["f_privacy"]}</a>'
            f'<a href="{href(lang,"support/")}">{t["f_support"]}</a><a href="mailto:a.estevez@gmail.com">{t["f_contact"]}</a></div></footer></body></html>')

def landing(t, lang):
    p = prefix(lang); s = t
    steps = "".join(f'<div class="step"><div class="n">{i+1}</div><h3>{h}</h3><p>{b}</p></div>' for i,(h,b) in enumerate(s["steps"]))
    imgs = ["01-home","02-swipe","03-group","04-review"]
    feats = "".join(f'<div class="feature"><div class="shot"><div class="phone"><img src="{p}img/{imgs[i]}.png" alt=""></div></div><div><h3>{h}</h3><p>{b}</p></div></div>' for i,(h,b) in enumerate(s["feats"]))
    priv = 'href="' + href(lang, "privacy/") + '"'
    cards = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, b.replace('href="privacy/"', priv)) for h, b in s["cards"])
    dmg = 'href="' + p + 'DeckSweep'
    mac = "".join("<li>%s</li>" % x.replace('href="../DeckSweep', dmg).replace('href="DeckSweep', dmg) for x in s["mac_steps"])
    ios = "".join(f"<li>{x}</li>" for x in s["ios_steps"])
    faqs = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in s["faqs"])
    faq_k = s["faq_k"].replace('href="support/"', f'href="{href(lang,"support/")}"')
    return (head(s, lang, "") + nav(s, lang, "") +
      f'<header class="hero"><div class="wrap"><div><h1>{s["h1a"]}<span>{s["h1b"]}</span></h1><p class="sub">{s["sub"]}</p>'
      f'<div class="cta"><a class="btn" href="{p}DeckSweep-1.0.dmg">{s["nav_dl"]}</a><a class="btn ghost" href="#install">{s["cta_ios"]}</a><span class="note">{s["note"]}</span></div></div>'
      f'<div class="phones"><div class="phone back"><img src="{p}img/01-home.png" alt=""></div><div class="phone front"><img src="{p}img/02-swipe.png" alt=""></div></div></div></header>'
      f'<section id="how"><div class="wrap"><h2>{s["how"]}</h2><p class="kicker">{s["how_k"]}</p><div class="steps">{steps}</div></div></section>'
      f'<section id="swipe" class="alt"><div class="wrap"><h2>{s["swipe_h"]}</h2><p class="kicker">{s["swipe_k"]}</p>'
      f'<div class="swipe"><figure><div class="phone"><img src="{p}img/swipe-trash.png" alt=""></div><h3 class="trash">{s["swipe_trash"]}</h3><p>{s["swipe_trash_p"]}</p></figure>'
      f'<figure><div class="phone"><img src="{p}img/swipe-keep.png" alt=""></div><h3 class="keep">{s["swipe_keep"]}</h3><p>{s["swipe_keep_p"]}</p></figure></div>'
      f'<p class="more">{s["swipe_more"]}</p></div></section>'
      f'<section id="features"><div class="wrap">{feats}</div></section>'
      f'<section><div class="wrap"><h2>{s["safe"]}</h2><p class="kicker">{s["safe_k"]}</p><div class="cards">{cards}</div></div></section>'
      f'<section id="install" class="alt"><div class="wrap"><h2>{s["install"]}</h2><p class="kicker">{s["install_k"]}</p><div class="install"><div class="card"><h3>{s["mac"]}</h3><ol>{mac}</ol></div><div class="card"><h3>{s["iphone"]}</h3><ol>{ios}</ol></div></div></div></section>'
      f'<section id="price"><div class="wrap"><h2 style="text-align:center">{s["price"]}</h2><p class="kicker" style="text-align:center">{s["price_k"]}</p><div class="price"><div class="big">9,99 € <small>{s["once"]}</small></div><p>{s["price_p"]}</p><p class="note" style="color:var(--muted);font-size:.9rem">{s["price_n"]}</p></div></div></section>'
      f'<section id="faq" class="alt"><div class="wrap"><h2>{s["faq"]}</h2><p class="kicker">{faq_k}</p>{faqs}</div></section>' + footer(s, lang))

def doc(t, lang, page, title, body):
    return head(t, lang, page) + nav(t, lang, page, doc=True) + f'<main class="doc"><h1>{title}</h1>{body}</main>' + footer(t, lang)

for lang in LANGS:
    t = S[lang]; d = ROOT if lang == "en" else os.path.join(ROOT, lang)
    os.makedirs(os.path.join(d, "privacy"), exist_ok=True); os.makedirs(os.path.join(d, "support"), exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(landing(t, lang))
    open(os.path.join(d, "privacy", "index.html"), "w").write(doc(t, lang, "privacy/", t["privacy_t"], f'<p>{t["privacy"]}</p><p class="muted">{t["privacy_d"]}</p>'))
    sf = "".join(f'<p><b>{q}</b> {a}</p>' for q,a in t["support_faq"])
    open(os.path.join(d, "support", "index.html"), "w").write(doc(t, lang, "support/", t["support_t"], f'<p>{t["support"]}</p><h2>{t["support_h"]}</h2>{sf}'))
    print("built", lang)
