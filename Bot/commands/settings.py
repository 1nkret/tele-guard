from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import owner, bot
from Bot.helpers.check_chat_id import check_chat_id
from services.console_messanger import start_prank

router = Router()


@router.callback_query(lambda c: c.data == "settings")
@router.message(Command("settings"))
async def settings_command(event: types.Message or types.CallbackQuery):
    chat_id = check_chat_id(event)

    if chat_id in owner:
        ...
