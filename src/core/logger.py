from datetime import datetime


class Logger:
    """
    Simple console logger for the Dynamic Wallpaper project.
    """

    def _timestamp(self):
        return datetime.now().strftime("%H:%M:%S")

    def info(self, message):
        print(f"[{self._timestamp()}] INFO     {message}")

    def success(self, message):
        print(f"[{self._timestamp()}] SUCCESS  {message}")

    def warning(self, message):
        print(f"[{self._timestamp()}] WARNING  {message}")

    def error(self, message):
        print(f"[{self._timestamp()}] ERROR    {message}")


logger = Logger()