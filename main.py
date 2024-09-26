import asyncio

from services.start import start
from Bot.telegram_bot import start_bot


async def main():
    bot_task = asyncio.create_task(start_bot())
    blocker_task = asyncio.create_task(start())

    await bot_task
    await blocker_task

if __name__ == "__main__":
    asyncio.run(main())
