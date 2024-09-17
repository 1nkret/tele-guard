import asyncio

from aiogram.exceptions import TelegramNetworkError
from Bot.core.config import dp, bot, logger
from Bot.utils.loader.router_loader import load_routers


async def start_bot():
    dp.include_routers(
        load_routers()
    )

    tries = 0
    try:
        await dp.start_polling(bot)
        tries = 0
    except TelegramNetworkError:
        tries += 1
        logger.info(f"Check your internet connection. Tries {tries}")
        await asyncio.sleep(tries)
