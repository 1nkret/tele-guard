from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Bot.config import allowed_chat_ids, bot
from Bot.forms.ErrorForm import ErrorForm
from Bot.helpers.check_chat_id import check_chat_id


router = Router()


@router.callback_query(lambda c: c.data == "error")
@router.message(Command("error"))
async def error_command(event: types.Message or types.CallbackQuery, state: FSMContext):
    chat_id = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        await state.set_state(ErrorForm.title)
        await bot.send_message(
            chat_id=chat_id,
            text="Tittle:"
        )


@router.message(ErrorForm.title)
async def state_error_form_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)

    await state.set_state(ErrorForm.message)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Message:"
    )


@router.message(ErrorForm.message)
async def state_error_successful(message: types.Message, state: FSMContext):
    from services.console_messanger import show_error

    await state.update_data(message=message.text)

    data = await state.get_data()
    show_error(
        title=data["title"],
        message=data["message"]
    )

    await state.clear()
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Successful."
    )
