from pathlib import Path
import sys

# ==========================================================
# Detect Runtime Environment
# ==========================================================

if getattr(sys, "frozen", False):
    # Running as a PyInstaller executable

    RESOURCE_DIR = Path(sys._MEIPASS)

    PROJECT_ROOT = Path(sys.executable).parent

else:
    # Running from source code

    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

    RESOURCE_DIR = PROJECT_ROOT

# ==========================================================
# Directories
# ==========================================================

ASSETS_DIR = RESOURCE_DIR / "Assets"

CONFIG_DIR = RESOURCE_DIR / "Config"

OUTPUT_DIR = PROJECT_ROOT / "Output"

# ==========================================================
# Files
# ==========================================================

BASE_WALLPAPER = ASSETS_DIR / "base_wallpaper.png"

COORDINATES_JSON = CONFIG_DIR / "coordinates.json"

SETTINGS_JSON = CONFIG_DIR / "settings.json"

OUTPUT_IMAGE = OUTPUT_DIR / "output.png"

# ==========================================================
# Ensure Output Directory Exists
# ==========================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)