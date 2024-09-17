import logging
import psutil
import asyncio
from concurrent.futures import ThreadPoolExecutor


critical_processes = [
    "csrss.exe", "lsass.exe", "wininit.exe", "smss.exe",
    "services.exe", "fontdrvhost.exe", "winlogon.exe",
    "ui32.exe", "dllhost.exe"
]

system_processes = [
    'explorer.exe', 'svchost.exe', 'System Idle Process',
    'System', 'python3.10.exe', "python.exe", 'pycharm64.exe',
    'wallpaperservice32.exe', "wallpaper64.exe", "Lightshot.exe",
    "dwm.exe", "nvcontainer.exe", "wallpaper32.exe", "gamingservices.exe",
    "NVDisplay.Container.exe", "RuntimeBroker.exe", "NVIDIA Web Helper.exe",
    "sihost.exe", "cmd.exe", "pythonw3.10.exe", "SearchFilterHost.exe", "audiodg.exe",
    "RtkAudUService64.exe", "SearchApp.exe", "NVIDIA Share.exe", "SearchProtocolHost.exe",
    "ctfmon.exe", "fsnotifier.exe", "SearchIndexer.exe", "pythonw.exe"
]
system_users = ['SYSTEM', 'LOCAL SERVICE', 'NETWORK SERVICE']

executor = ThreadPoolExecutor()


async def terminate_process(proc):
    loop = asyncio.get_event_loop()
    process_name = proc.info['name']
    process_pid = proc.info['pid']
    process_user = proc.info.get('username', '')

    if process_name.lower() in critical_processes:
        logging.info(f"Процесс {process_name} (PID: {process_pid}) является брадом и не будет скушан.")
        return

    if process_user in system_users:
        logging.info(
            f"Процесс {process_name} (PID: {process_pid}) запущен от имени бибизяна и не будет скушан.")
        return

    try:
        logging.info(f"Кушаем процесс... {process_name} (PID: {process_pid})")
        await loop.run_in_executor(executor, proc.terminate)
        await loop.run_in_executor(executor, proc.wait, 1)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    except Exception as e:
        logging.error(f"Процесс слишком крутой шоп его кушат {process_name} (PID: {process_pid}): {e}")


async def close_all_windows():
    tasks = []
    logging.info("Начинаем кушать процессы.")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if (proc.info['name'] not in system_processes
                and proc.info['username'] is not None):
            tasks.append(asyncio.create_task(terminate_process(proc)))
    logging.info("я покушал")
    await asyncio.gather(*tasks)


