import asyncio

from Bot.config import bot
from Bot.helpers.access import get_json_members


async def send_message(text: str) -> None:
    """
    This function sends out to allowed users your message.
    :param text: message
    :return: None
    """
    for aci in get_json_members():
        await bot.send_message(aci, text)
        await asyncio.sleep(0.1)
