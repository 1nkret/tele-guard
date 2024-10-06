import asyncio

from aiogram.exceptions import TelegramNetworkError
from Bot.core.config import dp, bot, logger
from Bot.utils.loader.router_loader import load_routers

from Bot.utils.chat.message_start_session import message_start_session


async def start_bot():
    dp.include_routers(
        load_routers()
    )

    tries = 0
    await message_start_session()
    try:
        await dp.start_polling(bot)
        tries = 0
    except TelegramNetworkError:
        tries += 1
        logger.info(f"Check your internet connection. Tries {tries}")
        await asyncio.sleep(tries)
