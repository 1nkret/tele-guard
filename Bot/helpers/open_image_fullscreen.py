from PIL import Image, ImageTk
import tkinter as tk


async def open_image_fullscreen(image_path: str) -> None:
    """
    Function is open image to fullscreen taken from image_path
    :param image_path: your path to img
    :return: None
    """
    root = tk.Tk()
    root.title("Fullscreen Image Viewer")

    image = Image.open(image_path)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    image = image.resize((screen_width, screen_height), Image.FIXED)

    tk_image = ImageTk.PhotoImage(image)

    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)

    label = tk.Label(root, image=tk_image)
    label.pack(expand=True)

    root.mainloop()
