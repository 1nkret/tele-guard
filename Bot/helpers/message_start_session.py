import asyncio

from aiogram import types

from Bot.config import allowed_chat_ids, bot


async def message_start_session() -> None:
    """
    Function is send message to allowed users on start session.
    :return: None
    """
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Shutdown",
                callback_data="shutdown"),
            types.InlineKeyboardButton(
                text="Prank",
                callback_data="prank")
        ],
        [
            types.InlineKeyboardButton(
                text="Tape photo",
                callback_data="take_photo")
        ],
        [
            types.InlineKeyboardButton(
                text="Upload photo",
                callback_data="upload_photo")
        ]
    ]
    builder = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    for aci in allowed_chat_ids:
        await bot.send_message(
            chat_id=aci,
            text="Session is started.",
            reply_markup=builder
        )
        await asyncio.sleep(0.1)
