import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aiogram.exceptions import TelegramNetworkError
from config import dp, bot, logger
from commands import *


async def main():
    dp.include_routers(
        shutdown_router,
        error_router,
        prank_router,
        takephoto_router,
        uploadphoto_router,
        menu_router,
        settings_router
    )
    tries = 0
    try:
        await dp.start_polling(bot)
        tries = 0
    except TelegramNetworkError:
        tries += 1
        logger.info(f"Check your internet connection. Tries {tries}")
        await asyncio.sleep(tries)


if __name__ == '__main__':
    asyncio.run(main())
