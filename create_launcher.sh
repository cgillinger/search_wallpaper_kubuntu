#!/bin/bash
# Skript för att skapa SearchWallpaper desktop launcher
# Fungerar med både svenska och engelska mapnamn

echo "🎯 Skapar SearchWallpaper desktop launcher..."

# Hitta projektmappen automatiskt
if [ -d "$HOME/Dokument/Github/search_wallpaper" ]; then
    PROJECT_PATH="$HOME/Dokument/Github/search_wallpaper"
    echo "✓ Hittade projekt: Dokument/Github/search_wallpaper"
elif [ -d "$HOME/Documents/Github/search_wallpaper" ]; then
    PROJECT_PATH="$HOME/Documents/Github/search_wallpaper"
    echo "✓ Hittade projekt: Documents/Github/search_wallpaper"
else
    echo "❌ Kunde inte hitta projektet!"
    echo "Letar efter:"
    echo "  - $HOME/Dokument/Github/search_wallpaper"
    echo "  - $HOME/Documents/Github/search_wallpaper"
    exit 1
fi

# Verifiera att venv finns
if [ ! -d "$PROJECT_PATH/venv" ]; then
    echo "❌ Virtual environment (venv) saknas i projektet!"
    echo "Kör först: cd $PROJECT_PATH && python3 -m venv venv"
    exit 1
fi

# Skapa .desktop-filen
DESKTOP_FILE="$HOME/.local/share/applications/search-wallpaper.desktop"

cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Type=Application
Name=SearchWallpaper
Comment=Hämta ny bakgrundsbild från Bing
Exec=/bin/bash -c "cd $PROJECT_PATH && source venv/bin/activate && python src/main.py"
Icon=preferences-desktop-wallpaper
Terminal=false
Categories=Utility;Graphics;
Keywords=wallpaper;bakgrund;bild;
StartupNotify=true
EOF

# Gör filen körbar
chmod +x "$DESKTOP_FILE"

echo "✅ Desktop launcher skapad!"
echo ""
echo "📍 Fil: $DESKTOP_FILE"
echo "📂 Projekt: $PROJECT_PATH"
echo ""
echo "🎉 Du kan nu starta programmet från:"
echo "   - Applikationsmenyn (sök efter 'SearchWallpaper')"
echo "   - Cinnamon-menyn under 'Tillbehör' eller 'Verktyg'"
echo ""
echo "💡 Tips: Högerklicka på ikonen i menyn och välj 'Lägg till på skrivbord'"
echo "         för snabbåtkomst!"
