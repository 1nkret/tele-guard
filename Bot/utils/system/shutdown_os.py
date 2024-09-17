import sys
import os


def shutdown_os() -> None:
    """
    Shutdown os (bye!)
    :return: None
    """
    if sys.platform == "win32":
        os.system("shutdown /s /t 1")
    elif sys.platform == "linux" or sys.platform == "darwin":
        os.system("shutdown -h now")
