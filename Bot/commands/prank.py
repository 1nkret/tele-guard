from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import allowed_chat_ids, bot
from Bot.helpers.check_chat_id import check_chat_id
from Bot.inline_keyboards.menu import inline_keyboard_menu
from services.console_messanger import start_prank
from Bot.helpers.get_session_time import session_time


router = Router()


@router.callback_query(lambda c: c.data == "prank")
@router.message(Command("prank"))
async def console_messanger_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        if is_message:
            await bot.delete_message(
                chat_id=chat_id,
                message_id=event.message_id
            )
            await start_prank()

            await bot.send_message(
                chat_id=chat_id,
                text=f"LOL! Prank is started. {session_time()}",
                reply_markup=inline_keyboard_menu(chat_id)
            )
        else:
            await start_prank()

            await event.message.edit_text(
                text=f"LOL! Prank is started. {session_time()}",
                reply_markup=inline_keyboard_menu(chat_id)
            )
