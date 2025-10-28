# SearchWallpaper - Kubuntu Edition

**[🇸🇪 Läs på svenska / Read in Swedish](README.sv.md)**

---

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
cd ~/Documents/Github/search_wallpaper_kubuntu
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
Exec=/bin/bash -c "cd ~/Documents/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py"
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
alias newwall='cd ~/Documents/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py'
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
cd ~/Documents/Github/search_wallpaper_kubuntu
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
cd ~/Documents/Github/search_wallpaper_kubuntu
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
