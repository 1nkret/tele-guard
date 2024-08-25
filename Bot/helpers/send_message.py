import asyncio

from Bot.config import allowed_chat_ids, bot


async def send_message(text: str) -> None:
    """
    This function sends out to allowed users your message.
    :param text: message
    :return: None
    """
    for aci in allowed_chat_ids:
        await bot.send_message(aci, text)
        await asyncio.sleep(0.1)
