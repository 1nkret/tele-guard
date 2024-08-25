import psutil
import logging

from services.config import save_config

logger = logging.getLogger(__name__)


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
        telegram_process = next((proc for proc in psutil.process_iter(['pid', 'name']) if proc.info['name'] == 'Telegram.exe'), None)
        if telegram_process:
            telegram_process.terminate()
            telegram_process.wait()
            config["exit_count"] += 1
            save_config(config)
            logger.info(f'Процесс Telegram (PID {telegram_process.pid}) завершен.')
        else:
            logger.info('Процесс Telegram не найден.')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        logger.warning(f'Не удалось завершить процесс Telegram: {e}')