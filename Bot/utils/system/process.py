import logging

import psutil


def get_process_iter():
    cache = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            cache.append(
                {
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "user": proc.info['username'],
                    "cpu": proc.info['cpu_percent'],
                    "memory": proc.info['memory_percent'],
                }
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return sorted(cache, key=lambda x: x['name'])


def get_process(pid) -> dict:
    try:
        process = psutil.Process(int(pid))

        return {
                "name": process.name(),
                "user": process.username(),
                "cpu": process.cpu_percent(),
                "memory": process.memory_percent()
        }
    except psutil.NoSuchProcess:
        return dict()


def count_processes_by_name(process_name):
    return sum(1 for proc in psutil.process_iter(['name']) if proc.info['name'] == process_name)


def kill_process_by_pid(pid) -> str:
    try:
        proc = psutil.Process(int(pid))
        proc.kill()
        logging.info(f"Process with PID {pid} is killed.")
        return f"Process with PID {pid} is killed."
    except psutil.NoSuchProcess:
        logging.info(f"Process with PID {pid} not found.")
        return f"Process with PID {pid} not found."
    except psutil.AccessDenied:
        logging.warning(f"You haven't permissions to kill process with PID {pid}.")
        return f"You haven't permissions to kill process with PID {pid}."
    except ValueError:
        return "Invalid PID format."
