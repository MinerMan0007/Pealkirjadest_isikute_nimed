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
pip install requests
pip install beautifulsoup4
```
## Käivitamine

Rakendus on käsurea (CLI) põhine.

Käivita projekt projekti juurkaustast:

python -m src.app


#### **Programm küsib portaali nime:**

Vali portaal: **delfi**, **postimees**, **ohtuleht**

Väljund

Tulemused salvestatakse kausta output/ domeenipõhiste JSON-failidena:

delfi.json

postimees.json

ohtuleht.json

JSON näidisväljund
```json
[
  {
    "name": "Mari Tamm",
    "headline": "Mari Tamm kandideerib uuesti volikokku",
    "url": "https://www.delfi.ee/artikkel/123456"
  },
  {
    "name": "Karl Johannes Põld",
    "headline": "Karl Johannes Põld lahkub ametist",
    "url": "https://www.postimees.ee/789012"
  }
]
```
### Projektistruktuur
```
Pealkirjadest-isikute-nimed/
├── src/
│   ├── app.py
│   ├── downloader.py
│   ├── parser.py
│   ├── name_extractor.py
│   ├── exporter.py
│   └── __init__.py
├── output/
│   ├── delfi.json
│   ├── postimees.json
│   └── ohtuleht.json
├── requirements.txt
└── README.md
```
