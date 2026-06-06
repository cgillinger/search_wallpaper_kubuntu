# SearchWallpaper - Linux Edition

**[🇬🇧 Read in English](README.md)**

---

## 🐧 Automatisk bakgrundsbildshanterare för Linux

SearchWallpaper är ett program som automatiskt hämtar och sätter slumpmässiga bakgrundsbilder på din Linux-dator. Programmet söker på Bing efter bilder baserat på söktermer som du själv kan anpassa. Det är särskilt utformat för att hitta högkvalitativa bilder i rätt storlek för moderna skärmar.

**Denna version stöder flera Linux-skrivbordsmiljöer.**

## 🎯 Funktioner

- ✅ **Automatisk bildhämtning** från Bing Images
- ✅ **Anpassningsbara söktermer** via konfigurationsfil
- ✅ **Bildvalidering** - endast högkvalitativa bilder i landskapsformat (1920x1080+)
- ✅ **Smart filtrering** - undvik teckningar, cartoons, människor etc.
- ✅ **Historikhantering** - inga dubbletter av nyligen använda bilder
- ✅ **Daglig sökgräns** - respekterar Bing TOS (max 50/dag)
- ✅ **Cache-system** - återanvänder bilder vid nätverksproblem
- ✅ **Detaljerad loggning** - enkel felsökning
- ✅ **Multi-DE stöd** - KDE Plasma, Cinnamon, MATE, GNOME

---

## 📋 Systemkrav

### Hårdvara
- Modern dator med minst 4GB RAM
- Internetanslutning
- Skärmupplösning minst 1920x1080

### Programvara
- **Ubuntu-baserad Linux** (Ubuntu 20.04+, Kubuntu, Linux Mint 20+)
- **Skrivbordsmiljöer som stöds:**
  - **Cinnamon** (Linux Mint standard)
  - **KDE Plasma 5/6**
  - **MATE Desktop**
  - **GNOME/Unity**
- **Python 3.8+**
- **Microsoft Edge** (installationsinstruktioner nedan)

### Kompatibilitet

**✅ Testat och fungerar:**
- **Linux Mint 21/22 med Cinnamon**
- **Kubuntu 24.04 med KDE Plasma 5**
- **Ubuntu MATE 22.04/24.04**
- **Ubuntu 22.04/24.04 med GNOME**

**✅ Borde fungera:**
- Linux Mint KDE Edition
- KDE neon
- Ubuntu Unity
- Debian med stödd skrivbordsmiljö

**🟡 Kan fungera med ändringar:**
- Andra Debian-baserade distributioner
- Xfce (kräver manuell gsettings-konfiguration)

**❌ Fungerar INTE:**
- LXQt, i3, Sway (ingen standard bakgrunds-API)
- Red Hat/Fedora/Arch Linux (kräver annat paketformat)

---

## 🚀 Installation

### Steg 1: Installera Microsoft Edge

Öppna terminalen (`Ctrl+Alt+T`) och kör:

```bash
# Ladda ner Microsoft-signeringsnyckeln
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

# Installera nyckeln
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/

# Lägg till Edge-repository
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# Ta bort temporär nyckel
rm microsoft.gpg

# Uppdatera och installera
sudo apt update
sudo apt install microsoft-edge-stable

# Verifiera installation
microsoft-edge --version
```

---

### Steg 2: Installera systempaket

```bash
# Installera nödvändiga paket
sudo apt install python3-tk python3-pip python3-venv dbus-x11

# Verifiera Python
python3 --version
```

---

### Steg 3: EdgeDriver — sköts automatiskt

**Du behöver inte installera msedgedriver manuellt.**

Appen använder Selenium Manager (inbyggt i Selenium 4.16+), som automatiskt laddar
ner rätt `msedgedriver` för din installerade Edge-version och håller den i synk varje
gång Edge uppdateras. Drivern cachas under `~/.cache/selenium/`.

> ⚠️ **Lägg inte en `msedgedriver`-binär i `/usr/local/bin/` (eller någon annanstans
> på din PATH).** En manuellt installerad driver blir föråldrad varje gång Edge
> uppdateras och orsakar ett versions-mismatch-fel (`SessionNotCreatedException`).
> Om du har en kvar från en äldre installation, ta bort den:
>
> ```bash
> sudo rm -f /usr/local/bin/msedgedriver
> ```

Inget att göra här — fortsätt bara till nästa steg.

---

### Steg 4: Hämta projektet

```bash
# Skapa projektmapp (anpassa efter din språkinställning)
mkdir -p ~/Dokument/Github  # eller ~/Documents/Github
cd ~/Dokument/Github

# Klona eller ladda ner projektet
# Om du har git:
git clone https://github.com/YOUR_REPO/search_wallpaper.git
cd search_wallpaper

# Om du laddade ner ZIP:
# Packa upp till ~/Dokument/Github/search_wallpaper
```

---

### Steg 5: Skapa virtual environment

```bash
# Gå till projektmappen
cd ~/Dokument/Github/search_wallpaper

# Skapa virtual environment
python3 -m venv venv

# Aktivera (du ska se "(venv)" i terminalen)
source venv/bin/activate

# Installera Python-paket
pip install -r requirements.txt
```

---

### Steg 6: Första testkörningen

```bash
# Aktivera venv om inte redan aktiverat
source venv/bin/activate

# Kör programmet
python src/main.py
```

**Om allt fungerar:**
- Ett GUI-fönster visas med "Söker efter bilder..."
- Efter några sekunder ändras din bakgrundsbild
- Fönstret stängs automatiskt

---

## 📁 Filstruktur

Programmet skapar filer i din hemkatalog enligt XDG Base Directory-standard:

```
~/.local/share/SearchWallpaper/
├── search_queries.ini    # Dina anpassade söktermer
├── history.json         # Historik (senaste 50 bilderna)
├── daily_search_count.json  # Räknare (max 50/dag)
├── logs/
│   └── search_wallpaper.log  # Loggfil för felsökning
└── cache/
    └── bing_wallpaper_*.jpg  # Nedladdade bilder
```

**Varför denna plats?**
- Följer Linux XDG-standard
- Inga sudo-rättigheter behövs
- Separerad från systemfiler
- Lätt att rensa och återställa

---

## 🎨 Anpassa söktermer

### Hitta konfigurationsfilen

```bash
# Öppna i textredigerare
nano ~/.local/share/SearchWallpaper/search_queries.ini

# Eller öppna mappen i filhanteraren (tryck Ctrl+H för att visa dolda mappar)
# Filhanterare per skrivbordsmiljö:

# Cinnamon (Linux Mint):
nemo ~/.local/share/SearchWallpaper/

# KDE Plasma (Kubuntu):
dolphin ~/.local/share/SearchWallpaper/

# GNOME (Ubuntu):
nautilus ~/.local/share/SearchWallpaper/

# MATE:
caja ~/.local/share/SearchWallpaper/
```

### Filformat

**Viktigt:** Använd INTE hakparenteser `[]`, citattecken `""` eller kommatecken på radslut!

**Korrekt format:**
```ini
[Search]
queries = 
    stockholm cityscape wallpaper
    stockholm skyline wallpaper
    mountain landscape wallpaper
    ocean sunset wallpaper

excluded_words = 
    people,person,car,cartoon,drawing
```

### Exempel på olika teman

**🏙️ Städer:**
```ini
queries = 
    stockholm cityscape wallpaper
    stockholm gamla stan wallpaper
    stockholm archipelago wallpaper
    stockholm sunset wallpaper
```

**🏔️ Natur och landskap:**
```ini
queries = 
    mountain landscape wallpaper
    forest nature wallpaper
    ocean sunset wallpaper
    northern lights wallpaper
    waterfall nature wallpaper
```

**🌌 Rymden:**
```ini
queries = 
    galaxy space wallpaper
    nebula wallpaper
    milky way wallpaper
    planet wallpaper
```

**🦜 Fåglar (standard):**
```ini
queries = 
    pet parrot beautiful wallpaper
    macaw bird wallpaper
    cockatoo portrait wallpaper
```

**🚗 Bilar:**
```ini
queries = 
    sports car wallpaper
    classic car wallpaper
    supercar wallpaper
```

### Filtrering

Lägg till ord som ska filtreras bort (kommaseparerade på EN rad):

```ini
excluded_words = 
    people,person,car,traffic,cartoon,drawing,sketch,clipart,anime,toy
```

---

## 🔄 Daglig användning

### Manuell körning

```bash
cd ~/Dokument/Github/search_wallpaper
source venv/bin/activate
python src/main.py
```

### Skapa desktop launcher (rekommenderas!)

**För alla skrivbordsmiljöer:**

```bash
cat > ~/.local/share/applications/search-wallpaper.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=SearchWallpaper
Comment=Hämta ny bakgrundsbild från Bing
Exec=/bin/bash -c "cd ~/Dokument/Github/search_wallpaper && source venv/bin/activate && python src/main.py"
Icon=preferences-desktop-wallpaper
Terminal=false
Categories=Utility;
EOF

chmod +x ~/.local/share/applications/search-wallpaper.desktop
```

**Nu kan du starta programmet från applikationsmenyn!** 🎯

### Skapa terminal-alias (valfritt)

Lägg till i `~/.bashrc`:

```bash
alias newwall='cd ~/Dokument/Github/search_wallpaper && source venv/bin/activate && python src/main.py'
```

Ladda om konfigurationen:
```bash
source ~/.bashrc
```

Nu kan du bara skriva `newwall` för ny bakgrund! ⚡

---

## 📊 Hantera programdata

### Visa cache och historik

```bash
# Lista nedladdade bilder
ls -lh ~/.local/share/SearchWallpaper/cache/

# Visa historik
cat ~/.local/share/SearchWallpaper/history.json

# Visa logg
tail -50 ~/.local/share/SearchWallpaper/logs/search_wallpaper.log

# Följ loggen i realtid
tail -f ~/.local/share/SearchWallpaper/logs/search_wallpaper.log
```

### Rensa och återställa

```bash
# Rensa cache (behåll konfiguration)
rm ~/.local/share/SearchWallpaper/cache/*.jpg

# Nollställ daglig räknare
rm ~/.local/share/SearchWallpaper/daily_search_count.json

# Radera historik (börja om från början)
rm ~/.local/share/SearchWallpaper/history.json

# Återställ konfiguration till standard
rm ~/.local/share/SearchWallpaper/search_queries.ini
# Kör programmet igen så skapas ny standardfil
```

### Ta backup av inställningar

```bash
# Backup hela SearchWallpaper-mappen
cp -r ~/.local/share/SearchWallpaper ~/Dokument/SearchWallpaper-backup-$(date +%Y%m%d)

# Återställ från backup
cp -r ~/Dokument/SearchWallpaper-backup-YYYYMMDD ~/.local/share/SearchWallpaper
```

---

## 🐛 Felsökning

### Skrivbordsmiljö-detektering

Kontrollera vilken skrivbordsmiljö som detekteras:

```bash
echo $XDG_CURRENT_DESKTOP
```

Förväntade resultat:
- **Cinnamon**: `X-Cinnamon`
- **KDE Plasma**: `KDE`
- **MATE**: `MATE`
- **GNOME**: `GNOME` eller `ubuntu:GNOME`
- **Unity**: `Unity`

### Problem: Bakgrundsbild ändras inte

```bash
# Kontrollera skrivbordsmiljö
echo $XDG_CURRENT_DESKTOP

# Testa manuellt baserat på din skrivbordsmiljö:

# För Cinnamon (Linux Mint):
gsettings set org.cinnamon.desktop.background picture-uri "file://$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"

# För KDE Plasma (Kubuntu):
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg

# För MATE:
gsettings set org.mate.background picture-filename "$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"

# För GNOME (Ubuntu):
gsettings set org.gnome.desktop.background picture-uri "file://$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"
```

### Problem: "Edge saknas" trots installation

```bash
# Kontrollera Edge
which microsoft-edge
microsoft-edge --version

# Om inget resultat - installera om (se Steg 1)
```

### Problem: Versions-mismatch på drivern (`SessionNotCreatedException`)

Om du får ett fel som *"This version of Microsoft Edge WebDriver only supports
Microsoft Edge version X"* har du en föråldrad `msedgedriver` på din PATH som
Selenium Manager plockar upp i stället för att ladda ner rätt version.

```bash
# Hitta och ta bort den föråldrade drivern
which msedgedriver
sudo rm -f /usr/local/bin/msedgedriver

# Valfritt: rensa Selenium-cachen så den laddas om rent
rm -rf ~/.cache/selenium

# Vid nästa körning laddar Selenium Manager ner rätt driver automatiskt.
```

### Problem: "ModuleNotFoundError: No module named 'tkinter'"

```bash
# Installera tkinter
sudo apt install python3-tk
```

### Problem: "externally-managed-environment"

Du har glömt aktivera virtual environment:

```bash
cd ~/Dokument/Github/search_wallpaper
source venv/bin/activate
# Nu ska du se "(venv)" i terminalen
```

### Problem: "Parsing errors" i konfigurationsfilen

```bash
# Visa filen för att hitta fel
cat ~/.local/share/SearchWallpaper/search_queries.ini

# Vanliga fel:
# ❌ Hakparenteser [ ]
# ❌ Citattecken " "
# ❌ Kommatecken på radslut ,
# ✅ Korrekt format - se avsnittet "Anpassa söktermer"

# Återställ till standard
rm ~/.local/share/SearchWallpaper/search_queries.ini
python src/main.py  # Skapar ny standardfil
```

### Problem: "Could not reach host"

Oftast ett nätverks- eller driver-problem:

```bash
# Kontrollera nätverksanslutning
ping -c 3 bing.com

# Om felet är en driver-mismatch, ta bort ev. manuell driver så
# Selenium Manager kan ladda ner rätt version automatiskt:
sudo rm -f /usr/local/bin/msedgedriver
rm -rf ~/.cache/selenium
```

---

## ⚙️ Tekniska detaljer

### Stöd för skrivbordsmiljöer

Programmet detekterar automatiskt din skrivbordsmiljö via `XDG_CURRENT_DESKTOP`:

| Skrivbordsmiljö | Metod som används | Schema |
|---|---|---|
| **Cinnamon** | `gsettings` | `org.cinnamon.desktop.background` |
| **KDE Plasma** | `plasma-apply-wallpaperimage` eller `dbus` | Native KDE |
| **MATE** | `gsettings` | `org.mate.background` |
| **GNOME/Unity** | `gsettings` | `org.gnome.desktop.background` |

**Automatisk fallback:** Om skrivbordsmiljön är okänd försöker programmet alla metoder i ordning tills en lyckas.

### Begränsningar

- **Max 50 sökningar/dag** - respekterar Bing TOS
- **Max 50 bilder i historik** - undviker duplicering
- **Max 3 loggfiler** - automatisk rotation
- **Minimikrav bilder:** 1920x1080 pixlar, landskapsformat

### Säkerhet

- ✅ Inga API-nycklar behövs
- ✅ Lokal datalagring
- ✅ Ingen bakgrundskörning
- ✅ Respekterar Bing användarvillkor
- ✅ Ingen data skickas till externa servrar

### Prestanda

- **Headless browser** - Edge körs osynligt
- **Smart cachning** - återanvänder bilder
- **Historikhantering** - undviker dubbletter
- **Loggrotation** - rensas automatiskt

---

## 👨‍💻 Utveckling

### Projektstruktur

```
search_wallpaper/
├── src/
│   ├── api/
│   │   └── bing_scraper.py      # Bing-sökning med Selenium
│   ├── config/
│   │   ├── logging_config.py    # Loggning
│   │   └── search_config.py     # Sökterm-hantering
│   ├── utils/
│   │   ├── paths.py             # XDG-sökvägar
│   │   └── wallpaper.py         # Multi-DE integration
│   └── main.py                  # Huvudprogram
├── venv/                        # Virtual environment
├── requirements.txt             # Python-beroenden
└── README.md
```

### Köra i utvecklingsläge

```bash
cd ~/Dokument/Github/search_wallpaper
source venv/bin/activate
python src/main.py
```

---

## 🤝 Bidra

### Rapportera problem

1. Kontrollera loggfilen: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Kontrollera skrivbordsmiljö: `echo $XDG_CURRENT_DESKTOP`
3. Verifiera systemkrav uppfyllda
4. Skapa issue på GitHub med logg och systeminfo

### Utveckling

1. Forka repositoryt
2. Skapa feature-branch
3. Följ befintlig kodstil
4. Testa på din skrivbordsmiljö
5. Skicka pull request

---

## 📄 Licens

MIT License - Öppen källkod för personligt bruk.

**OBS:** Programmet använder Bing Image Search och måste respektera Microsofts användarvillkor.

---

## 🙏 Tack till

- **Microsoft Edge** - Webbläsare och WebDriver
- **Selenium** - Webbautomation
- **Bing Images** - Bildkälla
- **Linux DE-team** - KDE, GNOME, Cinnamon, MATE
- **Python-communityn** - Fantastiska bibliotek

---

## 📞 Support

För frågor eller problem - skapa ett issue på GitHub!

---

**Njut av vackra bakgrundsbilder på ditt Linux-system! 🐧🎨**
