# SearchWallpaper — Linux Edition

**Automatic Bing wallpaper manager for KDE Plasma, Cinnamon, MATE, GNOME and Enlightenment on Linux**

[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Kubuntu%20%7C%20Linux%20Mint%20%7C%20Ubuntu-E95420?logo=ubuntu&logoColor=white)](https://kubuntu.org/)
[![KDE Plasma](https://img.shields.io/badge/KDE_Plasma-5%2B-1D99F3?logo=kde&logoColor=white)](https://kde.org/plasma-desktop/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16%2B-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Microsoft Edge](https://img.shields.io/badge/Microsoft_Edge-required-0078D7?logo=microsoftedge&logoColor=white)](https://www.microsoft.com/edge)
[![License](https://img.shields.io/badge/license-Open_Source-brightgreen)](LICENSE)

**[🇸🇪 Läs på svenska / Read in Swedish](README.sv.md)**

---

## What is SearchWallpaper?

**SearchWallpaper** automatically fetches high-resolution wallpapers from Bing Images and sets them as your desktop background on Kubuntu, Linux Mint, Ubuntu, or any Debian-based Linux system.

The program uses a headless Microsoft Edge browser (via Selenium) to search Bing for images matching your custom search terms. It validates every image for resolution (1920×1080 minimum, landscape orientation) before setting it as your wallpaper — so you only ever get crisp, full-screen backgrounds.

> **Supports KDE Plasma, Cinnamon, MATE, GNOME and Enlightenment on Debian-based Linux.**
> No API keys required. No background daemon. Just run it when you want a new wallpaper.

---

## Features

| Feature | Details |
|---|---|
| **Automatic image fetching** | Searches Bing Images using Selenium + headless Edge |
| **Customisable search terms** | Edit a plain `.ini` file — no coding needed |
| **Image validation** | Only landscape images at 1920×1080 px or larger |
| **Smart filtering** | Block keywords (cartoons, people, drawings, etc.) |
| **History management** | Tracks the last 50 images — no repeats |
| **Daily search limit** | Max 50 searches/day to respect Bing TOS |
| **Cache system** | Falls back to cached images if network is unavailable |
| **Detailed logging** | Rotating log files for easy troubleshooting |
| **KDE Plasma integration** | Uses `plasma-apply-wallpaperimage` directly |

---

## System Requirements

### Hardware
- 4 GB RAM or more
- Internet connection
- Screen resolution 1920×1080 or higher

### Software
- **Kubuntu 20.04+ / Linux Mint 20+ / Ubuntu 20.04+** (tested on Kubuntu 24.04 and Linux Mint 21)
- **KDE Plasma 5 or 6**
- **Python 3.8+**
- **Microsoft Edge** (stable) — see installation below
- **msedgedriver** matching your Edge version — see installation below

### Compatibility

| Status | Desktop Environment |
|---|---|
| ✅ Tested and working | Kubuntu 24.04 with KDE Plasma 5 |
| ✅ Tested and working | Linux Mint 21+ with Cinnamon |
| 🟡 Should work (untested) | Ubuntu with KDE, Linux Mint KDE, KDE neon, Debian KDE |
| 🟡 Should work (untested) | GNOME, MATE |
| 🟡 Should work (untested) | Enlightenment (E17/E18+) |
| ❌ Not supported | Xfce, LXQt, i3, Sway, Fedora/Arch/Red Hat |

---

## Installation

### Step 1 — Install Microsoft Edge

```bash
# Download Microsoft signing key
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

# Install key
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/

# Add Edge repository
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# Clean up
rm microsoft.gpg

# Update and install
sudo apt update
sudo apt install microsoft-edge-stable

# Verify
microsoft-edge --version
```

---

### Step 2 — Install System Packages

```bash
sudo apt install python3-tk python3-pip python3-venv dbus-x11

# Verify
python3 --version
```

---

### Step 3 — Download and Install EdgeDriver

**msedgedriver must exactly match your Edge browser version.**

**Method A — Via browser (recommended for beginners)**

1. Check your Edge version: `microsoft-edge --version`
2. Go to: <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>
3. Download **Linux x64** for your exact version
4. Install:

```bash
cd ~/Downloads
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

**Method B — Via terminal**

```bash
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
cd ~/Downloads
wget "https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver/${VERSION}/edgedriver_linux64.zip"
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver
/usr/local/bin/msedgedriver --version
```

> **Note:** If the primary CDN (`msedgedriver.azureedge.net`) is unreachable — which can happen after VPN use due to DNS issues — use the blob storage URL above (`msedgewebdriverstorage.blob.core.windows.net`). It is a reliable alternative that always works.

---

### Step 4 — Clone the Repository

```bash
mkdir -p ~/Documents/Github
cd ~/Documents/Github
git clone https://github.com/cgillinger/search_wallpaper_kubuntu.git
cd search_wallpaper_kubuntu
```

---

### Step 5 — Set Up Python Virtual Environment

```bash
cd ~/Documents/Github/search_wallpaper_kubuntu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Step 6 — First Run

```bash
source venv/bin/activate
python src/main.py
```

If everything works:
- A small status window appears briefly
- Your desktop wallpaper changes after a few seconds
- The window closes automatically

---

## File Structure

```
~/.local/share/SearchWallpaper/
├── search_queries.ini       # Your custom search terms
├── history.json             # Last 50 wallpapers (prevents repeats)
├── daily_search_count.json  # Daily counter (max 50/day)
├── logs/
│   └── search_wallpaper.log # Rotating log for troubleshooting
└── cache/
    └── bing_wallpaper_*.jpg # Downloaded wallpapers
```

All data is stored in your home directory following the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). No sudo access is needed for normal operation.

---

## Customise Search Terms

```bash
nano ~/.local/share/SearchWallpaper/search_queries.ini
```

**Format rules:** No brackets `[]`, no quotes `""`, no trailing commas.

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

### Theme Examples

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
<summary>🏔️ Nature & Landscapes</summary>

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
<summary>🌌 Space</summary>

```ini
queries =
    galaxy space wallpaper
    nebula wallpaper
    milky way wallpaper
    planet wallpaper
```
</details>

<details>
<summary>🦜 Birds (default)</summary>

```ini
queries =
    pet parrot beautiful wallpaper
    macaw bird wallpaper
    cockatoo portrait wallpaper
```
</details>

<details>
<summary>🚗 Cars</summary>

```ini
queries =
    sports car wallpaper
    classic car wallpaper
    supercar wallpaper
```
</details>

---

## Daily Usage

### Run Manually

```bash
cd ~/Documents/Github/search_wallpaper_kubuntu
source venv/bin/activate
python src/main.py
```

### Desktop Launcher (recommended)

```bash
cat > ~/.local/share/applications/search-wallpaper.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=SearchWallpaper
Comment=Fetch a new wallpaper from Bing
Exec=/bin/bash -c "cd ~/Documents/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py"
Icon=preferences-desktop-wallpaper
Terminal=false
Categories=Utility;
EOF

chmod +x ~/.local/share/applications/search-wallpaper.desktop
```

### Shell Alias

Add to `~/.bashrc`:

```bash
alias newwall='cd ~/Documents/Github/search_wallpaper_kubuntu && source venv/bin/activate && python src/main.py'
```

Then reload: `source ~/.bashrc`

---

## Manage Data

```bash
# View downloaded images
ls -lh ~/.local/share/SearchWallpaper/cache/

# Follow log in real time
tail -f ~/.local/share/SearchWallpaper/logs/search_wallpaper.log

# Clear cache
rm ~/.local/share/SearchWallpaper/cache/*.jpg

# Reset daily counter
rm ~/.local/share/SearchWallpaper/daily_search_count.json

# Delete history (start fresh)
rm ~/.local/share/SearchWallpaper/history.json

# Backup all settings
cp -r ~/.local/share/SearchWallpaper ~/Documents/SearchWallpaper-backup-$(date +%Y%m%d)
```

---

## Troubleshooting

### Problem: Edge updated automatically and EdgeDriver version no longer matches

When Microsoft Edge updates itself automatically, the installed `msedgedriver` may no longer match the new browser version. The program detects this and logs a clear error message.

**How to detect the problem:**

Check the log file for a version mismatch message:

```bash
tail -50 ~/.local/share/SearchWallpaper/logs/search_wallpaper.log
```

You will see a line like:
```
EdgeDriver-versionsmatchfel: Edge=131.0.2903.112, msedgedriver=130.0.2849.68
```

The status window will show: **"EdgeDriver-version stämmer inte — se loggen för åtgärd"**

**Verify both versions manually:**

```bash
microsoft-edge --version
/usr/local/bin/msedgedriver --version
# Both outputs must show the same version number
```

**Fix — download the correct EdgeDriver:**

The primary CDN (`msedgedriver.azureedge.net`) is sometimes unreachable due to DNS issues — for example after VPN use. Use the reliable blob storage URL instead:

```bash
# Get your current Edge version
VERSION=$(microsoft-edge --version | grep -oP '\d+\.\d+\.\d+\.\d+')
echo "Edge version: $VERSION"

# Download from blob storage (reliable alternative URL)
cd ~/Downloads
wget "https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver/${VERSION}/edgedriver_linux64.zip"

# Install
unzip edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/msedgedriver

# Verify both versions match
microsoft-edge --version
/usr/local/bin/msedgedriver --version
```

---

### Problem: "Edge missing" despite installation

```bash
which microsoft-edge
microsoft-edge --version
# If no output — reinstall Edge (see Step 1)
```

### Problem: "msedgedriver not found"

```bash
which msedgedriver
/usr/local/bin/msedgedriver --version
# If error — reinstall EdgeDriver (see Step 3)
```

### Problem: `ModuleNotFoundError: No module named 'tkinter'`

```bash
sudo apt install python3-tk
```

### Problem: `externally-managed-environment`

You forgot to activate the virtual environment:

```bash
cd ~/Documents/Github/search_wallpaper_kubuntu
source venv/bin/activate
# You should see "(venv)" in your prompt
```

### Problem: Wallpaper doesn't change

```bash
echo $XDG_CURRENT_DESKTOP         # Should show "KDE"
which plasma-apply-wallpaperimage  # Must exist

# Test manually
plasma-apply-wallpaperimage ~/.local/share/SearchWallpaper/cache/bing_wallpaper_*.jpg
```

### Problem: Parsing errors in configuration file

```bash
cat ~/.local/share/SearchWallpaper/search_queries.ini
# Common mistakes: brackets [ ], quotes " ", trailing commas ,

# Reset to default
rm ~/.local/share/SearchWallpaper/search_queries.ini
python src/main.py  # Creates a new default file
```

---

## Technical Details

### Architecture

```
search_wallpaper_kubuntu/
├── src/
│   ├── api/
│   │   └── bing_scraper.py      # Bing search via Selenium + EdgeDriver
│   ├── config/
│   │   ├── logging_config.py    # Rotating log setup
│   │   └── search_config.py     # Search term management
│   ├── utils/
│   │   ├── paths.py             # XDG-compliant paths
│   │   └── wallpaper.py         # Cross-platform wallpaper (KDE, Cinnamon, MATE, GNOME, Enlightenment)
│   └── main.py                  # Entry point + GUI status window
├── requirements.txt
└── README.md
```

### Limits

| Limit | Value | Reason |
|---|---|---|
| Searches per day | 50 | Respects Bing TOS |
| History entries | 50 | Prevents wallpaper repeats |
| Log files | 3 (rotating) | Keeps disk usage low |
| Minimum image size | 1920×1080 px | Ensures full-HD quality |

### Security

- No API keys or accounts required
- All data stored locally in `~/.local/share/SearchWallpaper/`
- No background daemon or scheduled process
- Respects Bing terms of service
- No data sent to third-party servers

---

## Changelog

### Version 2.2 (2026-03-07)

- **New:** Cinnamon desktop support (Linux Mint default) via `gsettings org.cinnamon.desktop.background`
- **New:** MATE Desktop support via `gsettings org.mate.background`
- **New:** Enlightenment (E17/E18+) support via `enlightenment_remote`
- **Improved:** GNOME now sets both `picture-uri` and `picture-uri-dark` (dark theme support)
- **Improved:** Unknown desktop environment fallback now tries all five methods in order

### Version 2.1 (2026-03-07)

- **New:** Automatic EdgeDriver version check at startup
- **New:** Clear log message with fix instructions when version mismatch is detected (includes blob storage URL as reliable CDN alternative)
- **New:** User-friendly status message in GUI when version mismatch occurs

### Version 2.0 — Kubuntu Edition (2025-10-24)

- KDE Plasma integration via `plasma-apply-wallpaperimage`
- XDG Base Directory standard for all data files
- GNOME fallback support
- Platform-specific Edge detection
- Complete beginner-friendly documentation

---

## Contributing

1. Check the log: `~/.local/share/SearchWallpaper/logs/search_wallpaper.log`
2. Verify system requirements
3. Run the manual troubleshooting commands above
4. Open a [GitHub issue](https://github.com/cgillinger/search_wallpaper_kubuntu/issues) with your log output and system info

For code contributions: fork the repository, create a feature branch, follow existing code style, test on Kubuntu, Linux Mint, or Ubuntu, then submit a pull request.

---

## License

Open source for personal use. This program uses Bing Image Search — please respect [Microsoft's terms of service](https://www.microsoft.com/en-us/servicesagreement/).

---

## Credits

- **Microsoft Edge** — browser and WebDriver
- **Selenium** — web automation framework
- **Bing Images** — image source
- **KDE Plasma** — desktop environment
- **Python community** — excellent libraries

---

**Get beautiful, high-resolution wallpapers on your Linux desktop automatically.**
