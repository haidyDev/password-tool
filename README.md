# Password Tool 🔐

Pieni Python-pohjainen työkalu vahvojen ja satunnaisten salasanojen luomiseen.
Projekti hyödyntää Pythonin `secrets`-moduulia kryptografisesti turvallisten
salasanojen generoimiseksi.

## Projektin tarkoitus

Tämä on harjoitusprojekti, jonka tavoitteena on:

- harjoitella ohjelmoinnin perusrakenteita ja loogista ajattelua
- pohtia, millainen on hyvä ja turvallinen salasana
- rakentaa käytännöllinen komentorivityökalu arjen käyttöön
- tutustua tietoturvan kannalta oikeisiin kirjastoihin ja toimintatapoihin

Projekti kehittyy vaiheittain, ja ratkaisua parannetaan vähitellen oppimisen edetessä.

## Tekninen toteutus (versio 1)

Projektin ensimmäinen versio on toteutettu Pythonilla komentorivityökaluna.

Keskeiset ominaisuudet:
- erillinen `generate_password`-funktio salasanan luontiin
- valittavissa:
  - salasanan pituus
  - käytetäänkö numeroita
  - käytetäänkö erikoismerkkejä
- hyödyntää Pythonin vakiokirjastoja (`secrets` ja `string`)
- varmistaa, että valitut merkkiryhmät sisältyvät salasanaan

Salasanat generoidaan satunnaisesti ilman ennustettavaa rakennetta.

## Käyttö

1. Varmista, että koneella on asennettuna Python 3
2. Aja ohjelma projektikansiosta:

```bash
python password_generator.py
