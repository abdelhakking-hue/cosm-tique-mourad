import os, shutil

# ─── CONFIGURATION DU BUSINESS ───
business = {
    "id": "cosmetique1mourad",
    "name": "Cosmétique 1 Mourad",
    "niche": "Cosmétiques Naturels & Artisanaux",
    "city": "Bab El Oued, Alger",
    "phone": None,           # pas de numéro public → bouton DM Instagram
    "phone2": None,
    "ig": "@cosmetique1mourad",
    "colors": ("#3e7c59", "#efe9dc"),   # vert nature / beige
    "tagline": "Cosmétique artisanale à base d'ingrédients naturels",
    "products": [
        ("Savon d'alep artisanal", "900 DA"),
        ("Huile d'argan pure", "2 800 DA"),
        ("Crème visage bio", "1 800 DA"),
        ("Gommage au café", "1 200 DA"),
    ],
    "extra": "page ingrédients + avis clients",
}

# ─── GÉNÉRATION DU SITE ───
def generate_site(b, out_root="/mnt/agents/output/sites_business_algeriens"):
    d = os.path.join(out_root, b["id"])
    os.makedirs(d, exist_ok=True)

    # photo d'illustration (optionnelle)
    illus_src = "/mnt/agents/output/photos_business2/6_Cosm_tiques_en_poudre_entre_opportunit.png"
    imgs = []
    if os.path.exists(illus_src):
        shutil.copy(illus_src, os.path.join(d, "photo1.png"))
        imgs.append(("photo1.png", "Cosmétiques naturels · illustration"))

    c1, c2 = b["colors"]
    wa = f"https://wa.me/{b['phone']}" if b["phone"] else None
    link = wa or f'https://instagram.com/{b["ig"].lstrip("@")}'
    wa_btn = (f'<a href="{wa}" class="cta">Commander sur WhatsApp</a>' if wa
              else f'<a href="{link}" class="cta">Commander par DM Instagram</a>')

    cards = ""
    for i, (p, pr) in enumerate(b["products"]):
        if i < len(imgs):
            f, cap = imgs[i]
            im = f'<img src="{f}" alt="{cap}" loading="lazy"><p class="cap">{cap}</p>'
        else:
            im = '<div class="img">📷 Photo produit<br>à importer depuis Instagram</div>'
        cards += (f'<div class="prod">{im}<h4>{p}</h4><p class="price">{pr}</p>'
                  f'<a class="order" href="{link}">Commander</a></div>')

    notice = ('<p class="notice">ℹ️ Photo d\'illustration – à remplacer par les photos Instagram du client</p>'
              if imgs else '<p class="notice">⚠️ Importer les photos depuis Instagram</p>')

    tel_html = (f'<p class="tel">📞 <a href="{wa}">{b["phone"]}</a></p>' if b["phone"]
                else '<p class="tel">📩 Commande par message Instagram</p>')

    html = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b['name']} – {b['niche']} à {b['city']}</title>
<meta name="description" content="{b['name']} : {b['tagline']}. {b['city']}. Commandez par WhatsApp ou Instagram.">
<style>
:root{{--c1:{c1};--c2:{c2}}}*{{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Tahoma,sans-serif}}
body{{background:#fff;color:#222}}
header{{background:linear-gradient(135deg,var(--c1),var(--c1)dd);color:#fff;text-align:center;padding:60px 20px}}
header h1{{font-size:2.2em}}header p{{margin-top:10px;opacity:.9}}
.cta{{display:inline-block;margin-top:25px;background:var(--c2);color:var(--c1);padding:14px 30px;border-radius:30px;text-decoration:none;font-weight:bold}}
nav{{position:sticky;top:0;background:var(--c1);text-align:center;padding:12px}}nav a{{color:#fff;text-decoration:none;margin:0 15px;font-size:.95em}}
section{{max-width:1000px;margin:auto;padding:50px 20px}}h2{{color:var(--c1);text-align:center;margin-bottom:30px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}}
.prod{{border:1px solid #eee;border-radius:14px;overflow:hidden;text-align:center;transition:.2s}}
.prod:hover{{box-shadow:0 5px 20px rgba(0,0,0,.1)}}
.prod img{{width:100%;height:200px;object-fit:cover}}
.cap{{font-size:.75em;color:#999;padding:4px}}
.img{{background:var(--c2);padding:40px 0;font-size:1em;color:#999}}
.prod h4{{padding:12px 10px 4px}}.price{{color:var(--c1);font-weight:bold;padding-bottom:8px}}
.order{{display:block;background:var(--c1);color:#fff;text-decoration:none;padding:10px}}
.notice{{text-align:center;margin-top:15px;color:#a60;font-size:.85em}}
.steps{{display:flex;flex-wrap:wrap;gap:15px;justify-content:center}}
.step{{flex:1;min-width:200px;background:var(--c2);border-radius:12px;padding:20px;text-align:center}}
.tel{{text-align:center;font-size:1.1em;margin-top:20px}}
footer{{background:var(--c1);color:#fff;text-align:center;padding:30px 20px}}footer a{{color:var(--c2)}}
@media(max-width:600px){{header h1{{font-size:1.6em}}}}
</style></head><body>
<header><h1>{b['name']}</h1><p>{b['tagline']}</p><p>📍 {b['city']}</p>{wa_btn}</header>
<nav><a href="#catalogue">Catalogue</a><a href="#commander">Comment commander</a><a href="#contact">Contact</a></nav>
<section id="catalogue"><h2>Notre catalogue</h2><div class="grid">{cards}</div>{notice}</section>
<section id="commander" style="background:var(--c2)"><h2>Comment commander ?</h2><div class="steps">
<div class="step"><h3>1️⃣ Choisissez</h3><p>Parcourez le catalogue et notez la référence du produit</p></div>
<div class="step"><h3>2️⃣ Contactez-nous</h3><p>Via WhatsApp ou Instagram (réponse rapide garantie)</p></div>
<div class="step"><h3>3️⃣ Recevez</h3><p>Livraison à domicile, paiement à la livraison (COD)</p></div></div></section>
<section id="contact"><h2>Contact</h2>{tel_html}
<p style="text-align:center;margin-top:10px">📷 Instagram : <a href="https://instagram.com/{b['ig'].lstrip('@')}">{b['ig']}</a></p>
<p style="text-align:center;margin-top:10px">📍 {b['city']} – <a href="https://www.google.com/maps/search/{b['name']} {b['city']}">Voir sur Google Maps</a></p></section>
<footer><p>{b['name']} – {b['niche']}</p><p style="font-size:.8em;margin-top:8px">✨ Module suggéré : {b['extra']}</p></footer>
</body></html>"""

    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Site généré : {d}/index.html")

generate_site(business)