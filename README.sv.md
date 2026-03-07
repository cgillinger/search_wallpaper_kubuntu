# SearchWallpaper — Kubuntu Edition

**Automatisk Bing-bakgrundsbildshanterare för KDE Plasma på Kubuntu / Linux**

[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/plattform-Kubuntu%20%7C%20Linux%20Mint%20KDE-E95420?logo=ubuntu&logoColor=white)](https://kubuntu.org/)
[![KDE Plasma](https://img.shields.io/badge/KDE_Plasma-5%2B-1D99F3?logo=kde&logoColor=white)](https://kde.org/plasma-desktop/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16%2B-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Microsoft Edge](https://img.shields.io/badge/Microsoft_Edge-krävs-0078D7?logo=microsoftedge&logoColor=white)](https://www.microsoft.com/edge)
[![License](https://img.shields.io/badge/licens-Öppen_källkod-brightgreen)](LICENSE)

**[🇬🇧 Read in English](Readme.md)**

---

## Vad är SearchWallpaper?

**SearchWallpaper** hämtar automatiskt högupplösta bakgrundsbilder från Bing Images och sätter dem som skrivbordsbakgrund i KDE Plasma på Kubuntu, Linux Mint KDE eller annat Debian-baserat system med KDE Plasma.

Programmet använder en headless Microsoft Edge-webbläsare (via Selenium) för att söka Bing efter bilder som matchar dina egna söktermer. Varje bild valideras för upplösning (minst 1920×1080, landskapsformat) innan den sätts som bakgrundsbild — så du alltid får vassa, fullskärmsbakgrunder.

> **Specifikt utformat för Kubuntu med KDE Plasma.**
> Inga API-nycklar behövs. Ingen bakgrundsdemon. Kör det när du vill ha en ny bakgrundsbild.

---

## Funktioner

| Funktion | Detaljer |
|---|---|
| **Automatisk bildhämtning** | Söker Bing Images via Selenium + headless Edge |
| **Anpassningsbara söktermer** | Redigera en enkel `.ini`-fil — ingen kodning krävs |
| **Bildvalidering** | Endast landskapsbilder på 1920×1080 px eller mer |
| **Smart filtrering** | Blockera nyckelord (tecknat, människor, ritningar osv.) |
| **Historikhantering** | Håller koll på de senaste 50 bilderna — inga upprepningar |
| **Daglig sökgräns** | Max 50 sökningar/dag för att respektera Bing TOS |
| **Cache-system** | Faller tillbaka till cachade bilder vid nätverksproblem |
| **Detaljerad loggning** | Roterande loggfiler för enkel felsökning |
| **KDE Plasma-integration** | Använder `plasma-apply-wallpaperimage` direkt |

---

## Systemkrav

### Hårdvara
- 4 GB RAM eller mer
- Internetanslutning
- Skärmupplösning 1920×1080 eller högre

### Programvara
- **Kubuntu 20.04 eller senare** (testat på 24.04)
- **KDE Plasma 5 eller 6**
- **Python 3.8+**
- **Microsoft Edge** (stable) — se installation nedan
- **msedgedriver** som matchar din Edge-version — se installation nedan

### Kompatibilitet

| Status | Skrivbordsmiljö |
|---|---|
| ✅ Testat och fungerar | Kubuntu 24.04 med KDE Plasma 5 |
| 🟡 Borde fungera (otestat) | Ubuntu med KDE, Linux Mint KDE, KDE neon, Debian KDE |
| 🟡 Kan fungera med ändringar | GNOME, MATE, Cinnamon (fallback-stöd finns) |
| ❌ Stöds ej | Xfce, LXQt, i3, Sway, Fedora/Arch/Red Hat |

---

## Installation

### Steg 1 — Installera Microsoft Edge

```bash
# Ladda ner Microsoft-signeringsnyckeln
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

# Installera nyckeln
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/

# Lägg till Edge-repository
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# Städa upp
rm microsoft.gpg

# Uppdatera och installera
sudo apt update
sudo apt install microsoft-edge-stable

# Verifiera
microsoft-edge --version
```

---

### Steg 2 — Installera systempaket

```bash
sudo apt install python3-tk python3-pip python3-venv dbus-x11

# Verifiera
python3 --version
```

---

### Steg 3 — Ladda ner och installera EdgeDriver

**msedgedriver måste exakt matcha din Edge-webbläsarversion.**

**Metod A — Via webbläsaren (rekommenderas för nybörjare)**

1. Kolla din Edge-version: `microsoft-edge --version`
2. Gå till: <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>
3. Ladda ner **Linux x64** för din exakta version
4. Installera:

```bash
cd ~/Hämtningar
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

**Metod B — Via terminalen**

```bash
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
cd ~/Hämtningar
wget "https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver/${VERSION}/edgedriver_linux64.zip"
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

> **OBS:** Om den primära CDN:en (`msedgedriver.azureedge.net`) inte är nåbar — vilket kan hända efter VPN-användning på grund av DNS-problem — använd blob storage-URL:en ovan (`msedgewebdriverstorage.blob.core.windows.net`). Det är ett pålitligt alternativ som alltid fungerar.

---

### Steg 4 — Klona repositoryt

```bash
mkdir -p ~/Dokument/Github
cd ~/Dokument/Github
git clone https://github.com/cgillinger/search_wallpaper_kubuntu.git
cd search_wallpaper_kubuntu
```

---

### Steg 5 — Skapa Python virtual environment

```bash
cd ~/Dokument/Github/search_wallpaper_kubuntu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Steg 6 — Första körningen

```bash
source venv/bin/activate
python src/main.py
```

Om allt fungerar:
- Ett litet statusfönster visas kort
- Din skrivbordsbakgrund ändras efter några sekunder
- Fönstret stängs automatiskt

---

## Filstruktur

```
~/.local/share/SearchWallpaper/
├── search_queries.ini       # Dina anpassade söktermer
├── history.json             # Senaste 50 bakgrundsbilder (förhindrar upprepningar)
├── daily_search_count.json  # Daglig räknare (max 50/dag)
├── logs/
│   └── search_wallpaper.log # Roterande logg för felsökning
└── cache/
    └── bing_wallpaper_*.jpg # Nedladdade bakgrundsbilder
```

All data sparas i din hemkatalog enligt [XDG Base Directory-specifikationen](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). Inga sudo-rättigheter behövs för normal drift.

---

## Anpassa söktermer

```bash
nano ~/.local/share/SearchWallpaper/search_queries.ini
```

**Formatregler:** Inga hakparenteser `[]`, inga citattecken `""`, inga avslutande kommatecken.

```ini
[Search]
queries =
    stockholm cityscape wallpaper
    mountain landscape wallpaper
    ocean sunset wallpaper
    northern lights wallpaper

excluded_words =
    people,person,car,cartoon,drawing,sketch,clipart,anime
```

### Exempel på teman

<details>
<summary>🏙️ Stockholm</summary>

```ini
queries =
    stockholm cityscape wallpaper
    stockholm gamla stan wallpaper
    stockholm archipelago wallpaper
    stockholm sunset wallpaper
```
</details>

<details>
<summary>🏔️ Natur och landskap</summary>

```ini
queries =
    mountain landscape wallpaper
    forest nature wallpaper
    ocean sunset wallpaper
    northern lights wallpaper
    waterfall nature wallpaper
```
</details>

<details>
<summary>🌌 Rymden</summary>

```ini
queries =
    galaxy space wallpaper
    nebula wallpaper
    milky way wallpaper
    planet wallpaper
```
</details>

<details>
<summary>🦜 Fåglar (standard)</summary>

```ini
queries =
    pet parrot beautiful wallpaper
    macaw bird wallpaper
    cockatoo portrait wallpaper
```
</details>

<details>
<summary>🚗 Bilar</summary>

```ini
queries =
    sports car wallpaper
    classic car wallpaper
    supercar wallpaper
```
</details>

---

## Daglig användning

### Kör manuellt

```bash
cd ~/Dokument/Github/search_wallpaper_kubuntu
source venv/bin/activate
python src/main.py
```

### Desktop-launcher (rekommenderas)

```bash
cat > ~/.local/share/applications/search-wallpaper.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=SearchWallpaper
Comment=Hämta ny bakgrundsbild från Bing
Exec=/bin/bash -c "cd ~/Dokument/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py"
Icon=preferences-desktop-wallpaper
Terminal=false
Categories=Utility;
EOF

chmod +x ~/.local/share/applications/search-wallpaper.desktop
```

### Shell-alias

Lägg till i `~/.bashrc`:

```bash
alias newwall='cd ~/Dokument/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py'
```

Ladda sedan om: `source ~/.bashrc`

---

## Hantera data

```bash
# Visa nedladdade bilder
ls -lh ~/.local/share/SearchWallpaper/cache/

# Följ loggen i realtid
tail -f ~/.local/share/SearchWallpaper/logs/search_wallpaper.log

# Rensa cache
rm ~/.local/share/SearchWallpaper/cache/*.jpg

# Nollställ daglig räknare
rm ~/.local/share/SearchWallpaper/daily_search_count.json

# Radera historik (börja om)
rm ~/.local/share/SearchWallpaper/history.json

# Backup alla inställningar
cp -r ~/.local/share/SearchWallpaper ~/Dokument/SearchWallpaper-backup-$(date +%Y%m%d)
```

---

## Felsökning

### Problem: Edge har uppdaterats automatiskt och EdgeDriver-versionen matchar inte längre

När Microsoft Edge uppdaterar sig automatiskt kan den installerade `msedgedriver` sluta matcha den nya webbläsarversionen. Programmet detekterar detta och loggar ett tydligt felmeddelande.

**Hur du upptäcker problemet:**

Kontrollera loggfilen efter ett versionsmatchfel:

```bash
tail -50 ~/.local/share/SearchWallpaper/logs/search_wallpaper.log
```

Du ser en rad som:
```
EdgeDriver-versionsmatchfel: Edge=131.0.2903.112, msedgedriver=130.0.2849.68
```

Statusfönstret visar: **"EdgeDriver-version stämmer inte — se loggen för åtgärd"**

**Verifiera båda versionerna manuellt:**

```bash
microsoft-edge --version
/usr/local/bin/msedgedriver --version
# Båda utskrifterna måste visa samma versionsnummer
```

**Åtgärd — ladda ner rätt EdgeDriver:**

Den primära CDN:en (`msedgedriver.azureedge.net`) är ibland otillgänglig på grund av DNS-problem — till exempel efter VPN-användning. Använd den pålitliga blob storage-URL:en istället:

```bash
# Hämta din nuvarande Edge-version
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
echo "Edge-version: $VERSION"

# Ladda ner från blob storage (pålitlig alternativ-URL)
cd ~/Hämtningar
wget "https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver/${VERSION}/edgedriver_linux64.zip"

# Installera
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver

# Verifiera att båda versionerna matchar
microsoft-edge --version
/usr/local/bin/msedgedriver --version
```

---

### Problem: "Edge saknas" trots installation

```bash
which microsoft-edge
microsoft-edge --version
# Om inget resultat — installera om Edge (se Steg 1)
```

### Problem: "msedgedriver kunde inte hittas"

```bash
which msedgedriver
/usr/local/bin/msedgedriver --version
# Om fel — installera om EdgeDriver (se Steg 3)
```

### Problem: `ModuleNotFoundError: No module named 'tkinter'`

```bash
sudo apt install python3-tk
```

### Problem: `externally-managed-environment`

Du har glömt aktivera virtual environment:

```bash
cd ~/Dokument/Github/search_wallpaper_kubuntu
source venv/bin/activate
# Du ska se "(venv)" i din prompt
```

### Problem: Bakgrundsbild ändras inte

```bash
echo $XDG_CURRENT_DESKTOP          # Ska visa "KDE"
which plasma-apply-wallpaperimage  # Måste finnas

# Testa manuellt
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg
```

### Problem: Tolkningsfel i konfigurationsfilen

```bash
cat ~/.local/share/SearchWallpaper/search_queries.ini
# Vanliga fel: hakparenteser [ ], citattecken " ", avslutande kommatecken ,

# Återställ till standard
rm ~/.local/share/SearchWallpaper/search_queries.ini
python src/main.py  # Skapar en ny standardfil
```

---

## Tekniska detaljer

### Arkitektur

```
search_wallpaper_kubuntu/
├── src/
│   ├── api/
│   │   └── bing_scraper.py      # Bing-sökning via Selenium + EdgeDriver
│   ├── config/
│   │   ├── logging_config.py    # Roterande logg-setup
│   │   └── search_config.py     # Söktermshantering
│   ├── utils/
│   │   ├── paths.py             # XDG-kompatibla sökvägar
│   │   └── wallpaper.py         # KDE Plasma-integration
│   └── main.py                  # Startpunkt + GUI-statusfönster
├── requirements.txt
└── README.md
```

### Gränser

| Gräns | Värde | Anledning |
|---|---|---|
| Sökningar per dag | 50 | Respekterar Bing TOS |
| Historikposter | 50 | Förhindrar upprepningar |
| Loggfiler | 3 (roterande) | Håller diskutrymme nere |
| Minsta bildstorlek | 1920×1080 px | Säkerställer Full HD-kvalitet |

### Säkerhet

- Inga API-nycklar eller konton behövs
- All data sparas lokalt i `~/.local/share/SearchWallpaper/`
- Ingen bakgrundsdemon eller schemalagd process
- Respekterar Bings användarvillkor
- Ingen data skickas till tredjepartsservrar

---

## Changelog

### Version 2.1 (2026-03-07)

- **Nytt:** Automatisk EdgeDriver-versionskontroll vid start
- **Nytt:** Tydligt loggmeddelande med åtgärdsinstruktioner vid versionsmatchfel (inkluderar blob storage-URL som pålitligt CDN-alternativ)
- **Nytt:** Användarvänligt statusmeddelande i GUI vid versionsmatchfel

### Version 2.0 — Kubuntu Edition (2025-10-24)

- KDE Plasma-integration via `plasma-apply-wallpaperimage`
- XDG Base Directory-standard för alla datafiler
- GNOME-fallback-stöd
- Plattformsspecifik Edge-detection
- Komplett nybörjarvänlig dokumentation

---

## Bidra

1. Kontrollera loggen: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Verifiera systemkrav
3. Kör de manuella felsökningskommandona ovan
4. Öppna ett [GitHub-issue](https://github.com/cgillinger/search_wallpaper_kubuntu/issues) med din loggutskrift och systeminformation

För kodbidrag: forka repositoryt, skapa en feature-branch, följ befintlig kodstil, testa på Kubuntu och skicka sedan en pull request.

---

## Licens

Öppen källkod för personligt bruk. Det här programmet använder Bing Image Search — vänligen respektera [Microsofts användarvillkor](https://www.microsoft.com/sv-se/servicesagreement/).

---

## Tack till

- **Microsoft Edge** — webbläsare och WebDriver
- **Selenium** — webbautomationsramverk
- **Bing Images** — bildkälla
- **KDE Plasma** — skrivbordsmiljö
- **Python-communityn** — utmärkta bibliotek

---

**Få vackra, högupplösta bakgrundsbilder på din Kubuntu-dator automatiskt.**
