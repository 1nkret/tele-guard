import asyncio

from Bot.config import bot
from Bot.inline_keyboards.menu import inline_keyboard_menu
from Bot.helpers.access import get_json_members


async def message_start_session() -> None:
    """
    Function is send message to allowed users on start session.
    :return: None
    """
    for aci in get_json_members():
        await bot.send_message(
            chat_id=aci,
            text="Session is started.",
            reply_markup=inline_keyboard_menu(aci)
        )
        await asyncio.sleep(0.1)
