import asyncio

from aiogram.exceptions import TelegramNetworkError
from Bot.core.config import bot, logger
from Bot.apps.menu.keyboard import get_main_menu
from Bot.utils.access.members import get_from_json_members


async def message_start_session() -> None:
    """
    Function is send message_echo to allowed users on start session.
    :return: None
    """
    tries = 0

    try:
        for aci in get_from_json_members():
            await bot.send_message(
                chat_id=aci,
                text="Session is started.",
                reply_markup=get_main_menu(aci)
            )
            await asyncio.sleep(0.1)
        tries = 0
        logger.info("All users are notified that the computer is running.")
    except TelegramNetworkError:
        tries += 1
        logger.warning(f"Bad connect with ethernet. Tries {tries}")
        await asyncio.sleep(tries)
