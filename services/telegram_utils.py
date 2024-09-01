import psutil

from services.config import save_config, logger


def is_telegram_open() -> bool:
    """
    Is Telegram.exe opened
    :return: bool
    """
    telegram_process = next(
        (
            proc for proc in psutil.process_iter(['pid', 'name']) if proc.info['name'] == 'Telegram.exe'
        ), None
    )
    return True if telegram_process else False


def close_telegram(config) -> None:
    """
    End process Telegram.exe
    :param config: cfg yaml
    :return: None
    """
    try:
        telegram_process = next(
            (proc for proc in psutil.process_iter(['pid', 'name']) if proc.info['name'] == 'Telegram.exe'), None)
        if telegram_process:
            telegram_process.terminate()
            telegram_process.wait()
            config["exit_count"] += 1
            save_config(config)
            logger.info(f'Process Telegram (PID {telegram_process.pid}) is shutdown.')
        else:
            logger.info('Process Telegram not found.')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        logger.warning(f'Cant shutdown process Telegram: {e}')
