from aiogram import Router, types
from aiogram.filters import Command

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.access import get_from_json_owners

router = Router()


@router.message(Command("storage"))
@router.callback_query(lambda c: c.data == "storage")
async def storage(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_owners():
        text = "Storage"

        if is_message:
            await event.answer(
                text=text,
                reply_markup=...
            )
        else:
            await event.message.edit_text(
                text=text,
                reply_markup=...
            )
