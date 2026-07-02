import cv2
import json
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

IMAGE_PATH = PROJECT_ROOT / "Assets" / "base_wallpaper.png"
CONFIG_PATH = PROJECT_ROOT / "Config" / "coordinates.json"

# ==========================================================
# Load Wallpaper
# ==========================================================

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(
        f"Could not load:\n{IMAGE_PATH}"
    )

# ==========================================================
# Window Settings
# ==========================================================

WINDOW_NAME = "Dynamic Wallpaper Setup"

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

# ==========================================================
# Days
# ==========================================================

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

current_day = 0

# ==========================================================
# Rectangle Storage
# ==========================================================

saved_rectangles = {}

rectangle_order = []

drawing = False

start_x = 0
start_y = 0

current_x = 0
current_y = 0

# ==========================================================
# Mouse Callback
# ==========================================================

def mouse_callback(event, x, y, flags, param):
    global drawing
    global start_x, start_y
    global current_x, current_y
    global current_day

    # Start Drawing
    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True

        start_x = x
        start_y = y

        current_x = x
        current_y = y

    # Update Rectangle
    elif event == cv2.EVENT_MOUSEMOVE and drawing:

        current_x = x
        current_y = y

    # Finish Drawing
    elif event == cv2.EVENT_LBUTTONUP and drawing:

        drawing = False

        current_x = x
        current_y = y

        left = min(start_x, current_x)
        top = min(start_y, current_y)
        right = max(start_x, current_x)
        bottom = max(start_y, current_y)

        saved_rectangles[DAYS[current_day]] = {
            "left": left,
            "top": top,
            "right": right,
            "bottom": bottom
        }
        rectangle_order.append(DAYS[current_day])

        current_day += 1

        # Finished all days
        if current_day >= len(DAYS):

            with open(CONFIG_PATH, "w") as file:
                json.dump(saved_rectangles, file, indent=4)

            print("coordinates.json saved successfully!")

            cv2.destroyAllWindows()
            raise SystemExit
        # ==========================================================
# Create Window
# ==========================================================

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

cv2.resizeWindow(
    WINDOW_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

cv2.setMouseCallback(
    WINDOW_NAME,
    mouse_callback
)

# ==========================================================
# Main Loop
# ==========================================================

while True:

    # Create a fresh copy every frame
    display_image = image.copy()

    # ------------------------------------------------------
    # Draw Saved Rectangles (Green)
    # ------------------------------------------------------

    for rectangle in saved_rectangles.values():

        cv2.rectangle(
            display_image,
            (rectangle["left"], rectangle["top"]),
            (rectangle["right"], rectangle["bottom"]),
            (0, 255, 0),
            2
        )

    # ------------------------------------------------------
    # Draw Current Rectangle (Red)
    # ------------------------------------------------------

    if drawing:

        cv2.rectangle(
            display_image,
            (start_x, start_y),
            (current_x, current_y),
            (0, 0, 255),
            2
        )

    # ------------------------------------------------------
    # Current Day Text
    # ------------------------------------------------------

    if current_day < len(DAYS):

        cv2.putText(
            display_image,
            f"Draw: {DAYS[current_day]}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    # ------------------------------------------------------
    # Instructions
    # ------------------------------------------------------

    cv2.putText(
        display_image,
        "Left Click + Drag : Draw Rectangle",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (220, 220, 220),
        2
    )

    cv2.putText(
        display_image,
        "ESC : Exit",
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (220, 220, 220),
        2
    )

    # ------------------------------------------------------
    # Display
    # ------------------------------------------------------

    cv2.imshow(
        WINDOW_NAME,
        display_image
    )

    key = cv2.waitKey(1) & 0xFF

    # ------------------------------------------------------
    # Undo (Backspace)
    # ------------------------------------------------------

    if key == 8:

     if rectangle_order:

        last_day = rectangle_order.pop()

        del saved_rectangles[last_day]

        current_day -= 1
    

    if key == 27:
        break

    if cv2.getWindowProperty(
        WINDOW_NAME,
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

# ==========================================================
# Cleanup
# ==========================================================

cv2.destroyAllWindows()