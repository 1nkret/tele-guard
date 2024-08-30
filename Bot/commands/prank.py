from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import bot
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.access import get_json_members
from Bot.helpers.get_session_time import session_time
from Bot.inline_keyboards.menu import get_main_menu

from services.console_messanger import start_prank


router = Router()


@router.callback_query(lambda c: c.data == "prank")
@router.message(Command("prank"))
async def console_messanger_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_json_members():
        if is_message:
            await bot.delete_message(
                chat_id=chat_id,
                message_id=event.message_id
            )
            await start_prank()

            await bot.send_message(
                chat_id=chat_id,
                text=f"LOL! Prank is started. {session_time()}",
                reply_markup=get_main_menu(chat_id)
            )
        else:
            await start_prank()

            await event.message.edit_text(
                text=f"LOL! Prank is started. {session_time()}",
                reply_markup=get_main_menu(chat_id)
            )
