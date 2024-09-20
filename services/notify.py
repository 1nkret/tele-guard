import asyncio

from plyer import notification
from os import system
from Bot.core.config import bot
from Bot.utils.access.members import get_from_json_members
from services.config import logger


async def notify_windows(
        title: str,
        message: str,
        config=None,
        app_name: str = "Telegram Desktop",
        timeout: int = 10
) -> None:
    """
    Notify windows
    :param config: your config (variable with loaded config.yaml)
    :param title: title
    :param message: message_echo on notify
    :param app_name: app name
    :param timeout: timeout to close notify
    :return: None
    """
    if config is None:
        config = {"exit_count": 0}
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
        timeout=timeout
    )
    if config["exit_count"] in [3, 5, 6] or config["exit_count"] > 6:
        logger.info("Shutdown process start.")
        for aci in get_from_json_members():
            await bot.send_message(aci, "Admin: Your PC is turning off.")
            await asyncio.sleep(0.1)

        system("shutdown /s /t 3")
