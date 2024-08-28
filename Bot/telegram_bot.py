import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import dp, bot
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
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
