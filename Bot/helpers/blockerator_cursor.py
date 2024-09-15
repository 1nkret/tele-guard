import json
import pyautogui
import asyncio

from random import randint
from concurrent.futures import ThreadPoolExecutor
from Bot.helpers.access import read_json

executor = ThreadPoolExecutor()
screen_width, screen_height = pyautogui.size()


async def move_cursor_async(x, y):
    loop = asyncio.get_event_loop()
    try:
        await loop.run_in_executor(executor, pyautogui.moveTo, x, y)
    except Exception as e:
        pass


async def lock_cursor():
    try:
        while True:
            await move_cursor_async(randint(1, screen_width - 1), randint(1, screen_height - 1))
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        pass


async def check_blocker_cursor() -> bool:
    return read_json("settings.json")["blockerator_cursor"]


async def change_status_blocker(status: bool):
    settings = read_json("settings.json")

    settings["blockerator_cursor"] = status
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)


async def blocker_cursor():
    task = asyncio.create_task(lock_cursor())

    try:
        while True:
            if await check_blocker_cursor():
                await asyncio.sleep(5)
            else:
                break
    except Exception:
        pass
    finally:
        task.cancel()
        await task
        await change_status_blocker(False)
