# SearchWallpaper - Linux Edition

**[🇸🇪 Läs på svenska / Read in Swedish](README.sv.md)**

---

## 🐧 Automatic Wallpaper Manager for Linux

SearchWallpaper is a program that automatically fetches and sets random wallpapers on your Linux computer. The program searches Bing for images based on search terms that you can customize. It's specifically designed to find high-quality images in the right size for modern displays.

**This version supports multiple Linux desktop environments.**

## 🎯 Features

- ✅ **Automatic image fetching** from Bing Images
- ✅ **Customizable search terms** via configuration file
- ✅ **Image validation** - only high-quality images in landscape format (1920x1080+)
- ✅ **Smart filtering** - avoid drawings, cartoons, people, etc.
- ✅ **History management** - no duplicates of recently used images
- ✅ **Daily search limit** - respects Bing TOS (max 50/day)
- ✅ **Cache system** - reuses images during network issues
- ✅ **Detailed logging** - easy troubleshooting
- ✅ **Multi-DE support** - KDE Plasma, Cinnamon, MATE, GNOME

---

## 📋 System Requirements

### Hardware
- Modern computer with at least 4GB RAM
- Internet connection
- Screen resolution at least 1920x1080

### Software
- **Ubuntu-based Linux** (Ubuntu 20.04+, Kubuntu, Linux Mint 20+)
- **Supported Desktop Environments:**
  - **Cinnamon** (Linux Mint standard)
  - **KDE Plasma 5/6**
  - **MATE Desktop**
  - **GNOME/Unity**
- **Python 3.8+**
- **Microsoft Edge** (installation instructions below)

### Compatibility

**✅ Tested and working:**
- **Linux Mint 21/22 with Cinnamon**
- **Kubuntu 24.04 with KDE Plasma 5**
- **Ubuntu MATE 22.04/24.04**
- **Ubuntu 22.04/24.04 with GNOME**

**✅ Should work:**
- Linux Mint KDE Edition
- KDE neon
- Ubuntu Unity
- Debian with supported DE

**🟡 May work with modifications:**
- Other Debian-based distributions
- Xfce (requires manual gsettings configuration)

**❌ Does NOT work:**
- LXQt, i3, Sway (no standard wallpaper API)
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
# Go to Downloads folder (adjust path for your locale)
cd ~/Downloads  # or ~/Hämtningar for Swedish, ~/Nedlastinger for Norwegian, etc.

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
# Create project folder (adjust path for your locale)
mkdir -p ~/Documents/Github  # or ~/Dokument/Github for Swedish, etc.
cd ~/Documents/Github

# Clone or download project
# If you have git:
git clone https://github.com/YOUR_REPO/search_wallpaper.git
cd search_wallpaper

# If you downloaded ZIP:
# Extract to ~/Documents/Github/search_wallpaper
```

---

### Step 5: Create Virtual Environment

```bash
# Go to project folder
cd ~/Documents/Github/search_wallpaper

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
# File managers by desktop environment:

# Cinnamon (Linux Mint):
nemo ~/.local/share/SearchWallpaper/

# KDE Plasma (Kubuntu):
dolphin ~/.local/share/SearchWallpaper/

# GNOME (Ubuntu):
nautilus ~/.local/share/SearchWallpaper/

# MATE:
caja ~/.local/share/SearchWallpaper/
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

**🏙️ Cities:**
```ini
queries = 
    stockholm cityscape wallpaper
    new york skyline wallpaper
    tokyo night wallpaper
    paris sunset wallpaper
```

**🏔️ Nature:**
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

---

## 🔄 Daily Usage

### Manual Execution

```bash
cd ~/Documents/Github/search_wallpaper
source venv/bin/activate
python src/main.py
```

### Create Desktop Launcher (recommended!)

**For all desktop environments:**

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

---

## 🐛 Troubleshooting

### Desktop Environment Detection

Check which DE is detected:

```bash
echo $XDG_CURRENT_DESKTOP
```

Expected outputs:
- **Cinnamon**: `X-Cinnamon`
- **KDE Plasma**: `KDE`
- **MATE**: `MATE`
- **GNOME**: `GNOME` or `ubuntu:GNOME`
- **Unity**: `Unity`

### Wallpaper doesn't change

```bash
# Check desktop environment
echo $XDG_CURRENT_DESKTOP

# Test manually based on your DE:

# For Cinnamon (Linux Mint):
gsettings set org.cinnamon.desktop.background picture-uri "file://$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"

# For KDE Plasma (Kubuntu):
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg

# For MATE:
gsettings set org.mate.background picture-filename "$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"

# For GNOME (Ubuntu):
gsettings set org.gnome.desktop.background picture-uri "file://$HOME/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg"
```

### Problem: "Edge missing"

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

# Versions must match Edge!
microsoft-edge --version
/usr/local/bin/msedgedriver --version
```

### Problem: "ModuleNotFoundError: tkinter"

```bash
sudo apt install python3-tk
```

### Problem: Virtual environment not activated

```bash
cd ~/Documents/Github/search_wallpaper
source venv/bin/activate
# Should show "(venv)" in terminal
```

---

## ⚙️ Technical Details

### Desktop Environment Support

The program automatically detects your DE via `XDG_CURRENT_DESKTOP`:

| Desktop Environment | Method Used | Schema |
|---|---|---|
| **Cinnamon** | `gsettings` | `org.cinnamon.desktop.background` |
| **KDE Plasma** | `plasma-apply-wallpaperimage` or `dbus` | Native KDE |
| **MATE** | `gsettings` | `org.mate.background` |
| **GNOME/Unity** | `gsettings` | `org.gnome.desktop.background` |

**Automatic fallback:** If DE is unknown, the program tries all methods in order until one succeeds.

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
│   │   └── wallpaper.py         # Multi-DE integration
│   └── main.py                  # Main program
├── venv/                        # Virtual environment
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🤝 Contributing

### Report Issues

1. Check log: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Check DE: `echo $XDG_CURRENT_DESKTOP`
3. Verify requirements met
4. Create GitHub issue with log and system info

---

## 📄 License

MIT License - Open source for personal use.

**Note:** Program uses Bing Image Search and must respect Microsoft's terms of service.

---

## 🙏 Credits

- **Microsoft Edge** - Browser and WebDriver
- **Selenium** - Web automation
- **Bing Images** - Image source
- **Linux DE Teams** - KDE, GNOME, Cinnamon, MATE
- **Python community** - Amazing libraries

---

**Enjoy beautiful wallpapers on your Linux system! 🐧🎨**
