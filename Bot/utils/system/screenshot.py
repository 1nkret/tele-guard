import pyautogui
import os


def screenshot(
        path: str = "media/screen/",
        filename: str = "screenshot"
):
    os.makedirs(path, exist_ok=True)

    file = os.path.join(path, filename + ".png")
    screen = pyautogui.screenshot()
    screen.save(file)

    return file
