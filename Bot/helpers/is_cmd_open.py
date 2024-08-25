import psutil


def is_cmd_open() -> bool:
    """
    Function is check is cmd open
    :return: bool
    """
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'] == 'cmd.exe':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False
