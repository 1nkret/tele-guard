import random
import threading
import asyncio

from datetime import datetime
from services.config import load_config, save_config


async def update_session_time(config):
    while True:
        new_time = datetime.now()
        config["session_time_update"] = new_time
        save_config(config)
        await asyncio.sleep(random.randint(5, 20))


async def start_session_time_updater():
    config = load_config()
    threading.Thread(target=update_session_time, args=(config,), daemon=True).start()
