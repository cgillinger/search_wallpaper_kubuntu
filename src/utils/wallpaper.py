"""
Modul för att hantera nedladdning av bilder och inställning av skrivbordsbakgrund.
Plattformsoberoende version med stöd för Windows, macOS och Linux (KDE Plasma, Cinnamon, MATE, GNOME, Enlightenment).
"""
import os
import ctypes
import platform
import logging
import subprocess
import requests
from PIL import Image
from io import BytesIO
logger = logging.getLogger(__name__)
def download_image(url: str, save_path: str) -> bool:
    """
    Laddar ner en bild från en URL och sparar den lokalt.
    Verifierar också att bilden är i landskapsformat och har tillräcklig upplösning.

    Args:
        url (str): URL:en till bilden som ska laddas ner
        save_path (str): Sökvägen där bilden ska sparas

    Returns:
        bool: True om nedladdningen lyckades, False annars
    """
    try:
        # Skapa katalogen om den inte finns
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Hämta bilden
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Öppna bilden med PIL för att verifiera format och dimensioner
        img = Image.open(BytesIO(response.content))
        width, height = img.size

        # Verifiera att bilden är i landskapsformat och har tillräcklig upplösning
        if width < height:
            logger.error(f"Bilden är i porträttformat: {width}x{height}")
            return False

        if width < 1920 or height < 1080:
            logger.error(f"Bilden har för låg upplösning: {width}x{height}")
            return False

        # Spara bilden
        img.save(save_path, quality=95)
        logger.info(f"Bild sparad: {save_path}")
        return True

    except Exception as e:
        logger.error(f"Fel vid nedladdning av bild: {str(e)}")
        return False
def set_wallpaper_windows(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på Windows.

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        SPI_SETDESKWALLPAPER = 0x0014
        SPIF_UPDATEINIFILE = 0x01
        SPIF_SENDCHANGE = 0x02

        if ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
        ):
            logger.info("Bakgrundsbild inställd på Windows")
            return True
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på Windows: {str(e)}")
        return False
def set_wallpaper_cinnamon(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på Cinnamon (Linux Mint standard).

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        result = subprocess.run([
            'gsettings', 'set',
            'org.cinnamon.desktop.background',
            'picture-uri',
            f'file://{image_path}'
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            logger.info("Bakgrundsbild inställd på Cinnamon")
            return True
        else:
            logger.error(f"gsettings misslyckades: {result.stderr}")
            return False

    except FileNotFoundError:
        logger.error("gsettings kunde inte hittas - Cinnamon installerad?")
        return False
    except subprocess.TimeoutExpired:
        logger.error("Timeout vid gsettings-anrop")
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på Cinnamon: {str(e)}")
        return False
def set_wallpaper_kde(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på KDE Plasma.
    Försöker först plasma-apply-wallpaperimage, sedan dbus som fallback.

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    # Metod 1: plasma-apply-wallpaperimage (enklaste och mest pålitliga)
    try:
        result = subprocess.run([
            'plasma-apply-wallpaperimage',
            image_path
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            logger.info("Bakgrundsbild inställd på KDE Plasma via plasma-apply-wallpaperimage")
            return True
        else:
            logger.warning(f"plasma-apply-wallpaperimage misslyckades: {result.stderr}")
    except FileNotFoundError:
        logger.warning("plasma-apply-wallpaperimage inte tillgängligt, försöker dbus...")
    except Exception as e:
        logger.warning(f"plasma-apply-wallpaperimage fel: {str(e)}, försöker dbus...")

    # Metod 2: dbus (fallback)
    try:
        # JavaScript-skript för att ändra bakgrundsbild i KDE Plasma
        script = f'''
const desktops = desktops();
for (let i = 0; i < desktops.length; i++) {{
    desktops[i].wallpaperPlugin = "org.kde.image";
    desktops[i].currentConfigGroup = ["Wallpaper", "org.kde.image", "General"];
    desktops[i].writeConfig("Image", "file://{image_path}");
}}
'''

        # Skicka skript till plasmashell via dbus
        result = subprocess.run([
            'dbus-send',
            '--session',
            '--dest=org.kde.plasmashell',
            '--type=method_call',
            '/PlasmaShell',
            'org.kde.PlasmaShell.evaluateScript',
            f'string:{script}'
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            logger.info("Bakgrundsbild inställd på KDE Plasma via dbus")
            return True
        else:
            logger.error(f"dbus-send misslyckades: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        logger.error("Timeout vid dbus-anrop")
        return False
    except FileNotFoundError:
        logger.error("dbus-send kunde inte hittas - KDE Plasma installerad?")
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på KDE: {str(e)}")
        return False
def set_wallpaper_gnome(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på GNOME/Unity.
    Stöder både ljust och mörkt tema.

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        # Sätt både picture-uri (ljust tema) och picture-uri-dark (mörkt tema)
        subprocess.run([
            'gsettings', 'set',
            'org.gnome.desktop.background',
            'picture-uri',
            f'file://{image_path}'
        ], capture_output=True, timeout=10, check=True)

        subprocess.run([
            'gsettings', 'set',
            'org.gnome.desktop.background',
            'picture-uri-dark',
            f'file://{image_path}'
        ], capture_output=True, timeout=10, check=True)

        logger.info("Bakgrundsbild inställd på GNOME/Unity")
        return True
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på GNOME: {str(e)}")
        return False
def set_wallpaper_mate(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på MATE Desktop.

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        result = subprocess.run([
            'gsettings', 'set',
            'org.mate.background',
            'picture-filename',
            image_path
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            logger.info("Bakgrundsbild inställd på MATE")
            return True
        else:
            logger.error(f"gsettings misslyckades: {result.stderr}")
            return False

    except FileNotFoundError:
        logger.error("gsettings kunde inte hittas - MATE installerad?")
        return False
    except subprocess.TimeoutExpired:
        logger.error("Timeout vid gsettings-anrop")
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på MATE: {str(e)}")
        return False
def set_wallpaper_enlightenment(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på Enlightenment (E17/E18+).

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        # enlightenment_remote -desktop-bg-add ZONE DESK X Y /path/to/image
        # 0 0 0 0 = zone 0, desktop 0, position 0,0
        result = subprocess.run([
            'enlightenment_remote',
            '-desktop-bg-add',
            '0', '0', '0', '0',
            image_path
        ], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            logger.info("Bakgrundsbild inställd på Enlightenment")
            return True
        else:
            logger.error(f"enlightenment_remote misslyckades: {result.stderr}")
            return False

    except FileNotFoundError:
        logger.error("enlightenment_remote kunde inte hittas - Enlightenment installerad?")
        return False
    except subprocess.TimeoutExpired:
        logger.error("Timeout vid enlightenment_remote-anrop")
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på Enlightenment: {str(e)}")
        return False
def set_wallpaper_macos(image_path: str) -> bool:
    """
    Sätter bakgrundsbild på macOS.

    Args:
        image_path (str): Absolut sökväg till bilden

    Returns:
        bool: True om lyckades, False annars
    """
    try:
        from appscript import app, mactypes
        app('Finder').desktop_picture.set(mactypes.File(image_path))
        logger.info("Bakgrundsbild inställd på macOS")
        return True
    except ImportError:
        logger.error("appscript krävs för att ändra bakgrundsbild på macOS")
        return False
    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild på macOS: {str(e)}")
        return False
def set_wallpaper(image_path: str) -> bool:
    """
    Sätter den angivna bilden som skrivbordsbakgrund.
    Plattformsoberoende - detekterar automatiskt operativsystem och skrivbordsmiljö.

    Stöd för:
    - Windows
    - macOS
    - Linux: KDE Plasma, Cinnamon, MATE, GNOME, Unity, Enlightenment

    Args:
        image_path (str): Sökvägen till bilden som ska användas

    Returns:
        bool: True om inställningen lyckades, False annars
    """
    try:
        # Konvertera relativ sökväg till absolut
        abs_path = os.path.abspath(image_path)

        if not os.path.exists(abs_path):
            logger.error(f"Bilden kunde inte hittas: {abs_path}")
            return False

        # Detektera operativsystem
        system = platform.system().lower()

        if system == "windows":
            return set_wallpaper_windows(abs_path)

        elif system == "darwin":  # macOS
            return set_wallpaper_macos(abs_path)

        elif system == "linux":
            # Detektera skrivbordsmiljö
            desktop = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
            logger.info(f"Detekterad skrivbordsmiljö: {desktop}")

            # Cinnamon (Linux Mint standard)
            if 'cinnamon' in desktop:
                return set_wallpaper_cinnamon(abs_path)

            # KDE Plasma
            elif 'kde' in desktop or 'plasma' in desktop:
                return set_wallpaper_kde(abs_path)

            # MATE Desktop
            elif 'mate' in desktop:
                return set_wallpaper_mate(abs_path)

            # Enlightenment
            elif 'enlightenment' in desktop or 'e17' in desktop or 'e18' in desktop or 'e19' in desktop:
                return set_wallpaper_enlightenment(abs_path)

            # GNOME/Unity
            elif 'gnome' in desktop or 'unity' in desktop:
                return set_wallpaper_gnome(abs_path)

            # Okänd skrivbordsmiljö - intelligent fallback
            else:
                logger.warning(f"Okänd skrivbordsmiljö: {desktop}, försöker alla metoder...")

                # Försök i prioritetsordning baserat på vanligaste Linux-distributioner
                methods = [
                    ('Cinnamon', set_wallpaper_cinnamon),
                    ('KDE Plasma', set_wallpaper_kde),
                    ('MATE', set_wallpaper_mate),
                    ('Enlightenment', set_wallpaper_enlightenment),
                    ('GNOME', set_wallpaper_gnome)
                ]

                for name, method in methods:
                    logger.info(f"Försöker {name}...")
                    if method(abs_path):
                        logger.info(f"Lyckades med {name}")
                        return True

                logger.error("Ingen metod fungerade")
                return False
        else:
            logger.error(f"Operativsystemet stöds inte: {system}")
            return False

    except Exception as e:
        logger.error(f"Fel vid inställning av bakgrundsbild: {str(e)}")
        return False
