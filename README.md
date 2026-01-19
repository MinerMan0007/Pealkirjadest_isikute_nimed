# Pealkirjadest isikute nimede leidmine

## Projekti kirjeldus

See projekt on Pythonis kirjutatud rakendus, mis laeb Eesti uudisteportaalide  
(**delfi.ee**, **postimees.ee**, **ohtuleht.ee**) avalehe ning otsib uudiste  
pealkirjadest inimeste nimesid.  

Leitud nimed seotakse vastava pealkirja ja artikli URL-iga ning salvestatakse  
JSON-faili domeenipõhiselt.

Projekt kasutab objektorienteeritud programmeerimist (OOP) ning HTML-i  
parsimiseks BeautifulSoup4 teeki.

---

## Nõuded

- Python **3.10** või uuem
- Internetiühendus
- Vajalikud paketid:
  - `requests`
  - `beautifulsoup4`

---

## Paigaldus

### 1. Projekti kloonimine

```bash
git clone <repo_url>
cd Pealkirjadest-isikute-nimed
```
### 2. Pythoni virtuaalkeskkonna loomine
```bash
python -m venv venv
```
### 3. Pythoni virtuaalkeskkonna aktiveerimine

#### Windows
```
venv\Scripts\activate
```

#### macOS / Linux
```
source venv/bin/activate
```
### 4. Vajalikud paketid
```bash
pip install -r requirements.txt
```
## Käivitamine

Rakendus on käsurea (CLI) põhine ja töötab kõikide portaalidega, mille URL-id on kirjas config/websites.txt failis.

### 1. Veebilehtede lisamine

Kuna veebilehtede aadressid on nüüd eraldi failis, saad neid väga lihtsalt lisada:

Ava fail config/websites.txt

Lisa iga veebileht uuele reale, näiteks:
```
https://www.delfi.ee
https://kroonika.delfi.ee
https://www.postimees.ee
https://www.ohtuleht.ee
```
siia saab veel lisada weebilehti aga kõik ei tööta 100% sest mõnedel lehteel on bot kaitse et see koodi siis ei tööta
2. Rakenduse käivitamine

Käivita projekt projekti juurkaustast:
```
python -m src.app
```

Kuna veebilehti saab hõlpsasti juurde lisada, töötab rakendus automaatselt kõigi veebilehtedega, mis on config/websites.txt failis.

### Väljund:

Programm kogub iga portaali pealkirjad ja otsib neist inimeste nimesid. Leitud nimed seotakse vastava pealkirja ja artikli URL-iga ning salvestatakse domeenipõhisesse JSON faili, näiteks:
```
json_files/
├── delfi.json
├── kroonika.json
├── postimees.json
└── ohtuleht.json
```

Tulemuste kohta prinditakse järgmine teave:
```
Uudiste nimede koguja käivitub...

Töötlen veebilehte: https://www.delfi.ee
Leitud 42 kirjet.

Töötlen veebilehte: https://kroonika.delfi.ee
Leitud 18 kirjet.
```