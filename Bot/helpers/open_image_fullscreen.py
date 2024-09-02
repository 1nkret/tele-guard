import tkinter as tk
from PIL import Image, ImageTk
import asyncio
from services.config import logger


def open_image_fullscreen_sync(
        image_path: str,
        title: str) -> None:
    root = tk.Tk()
    root.title(title)

    logger.info("Start loading image viewer...")
    image = Image.open(image_path)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    image = image.resize((screen_width, screen_height), Image.LANCZOS)

    tk_image = ImageTk.PhotoImage(image)

    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)

    logger.info("Open image")
    label = tk.Label(root, image=tk_image)
    label.pack(expand=True)

    root.mainloop()
    logger.info("Image is loaded.")


async def open_image_fullscreen(
        image_path: str,
        title: str = "Fullscreen Image Viewer"
) -> None:
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, open_image_fullscreen_sync, image_path, title)
