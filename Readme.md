# SearchWallpaper - Kubuntu Edition

**[🇬🇧 English](#english)** | **[🇸🇪 Svenska](#svenska)**

---

<a name="english"></a>
# 🇬🇧 ENGLISH VERSION

## 🐧 Automatic Wallpaper Manager for Linux

SearchWallpaper is a program that automatically fetches and sets random wallpapers on your Kubuntu computer. The program searches Bing for images based on search terms that you can customize. It's specifically designed to find high-quality images in the right size for modern displays.

**This version is specifically adapted for Kubuntu with KDE Plasma.**

## 🎯 Features

- ✅ **Automatic image fetching** from Bing Images
- ✅ **Customizable search terms** via configuration file
- ✅ **Image validation** - only high-quality images in landscape format (1920x1080+)
- ✅ **Smart filtering** - avoid drawings, cartoons, people, etc.
- ✅ **History management** - no duplicates of recently used images
- ✅ **Daily search limit** - respects Bing TOS (max 50/day)
- ✅ **Cache system** - reuses images during network issues
- ✅ **Detailed logging** - easy troubleshooting
- ✅ **KDE Plasma integration** - direct wallpaper updates

---

## 📋 System Requirements

### Hardware
- Modern computer with at least 4GB RAM
- Internet connection
- Screen resolution at least 1920x1080

### Software
- **Kubuntu 20.04 or later** (tested on 24.04)
- **KDE Plasma 5 or 6** (tested on Plasma 5)
- **Python 3.8+**
- **Microsoft Edge** (installation instructions below)

### Compatibility

**✅ Tested and working:**
- Kubuntu 24.04 with KDE Plasma 5

**🟡 Should work (untested):**
- Other Ubuntu variants with KDE Plasma
- Linux Mint KDE Edition
- KDE neon
- Debian with KDE Plasma

**🟡 May work with modifications:**
- GNOME (fallback support exists)
- MATE (GNOME-based)
- Cinnamon (GNOME-based)

**❌ Does NOT work:**
- Xfce, LXQt, i3, Sway (no wallpaper change support)
- Red Hat/Fedora/Arch Linux (requires different package format)

---

## 🚀 Installation

### Step 1: Install Microsoft Edge

Open terminal (`Ctrl+Alt+T`) and run:

```bash
# Download Microsoft signing key
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

# Install key
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/

# Add Edge repository
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# Remove temporary key
rm microsoft.gpg

# Update and install
sudo apt update
sudo apt install microsoft-edge-stable

# Verify installation
microsoft-edge --version
```

---

### Step 2: Install System Packages

```bash
# Install required packages
sudo apt install python3-tk python3-pip python3-venv dbus-x11

# Verify Python
python3 --version
```

---

### Step 3: Download and Install EdgeDriver

**Method A: Via browser (recommended for beginners)**

1. Open Microsoft Edge
2. Check your Edge version: `microsoft-edge --version` in terminal
3. Go to: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
4. Download **Linux x64** for your Edge version
5. Install:

```bash
# Go to Downloads folder
cd ~/Downloads

# Extract
unzip edgedriver_linux64.zip

# Install
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver

# Verify
/usr/local/bin/msedgedriver --version
```

**Method B: Via terminal (for advanced users)**

```bash
# Replace VERSION with your Edge version (e.g. 141.0.3537.92)
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
cd ~/Downloads
wget https://msedgedriver.azureedge.net/${VERSION}/edgedriver_linux64.zip
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

---

### Step 4: Get the Project

```bash
# Create project folder
mkdir -p ~/Documents/Github
cd ~/Documents/Github

# Clone or download project
# If you have git:
git clone https://github.com/cgillinger/search_wallpaper_kubuntu.git
cd search_wallpaper_kubuntu

# If you downloaded ZIP:
# Extract to ~/Documents/Github/search_wallpaper_kubuntu
```

---

### Step 5: Create Virtual Environment

```bash
# Go to project folder
cd ~/Documents/Github/search_wallpaper_kubuntu

# Create virtual environment
python3 -m venv venv

# Activate (you should see "(venv)" in terminal)
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

---

### Step 6: First Test Run

```bash
# Activate venv if not already activated
source venv/bin/activate

# Run program
python src/main.py
```

**If everything works:**
- A GUI window shows "Searching for images..."
- After a few seconds your wallpaper changes
- Window closes automatically

---

## 📁 File Structure

The program creates files in your home directory following XDG Base Directory standard:

```
~/.local/share/SearchWallpaper/
├── search_queries.ini    # Your custom search terms
├── history.json         # History (last 50 images)
├── daily_search_count.json  # Counter (max 50/day)
├── logs/
│   └── search_wallpaper.log  # Log file for troubleshooting
└── cache/
    └── bing_wallpaper_*.jpg  # Downloaded images
```

**Why this location?**
- Follows Linux XDG standard
- No sudo permissions needed
- Separated from system files
- Easy to clean and restore

---

## 🎨 Customize Search Terms

### Find Configuration File

```bash
# Open in text editor
nano ~/.local/share/SearchWallpaper/search_queries.ini

# Or open folder in file manager (press Ctrl+H to show hidden folders)
dolphin ~/.local/share/SearchWallpaper/
```

### File Format

**Important:** Do NOT use brackets `[]`, quotes `""` or commas at end of lines!

**Correct format:**
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

### Theme Examples

**🏙️ Stockholm:**
```ini
queries = 
    stockholm cityscape wallpaper
    stockholm gamla stan wallpaper
    stockholm archipelago wallpaper
    stockholm sunset wallpaper
```

**🏔️ Nature and Landscape:**
```ini
queries = 
    mountain landscape wallpaper
    forest nature wallpaper
    ocean sunset wallpaper
    northern lights wallpaper
    waterfall nature wallpaper
```

**🌌 Space:**
```ini
queries = 
    galaxy space wallpaper
    nebula wallpaper
    milky way wallpaper
    planet wallpaper
```

**🦜 Birds (default):**
```ini
queries = 
    pet parrot beautiful wallpaper
    macaw bird wallpaper
    cockatoo portrait wallpaper
```

**🚗 Cars:**
```ini
queries = 
    sports car wallpaper
    classic car wallpaper
    supercar wallpaper
```

### Filtering

Add words to filter out (comma-separated on ONE line):

```ini
excluded_words = 
    people,person,car,traffic,cartoon,drawing,sketch,clipart,anime,toy
```

---

## 🔄 Daily Usage

### Manual Execution

```bash
cd ~/Documents/Github/search_wallpaper
source venv/bin/activate
python src/main.py
```

### Create Desktop Launcher (recommended!)

```bash
cat > ~/.local/share/applications/search-wallpaper.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=SearchWallpaper
Comment=Get new wallpaper from Bing
Exec=/bin/bash -c "cd ~/Documents/Github/search_wallpaper && source venv/bin/activate && python src/main.py"
Icon=preferences-desktop-wallpaper
Terminal=false
Categories=Utility;
EOF

chmod +x ~/.local/share/applications/search-wallpaper.desktop
```

**Now you can start the program from application menu!** 🎯

### Create Terminal Alias (optional)

Add to `~/.bashrc`:

```bash
alias newwall='cd ~/Documents/Github/search_wallpaper && source venv/bin/activate && python src/main.py'
```

Reload configuration:
```bash
source ~/.bashrc
```

Now just type `newwall` for a new wallpaper! ⚡

---

## 📊 Manage Program Data

### View Cache and History

```bash
# List downloaded images
ls -lh ~/.local/share/SearchWallpaper/cache/

# View history
cat ~/.local/share/SearchWallpaper/history.json

# View log
tail -50 ~/.local/share/SearchWallpaper/logs/search_wallpaper.log

# Follow log in real-time
tail -f ~/.local/share/SearchWallpaper/logs/search_wallpaper.log
```

### Clean and Reset

```bash
# Clear cache (keep configuration)
rm ~/.local/share/SearchWallpaper/cache/*.jpg

# Reset daily counter
rm ~/.local/share/SearchWallpaper/daily_search_count.json

# Delete history (start from scratch)
rm ~/.local/share/SearchWallpaper/history.json

# Reset configuration to default
rm ~/.local/share/SearchWallpaper/search_queries.ini
# Run program again to create new default file
```

### Backup Settings

```bash
# Backup entire SearchWallpaper folder
cp -r ~/.local/share/SearchWallpaper ~/Documents/SearchWallpaper-backup-$(date +%Y%m%d)

# Restore from backup
cp -r ~/Documents/SearchWallpaper-backup-YYYYMMDD ~/.local/share/SearchWallpaper
```

---

## 🐛 Troubleshooting

### Problem: "Edge missing" despite installation

```bash
# Check Edge
which microsoft-edge
microsoft-edge --version

# If no result - reinstall (see Step 1)
```

### Problem: "msedgedriver not found"

```bash
# Check EdgeDriver
which msedgedriver
/usr/local/bin/msedgedriver --version

# If error - reinstall (see Step 3)
```

### Problem: "ModuleNotFoundError: No module named 'tkinter'"

```bash
# Install tkinter
sudo apt install python3-tk
```

### Problem: "externally-managed-environment"

You forgot to activate virtual environment:

```bash
cd ~/Documents/Github/search_wallpaper
source venv/bin/activate
# Now you should see "(venv)" in terminal
```

### Problem: Wallpaper doesn't change

```bash
# Check desktop environment
echo $XDG_CURRENT_DESKTOP
# Should show "KDE" or similar

# Check plasma-apply-wallpaperimage
which plasma-apply-wallpaperimage

# Test manually
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg
```

### Problem: "Parsing errors" in configuration file

```bash
# Show file to find errors
cat ~/.local/share/SearchWallpaper/search_queries.ini

# Common errors:
# ❌ Brackets [ ]
# ❌ Quotes " "
# ❌ Commas at end of lines ,
# ✅ Correct format - see "Customize Search Terms" section

# Reset to default
rm ~/.local/share/SearchWallpaper/search_queries.ini
python src/main.py  # Creates new default file
```

### Problem: "Could not reach host"

EdgeDriver issue:

```bash
# Check EdgeDriver version matches Edge
microsoft-edge --version
/usr/local/bin/msedgedriver --version

# Versions should match! If not - download correct version (see Step 3)
```

---

## ⚙️ Technical Details

### Limitations

- **Max 50 searches/day** - respects Bing TOS
- **Max 50 images in history** - avoids duplication
- **Max 3 log files** - automatic rotation
- **Image requirements:** 1920x1080 pixels minimum, landscape format

### Security

- ✅ No API keys needed
- ✅ Local data storage
- ✅ No background processes
- ✅ Respects Bing terms of service
- ✅ No data sent to external servers

### Performance

- **Headless browser** - Edge runs invisibly
- **Smart caching** - reuses images
- **History management** - avoids duplicates
- **Log rotation** - cleaned automatically

---

## 👨‍💻 Development

### Project Structure

```
search_wallpaper/
├── src/
│   ├── api/
│   │   └── bing_scraper.py      # Bing search with Selenium
│   ├── config/
│   │   ├── logging_config.py    # Logging
│   │   └── search_config.py     # Search term management
│   ├── utils/
│   │   ├── paths.py             # XDG paths
│   │   └── wallpaper.py         # KDE Plasma integration
│   └── main.py                  # Main program
├── venv/                        # Virtual environment
├── requirements.txt             # Python dependencies
└── README.md
```

### Run in Development Mode

```bash
cd ~/Documents/Github/search_wallpaper
source venv/bin/activate
python src/main.py
```

---

## 📝 Changelog

### Version 2.0 - Kubuntu Edition (2025-10-24)

**Initial release for Linux/Kubuntu:**
- ✅ KDE Plasma integration
- ✅ XDG Base Directory standard
- ✅ `plasma-apply-wallpaperimage` for wallpaper
- ✅ GNOME fallback for compatibility
- ✅ Platform-specific Edge detection
- ✅ Manual EdgeDriver installation
- ✅ Complete documentation for beginners

---

## 🤝 Contributing

### Report Issues

1. Check log file: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Verify system requirements met
3. Test manual commands from Troubleshooting
4. Create GitHub issue with log and system info

### Development

1. Fork repository
2. Create feature branch
3. Follow existing code style
4. Test on Kubuntu
5. Submit pull request

---

## 📄 License

Open source for personal use.

**Note:** Program uses Bing Image Search and must respect Microsoft's terms of service.

---

## 🙏 Credits

- **Microsoft Edge** - Browser and WebDriver
- **Selenium** - Web automation
- **Bing Images** - Image source
- **KDE Plasma** - Desktop Environment
- **Python community** - Amazing libraries

---

## 📞 Support

For questions or issues - create a GitHub issue!

---

**Enjoy beautiful wallpapers on your Kubuntu! 🐧🎨**

---
---
---

<a name="svenska"></a>
# 🇸🇪 SVENSK VERSION

## 🐧 Automatisk bakgrundsbildshanterare för Linux

SearchWallpaper är ett program som automatiskt hämtar och sätter slumpmässiga bakgrundsbilder på din Kubuntu-dator. Programmet söker på Bing efter bilder baserat på söktermer som du själv kan anpassa. Det är särskilt utformat för att hitta högkvalitativa bilder i rätt storlek för moderna skärmar.

**Denna version är specifikt anpassad för Kubuntu med KDE Plasma.**

## 🎯 Funktioner

- ✅ **Automatisk bildhämtning** från Bing Images
- ✅ **Anpassningsbara söktermer** via konfigurationsfil
- ✅ **Bildvalidering** - endast högkvalitativa bilder i landskapsformat (1920x1080+)
- ✅ **Smart filtrering** - undvik teckningar, cartoons, människor etc.
- ✅ **Historikhantering** - inga dubbletter av nyligen använda bilder
- ✅ **Daglig sökgräns** - respekterar Bing TOS (max 50/dag)
- ✅ **Cache-system** - återanvänder bilder vid nätverksproblem
- ✅ **Detaljerad loggning** - enkel felsökning
- ✅ **KDE Plasma-integration** - direkt bakgrundsuppdatering

---

## 📋 Systemkrav

### Hårdvara
- Modern dator med minst 4GB RAM
- Internetanslutning
- Skärmupplösning minst 1920x1080

### Programvara
- **Kubuntu 20.04 eller senare** (testat på 24.04)
- **KDE Plasma 5 eller 6** (testat på Plasma 5)
- **Python 3.8+**
- **Microsoft Edge** (installationsinstruktioner nedan)

### Kompatibilitet

**✅ Testat och fungerar:**
- Kubuntu 24.04 med KDE Plasma 5

**🟡 Borde fungera (otestat):**
- Andra Ubuntu-varianter med KDE Plasma
- Linux Mint KDE Edition
- KDE neon
- Debian med KDE Plasma

**🟡 Kan fungera med ändringar:**
- GNOME (fallback-stöd finns)
- MATE (GNOME-baserad)
- Cinnamon (GNOME-baserad)

**❌ Fungerar INTE:**
- Xfce, LXQt, i3, Sway (inget stöd för bakgrundsbyten)
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

### Steg 3: Ladda ner och installera EdgeDriver

**Metod A: Via webbläsaren (rekommenderas för nybörjare)**

1. Öppna Microsoft Edge
2. Kolla din Edge-version: `microsoft-edge --version` i terminal
3. Gå till: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
4. Ladda ner **Linux x64** för din Edge-version
5. Installera:

```bash
# Gå till Hämtningar
cd ~/Hämtningar

# Packa upp
unzip edgedriver_linux64.zip

# Installera
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver

# Verifiera
/usr/local/bin/msedgedriver --version
```

**Metod B: Via terminal (för avancerade)**

```bash
# Ersätt VERSION med din Edge-version (t.ex. 141.0.3537.92)
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
cd ~/Hämtningar
wget https://msedgedriver.azureedge.net/${VERSION}/edgedriver_linux64.zip
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

---

### Steg 4: Hämta projektet

```bash
# Skapa projektmapp
mkdir -p ~/Dokument/Github
cd ~/Dokument/Github

# Klona eller ladda ner projektet
# Om du har git:
git clone https://github.com/DIN_ANVÄNDARE/search_wallpaper.git
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
dolphin ~/.local/share/SearchWallpaper/
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

**🏙️ Stockholm:**
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

### Problem: "Edge saknas" trots installation

```bash
# Kontrollera Edge
which microsoft-edge
microsoft-edge --version

# Om inget resultat - installera om (se Steg 1)
```

### Problem: "msedgedriver kunde inte hittas"

```bash
# Kontrollera EdgeDriver
which msedgedriver
/usr/local/bin/msedgedriver --version

# Om fel - installera om (se Steg 3)
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

### Problem: Bakgrundsbild ändras inte

```bash
# Kontrollera skrivbordsmiljö
echo $XDG_CURRENT_DESKTOP
# Ska visa "KDE" eller liknande

# Kontrollera plasma-apply-wallpaperimage
which plasma-apply-wallpaperimage

# Testa manuellt
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg
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

EdgeDriver-problem:

```bash
# Kontrollera EdgeDriver-version matchar Edge
microsoft-edge --version
/usr/local/bin/msedgedriver --version

# Versioner ska matcha! Om inte - ladda ner rätt version (se Steg 3)
```

---

## ⚙️ Tekniska detaljer

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
│   │   └── wallpaper.py         # KDE Plasma-integration
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

## 📝 Changelog

### Version 2.0 - Kubuntu Edition (2025-10-24)

**Initial release för Linux/Kubuntu:**
- ✅ KDE Plasma-integration
- ✅ XDG Base Directory-standard
- ✅ `plasma-apply-wallpaperimage` för bakgrund
- ✅ GNOME-fallback för kompatibilitet
- ✅ Plattformsspecifik Edge-detection
- ✅ Manuell EdgeDriver-installation
- ✅ Komplett dokumentation för nybörjare

---

## 🤝 Bidra

### Rapportera problem

1. Kontrollera loggfilen: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Verifiera systemkrav uppfyllda
3. Testa manuella kommandon från Felsökning
4. Skapa issue på GitHub med logg och systeminfo

### Utveckling

1. Forka repositoryt
2. Skapa feature-branch
3. Följ befintlig kodstil
4. Testa på Kubuntu
5. Skicka pull request

---

## 📄 Licens

Öppen källkod för personligt bruk.

**OBS:** Programmet använder Bing Image Search och måste respektera Microsofts användarvillkor.

---

## 🙏 Tack till

- **Microsoft Edge** - Webbläsare och WebDriver
- **Selenium** - Webbautomation
- **Bing Images** - Bildkälla
- **KDE Plasma** - Desktop Environment
- **Python-communityn** - Fantastiska bibliotek

---

## 📞 Support

För frågor eller problem - skapa ett issue på GitHub!

---

**Njut av vackra bakgrundsbilder på din Kubuntu! 🐧🎨**
