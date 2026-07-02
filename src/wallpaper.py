import ctypes

from core.constants import OUTPUT_IMAGE
from core.logger import logger


# ==========================================================
# Main
# ==========================================================

def main():

    logger.info("Applying wallpaper...")

    wallpaper_path = str(
        OUTPUT_IMAGE.resolve()
    )

    ctypes.windll.user32.SystemParametersInfoW(
        20,
        0,
        wallpaper_path,
        3
    )

    logger.success(
        "Wallpaper applied successfully!"
    )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except Exception as error:

        logger.error(str(error))