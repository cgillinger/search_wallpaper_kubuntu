"""
Hantering av sökvägar för SearchWallpaper
Plattformsoberoende version med stöd för Windows och Linux (XDG Base Directory).
"""
import os
import sys
import platform
import logging
from typing import Dict

logger = logging.getLogger(__name__)

def get_executable_dir():
    """
    Hämtar sökvägen till mappen där programmet körs.
    Hanterar både utvecklingsläge och exe-läge.
    """
    if getattr(sys, 'frozen', False):
        # Körs som exe
        return os.path.dirname(sys.executable)
    else:
        # Körs i utvecklingsläge
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_app_paths() -> Dict[str, str]:
    """
    Hämtar alla viktiga sökvägar för applikationen.
    Skapar mapparna om de inte finns.
    
    Använder plattformsspecifika standarder:
    - Windows: Samma mapp som exe-filen
    - Linux: XDG Base Directory (~/.local/share/SearchWallpaper/)
    
    Returns:
        Dict[str, str]: Dictionary med alla viktiga sökvägar
    """
    try:
        system = platform.system().lower()
        
        if system == "linux":
            # Använd XDG Base Directory-standard för Linux
            xdg_data = os.environ.get('XDG_DATA_HOME', 
                                      os.path.expanduser('~/.local/share'))
            base_dir = os.path.join(xdg_data, 'SearchWallpaper')
            logger.info(f"Linux detekterat - använder XDG sökväg: {base_dir}")
        else:
            # Windows: Använd samma mapp som exe-filen
            base_dir = get_executable_dir()
            logger.info(f"Windows detekterat - använder exe-mapp: {base_dir}")
        
        paths = {
            'program_data': base_dir,
            'history_file': os.path.join(base_dir, 'history.json'),
            'logs_dir': os.path.join(base_dir, 'logs'),
            'cache_dir': os.path.join(base_dir, 'cache'),
            'daily_count_file': os.path.join(base_dir, 'daily_search_count.json'),
        }
        
        # Skapa alla mappar
        for path in [paths['logs_dir'], paths['cache_dir']]:
            if not os.path.exists(path):
                os.makedirs(path, mode=0o755)
                logger.info(f"Skapade mapp: {path}")
        
        return paths
        
    except Exception as e:
        logger.error(f"Fel vid skapande av applikationsmappar: {str(e)}")
        # Fallback till safe defaults
        base_dir = get_executable_dir()
        return {
            'program_data': base_dir,
            'history_file': os.path.join(base_dir, 'history.json'),
            'logs_dir': os.path.join(base_dir, 'logs'),
            'cache_dir': os.path.join(base_dir, 'cache'),
            'daily_count_file': os.path.join(base_dir, 'daily_search_count.json'),
        }

def is_admin() -> bool:
    """
    Kontrollerar om programmet körs med administratörsrättigheter.
    Plattformsoberoende.
    
    Returns:
        bool: True om programmet körs som administratör/root
    """
    try:
        system = platform.system().lower()
        
        if system == "windows":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        elif system == "linux":
            return os.geteuid() == 0
        else:
            return False
    except Exception as e:
        logger.error(f"Fel vid kontroll av admin-status: {str(e)}")
        return False

def needs_admin() -> bool:
    """
    Kontrollerar om programmet behöver administratörsrättigheter
    baserat på var det försöker spara filer.
    
    Returns:
        bool: True om admin-rättigheter behövs
    """
    try:
        test_dir = get_executable_dir()
        test_file = os.path.join(test_dir, 'test.tmp')
        
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return False
    except Exception as e:
        logger.warning(f"Skrivtest misslyckades: {str(e)}")
        return True
