import asyncio
import sys
import os
from core.main import start_bot
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


async def main():
    asyncio.run(await start_bot())


if __name__ == '__main__':
    asyncio.run(main())
