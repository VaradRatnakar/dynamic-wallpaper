from pathlib import Path
import sys

# ==========================================================
# Add src to Python Path
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

# ==========================================================
# Imports
# ==========================================================

from core.logger import logger

from renderer import main as render_wallpaper
from wallpaper import main as apply_wallpaper

# ==========================================================
# Main
# ==========================================================

def main():

    logger.info("=" * 50)
    logger.info("Dynamic Wallpaper")
    logger.info("=" * 50)

    render_wallpaper()

    apply_wallpaper()

    logger.success("Dynamic Wallpaper Updated Successfully!")

# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    try:
        main()

    except Exception as error:
        logger.error(str(error))