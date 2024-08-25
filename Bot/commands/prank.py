from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import allowed_chat_ids, bot
from Bot.helpers.check_chat_id import check_chat_id
from services.console_messanger import start_prank

router = Router()


@router.callback_query(lambda c: c.data == "prank")
@router.message(Command("prank"))
async def console_messanger_command(event: types.Message or types.CallbackQuery):
    chat_id = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        await start_prank()

        await bot.send_message(
            chat_id=chat_id,
            text=f"{event.from_user.first_name}: Prank is started."
        )
