import asyncio

from datetime import datetime
from random import randint

from services.config import load_config, load_logging, logger, save_config
from services.telegram_utils import is_telegram_open, close_telegram
from services.notify import notify_windows
from services.sequence_checker import check_sequence
from services.console_messanger import start_prank, close_cmd
from services.update_time import update_time

from Bot.helpers.message_start_session import message_start_session


async def start():
    logger.info("Loading guard...")
    config = load_config()
    load_logging("blocker")

    config["locked"], config["session_time"] = True, datetime.now()
    save_config(config)
    await message_start_session()

    logger.info("Successful.")
    while True:
        status = is_telegram_open()

        if status and config["locked"]:
            logger.info("Telegram запущен, ожидание комбинации...")
            await start_prank()

            if not await check_sequence(['esc', 'esc', 'esc'], False, config):
                logger.info("Комбинация не введена, закрытие Telegram.")
                close_telegram(config)
                await notify_windows(
                    config,
                    title="Сышиш",
                    message="Можеш даже не пытаться 😡",
                )
            close_cmd()
        elif not status:
            await asyncio.sleep(9)  # sleep mode
        else:
            if await check_sequence(['f10', 'f10', 'f10'], True, config):
                close_telegram(config)

        if randint(1, 10) == 5:
            await update_time(config)
        await asyncio.sleep(1)
