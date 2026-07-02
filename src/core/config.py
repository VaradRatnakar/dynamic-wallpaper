import json

from core.constants import (
    COORDINATES_JSON,
    SETTINGS_JSON
)

# ==========================================================
# Load Coordinates
# ==========================================================

def load_coordinates():
    """
    Load coordinates.json
    """

    with open(COORDINATES_JSON, "r") as file:
        return json.load(file)

# ==========================================================
# Load Settings
# ==========================================================

def load_settings():
    """
    Load settings.json
    """

    with open(SETTINGS_JSON, "r") as file:
        return json.load(file)