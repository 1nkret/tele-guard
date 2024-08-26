from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import allowed_chat_ids

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.get_session_time import session_time

from Bot.inline_keyboards.menu import inline_keyboard_menu


router = Router()


@router.callback_query(lambda c: c.data == "menu")
@router.message(Command("menu"))
async def upload_photo_to_monitor(event: types.CallbackQuery or types.Message):
    chat_id, is_message = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        if is_message:
            await event.answer(
                text=f"Main menu.{session_time()}",
                reply_markup=inline_keyboard_menu(chat_id)
            )
        else:
            await event.message.answer(
                text=f"Main menu.{session_time()}",
                reply_markup=inline_keyboard_menu(chat_id)
            )
