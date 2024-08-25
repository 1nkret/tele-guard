from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import allowed_chat_ids
from Bot.helpers.send_message import send_message
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.shutdown_os import shutdown_os

router = Router()


@router.callback_query(lambda c: c.data == "shutdown")
@router.message(Command("shutdown"))
async def handle_shutdown_command(event: types.Message or types.CallbackQuery):
    chat_id = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        shutdown_os()

        await send_message(f"{event.from_user.first_name}: Your PC is turning off.")
