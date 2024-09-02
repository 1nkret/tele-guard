from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import bot, owner_url
from Bot.helpers.access import get_from_json_members, is_whitelisted, is_blocked
from Bot.helpers.send_message import send_message
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.shutdown_os import shutdown_os

router = Router()


@router.callback_query(lambda c: c.data == "shutdown")
@router.message(Command("shutdown"))
async def handle_shutdown_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if is_blocked:
        if not is_whitelisted(chat_id):
            await bot.send_message(
                chat_id=chat_id,
                text=f"🌙  <b>Focus Mode</b> is enabled. Please contact the <a href='{owner_url}'>administrator "
                     "for access</a>.",
                parse_mode="HTML"
            )
            return

    if chat_id in get_from_json_members():
        shutdown_os()

        await send_message(f"{event.from_user.first_name}: Your PC is turning off.")
