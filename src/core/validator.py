from pathlib import Path

from core.constants import (
    BASE_WALLPAPER,
    COORDINATES_JSON,
    SETTINGS_JSON,
    OUTPUT_DIR
)

from core.config import (
    load_coordinates,
    load_settings
)

from core.logger import logger


# ==========================================================
# Validate Required Files
# ==========================================================

def validate_files():

    logger.info("Checking required files...")

    required_files = [
        BASE_WALLPAPER,
        COORDINATES_JSON,
        SETTINGS_JSON
    ]

    for file in required_files:

        if not file.exists():

            raise FileNotFoundError(
                f"\nRequired file not found:\n{file}"
            )

    OUTPUT_DIR.mkdir(exist_ok=True)

    logger.success("All required files found.")


# ==========================================================
# Validate Settings
# ==========================================================

def validate_settings():

    logger.info("Validating settings...")

    settings = load_settings()

    required = {

        "overlay": [
            "opacity"
        ],

        "highlight": [
            "padding",
            "border_radius",
            "border_width",
            "border_color"
        ],

        "output": [
            "filename"
        ]
    }

    for section in required:

        if section not in settings:

            raise KeyError(
                f"Missing section '{section}' in settings.json"
            )

        for key in required[section]:

            if key not in settings[section]:

                raise KeyError(
                    f"Missing key '{key}' in settings.json"
                )

    logger.success("Settings validated.")


# ==========================================================
# Validate Coordinates
# ==========================================================

def validate_coordinates():

    logger.info("Validating coordinates...")

    coordinates = load_coordinates()

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for day in days:

        if day not in coordinates:

            raise KeyError(
                f"Missing coordinates for {day}"
            )

        required = [
            "left",
            "top",
            "right",
            "bottom"
        ]

        for key in required:

            if key not in coordinates[day]:

                raise KeyError(
                    f"{day} is missing '{key}'"
                )

    logger.success("Coordinates validated.")


# ==========================================================
# Validate Everything
# ==========================================================

def validate():

    validate_files()

    validate_settings()

    validate_coordinates()

    logger.success("Validation completed successfully.")