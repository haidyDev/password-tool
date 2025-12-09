# Password Generator 🔐

Tämä on pieni harjoitusprojekti, jossa ideana on rakentaa työkalu vahvojen salasanojen luomiseen.

Tavoitteita tässä projektissa:

- harjoitella ohjelmoinnin perusajattelua ja rakenteita
- pohtia, millainen on hyvä ja turvallinen salasana
- rakentaa työkalu, jota olisi helppo käyttää arjessa

Projektin tekninen toteutus voi vaihdella eri vaiheissa.  
Tarkoitus on kokeilla erilaisia tapoja ratkaista sama ongelma ja kehittää ratkaisua vähitellen eteenpäin.

Lisään tarkempaa dokumentaatiota ja teknisiä yksityiskohtia sitä mukaa, kun projekti etenee.

---

## Tekninen toteutus (versio 1)

Projektin ensimmäinen versio on toteutettu Pythonilla komentorivityökaluna.

Pääkohdat:

- erillinen `generate_password`-funktio salasanan luontiin
- valittavissa:
  - salasanan pituus
  - käytetäänkö numeroita
  - käytetäänkö erikoismerkkejä
- hyödyntää Pythonin vakiokirjastoja (`random` ja `string`)

---

## Käyttö

1. Varmista, että koneella on asennettuna **Python 3**.
2. Aja ohjelma projektikansiosta:

```bash
python password_generator.py
