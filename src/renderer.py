from PIL import Image, ImageDraw
import datetime

from core.constants import (
    BASE_WALLPAPER,
    OUTPUT_DIR,
    OUTPUT_IMAGE
)

from core.config import (
    load_coordinates,
    load_settings
)

from core.logger import logger

from core.validator import validate


# ==========================================================
# Main
# ==========================================================

def main():

    # ------------------------------------------------------
    # Validate Project
    # ------------------------------------------------------

    validate()

    # ------------------------------------------------------
    # Load Resources
    # ------------------------------------------------------

    logger.info("Loading wallpaper...")

    wallpaper = Image.open(BASE_WALLPAPER).convert("RGBA")

    logger.info("Loading coordinates...")

    coordinates = load_coordinates()

    logger.info("Loading settings...")

    settings = load_settings()

    # ------------------------------------------------------
    # Current Day
    # ------------------------------------------------------

    today = datetime.datetime.now().strftime("%A")

    logger.info(f"Today detected: {today}")

    if today not in coordinates:
        raise KeyError(f"Coordinates for '{today}' were not found.")

    rect = coordinates[today]

    # ------------------------------------------------------
    # Settings
    # ------------------------------------------------------

    padding = settings["highlight"]["padding"]

    border_radius = settings["highlight"]["border_radius"]

    border_width = settings["highlight"]["border_width"]

    border_color = tuple(
        settings["highlight"]["border_color"]
    )

    overlay_opacity = settings["overlay"]["opacity"]

    # ------------------------------------------------------
    # Rectangle
    # ------------------------------------------------------

    left = max(
        0,
        rect["left"] - padding
    )

    top = max(
        0,
        rect["top"] - padding
    )

    right = min(
        wallpaper.width,
        rect["right"] + padding
    )

    bottom = min(
        wallpaper.height,
        rect["bottom"] + padding
    )

    # ------------------------------------------------------
    # Overlay
    # ------------------------------------------------------

    logger.info("Creating dark overlay...")

    overlay = Image.new(
        "RGBA",
        wallpaper.size,
        (
            0,
            0,
            0,
            overlay_opacity
        )
    )

    result = Image.alpha_composite(
        wallpaper,
        overlay
    )

    # ------------------------------------------------------
    # Restore Today's Section
    # ------------------------------------------------------

    logger.info("Restoring highlighted region...")

    today_crop = wallpaper.crop(
        (
            left,
            top,
            right,
            bottom
        )
    )

    result.paste(
        today_crop,
        (
            left,
            top
        )
    )

    # ------------------------------------------------------
    # Draw Border
    # ------------------------------------------------------

    logger.info("Drawing border...")

    draw = ImageDraw.Draw(result)

    draw.rounded_rectangle(
        (
            left,
            top,
            right,
            bottom
        ),
        outline=border_color,
        width=border_width,
        radius=border_radius
    )

    # ------------------------------------------------------
    # Save
    # ------------------------------------------------------

    OUTPUT_DIR.mkdir(
        exist_ok=True
    )

    logger.info("Saving wallpaper...")

    result.save(
        OUTPUT_IMAGE
    )

    logger.success(
        "Wallpaper generated successfully!"
    )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except Exception as error:

        logger.error(str(error))