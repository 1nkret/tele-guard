import asyncio

from Bot.config import allowed_chat_ids, bot
from Bot.inline_keyboards.menu import inline_keyboard_menu


async def message_start_session() -> None:
    """
    Function is send message to allowed users on start session.
    :return: None
    """
    for aci in allowed_chat_ids:
        await bot.send_message(
            chat_id=aci,
            text="Session is started.",
            reply_markup=inline_keyboard_menu(aci)
        )
        await asyncio.sleep(0.1)
