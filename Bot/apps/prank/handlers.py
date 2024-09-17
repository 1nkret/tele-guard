from aiogram import types, Router
from aiogram.filters import Command

from Bot.core.config import bot, owner_url
from Bot.utils.chat.check_chat_id import check_chat_id
from Bot.utils.access.members import get_from_json_members, is_whitelisted, focus_mode_immunity
from Bot.utils.access.status import is_blocked

from Bot.utils.time.get_session_time import session_time
from Bot.apps.menu.keyboard import get_main_menu

from services.console_messanger import start_prank


router = Router()


@router.callback_query(lambda c: c.data == "prank")
@router.message(Command("prank"))
async def console_messanger_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if is_blocked():
        if not is_whitelisted(chat_id):
            await bot.send_message(
                chat_id=chat_id,
                text=f"🌙  <b>Focus Mode</b> is enabled. Please contact the <a href='{owner_url}'>administrator "
                     "for access</a>.",
                parse_mode="HTML"
            )
            return

    if chat_id in get_from_json_members():
        if is_message:
            await bot.delete_message(
                chat_id=chat_id,
                message_id=event.message_id
            )
            await start_prank()

            await bot.send_message(
                chat_id=chat_id,
                text=f"LOL! Prank is started. {focus_mode_immunity(chat_id)}{session_time()}",
                reply_markup=get_main_menu(chat_id)
            )
        else:
            await start_prank()

            await event.message.edit_text(
                text=f"LOL! Prank is started. {focus_mode_immunity(chat_id)}{session_time()}",
                reply_markup=get_main_menu(chat_id)
            )
