from plyer import notification
from os import system
from Bot.helpers.send_message import send_message
from services.config import logger


async def notify_windows(
        config,
        title: str,
        message: str,
        app_name: str = "Telegram Desktop",
        timeout: int = 10
) -> None:
    """
    Notify windows
    :param config: your config (variable with loaded config.yaml)
    :param title: title
    :param message: message on notify
    :param app_name: app name
    :param timeout: timeout to close notify
    :return: None
    """
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
        timeout=timeout
    )
    if config["exit_count"] in [3, 5, 6] or config["exit_count"] > 6:
        logger.info("Shutdown process start.")
        await send_message(f"Session is closed.")
        system("shutdown /s /t 3")
