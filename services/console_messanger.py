import os
import subprocess
import time
import asyncio
import psutil
import ctypes

from colorama import Fore
from random import uniform, randint

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def show_error(
        title: str,
        message: str
) -> None:
    """
    Show error with your tittle and message on computer
    :param title: title
    :param message: message
    :return: None
    """
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x10 | 0x40000)


def set_console_title(title: str) -> None:
    """
    Set your title on cmd. (Only for windows)
    :param title: title
    :return: None
    """
    if os.name == 'nt':
        os.system(f'title {title}')


def clear_console() -> None:
    """
    Clear console (Only for windows)
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


async def type_text(
        text: str,
        delay: float
) -> None:
    """
    Beautiful typing text...
    :param text: Message
    :param delay: your delay (example: 0.6)
    :return: None
    """
    for char in text:
        print(f"{Fore.GREEN}{char}", end='', flush=True)
        time.sleep(delay)


def set_window_size(
        width: int,
        height: int
) -> None:
    """
    Set your window size
    :param width: width
    :param height: height
    :return: None
    """
    if os.name == 'nt':
        os.system(f'mode con: cols={width} lines={height}')


def close_cmd() -> None:
    """
    Casual close cmd
    :return: None
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.name() == 'cmd.exe':
            try:
                proc.terminate()
                proc.wait()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                pass


async def spam_on_start() -> None:
    """
    Spam at launch cmd with good looks animations :)
    :return: None
    """
    welcome_text = """
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝"""

    print(f"""{Fore.GREEN}{welcome_text}\n\n""")

    print(f"{Fore.GREEN}Username: ", end='', flush=True)
    await type_text("admin", delay=uniform(0.05, 0.2))
    print()

    print(f"{Fore.GREEN}Password: ", end='', flush=True)
    await type_text("***********", delay=uniform(0.05, 0.2))

    time.sleep(1)
    print(f"\n\n{Fore.GREEN}Access Granted!")
    time.sleep(2)
    s = ""
    while len(s) < 15000:
        print(f"{Fore.GREEN}{s}", end="")
        for _ in range(59):
            s += f"{randint(0, 1)}"
        time.sleep(0.05)

    clear_console()
    print(f"{Fore.GREEN}{uniform(0, 10)} BTC founded.")

    time.sleep(8)


async def main() -> None:
    """
    Main function with configure
    :return: None
    """
    set_console_title("Scanner")
    set_window_size(65, 20)
    clear_console()
    await spam_on_start()
    close_cmd()


async def start_prank() -> None:
    """
    Alternative launch cmd prank. (on another window)
    :return: None
    """
    local_path = os.path.abspath(os.getcwd())
    python_path = os.path.join(local_path, '.venv', 'Scripts', 'python.exe')
    script_path = os.path.join(local_path, 'services', 'console_messanger.py')

    if not os.path.isfile(python_path):
        print(f"Ошибка: Python не найден по пути {python_path}")
        return
    if not os.path.isfile(script_path):
        print(f"Ошибка: Скрипт не найден по пути {script_path}")
        return

    try:
        subprocess.Popen(['start', 'cmd', '/k', python_path, script_path], cwd=local_path, shell=True)
    except Exception as e:
        print(f"Ошибка при запуске скрипта: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
