import asyncio

from services.config import load_config, load_logging, save_config, logger
from services.telegram_utils import is_telegram_open, close_telegram
from services.notify import notify_windows
from services.sequence_checker import check_sequence
from services.console_messanger import start_prank, close_cmd
from services.load_env import load_env


async def start():
    if load_env() == "true":

        logger.info("Loading guard...")
        config = load_config()
        load_logging("blocker")

        config["locked"] = True
        save_config(config)

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
                        config=config,
                        title="Сышиш",
                        message="Можеш даже не пытаться 😡",
                    )
                close_cmd()
            elif not status:
                await asyncio.sleep(9)  # sleep mode
            else:
                if await check_sequence(['f10', 'f10', 'f10'], True, config):
                    close_telegram(config)

            await asyncio.sleep(1)
    else:
        logger.warning("Telegram blocker is not allowed.")
