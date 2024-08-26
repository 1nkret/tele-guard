from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Bot.config import owner, bot
from Bot.forms.ErrorForm import ErrorForm

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.get_session_time import session_time
from Bot.helpers.edit_message_text import edit_message_text

from Bot.inline_keyboards.error_cancel import error_cancel_keyboard
from Bot.inline_keyboards.menu import inline_keyboard_menu


router = Router()


@router.callback_query(lambda c: c.data == "error")
@router.message(Command("error"))
async def error_command(event: types.Message or types.CallbackQuery, state: FSMContext):
    chat_id, is_message = check_chat_id(event)

    if chat_id in owner:
        if is_message:
            await state.set_state(ErrorForm.title)
            await bot.send_message(
                chat_id=chat_id,
                text="Tittle:",
                reply_markup=error_cancel_keyboard()
            )
        else:
            await state.set_state(ErrorForm.title)
            await edit_message_text(
                chat_id=chat_id,
                message_id=event.message.message_id,
                text="Title:",
                reply_markup=error_cancel_keyboard()
            )


@router.message(ErrorForm.title)
async def state_error_form_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(ErrorForm.message)

    await edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"Now type message:",
        reply_markup=error_cancel_keyboard()
    )
    await message.delete()


@router.message(ErrorForm.message)
async def state_error_successful(message: types.Message, state: FSMContext):
    from services.console_messanger import show_error

    await state.update_data(message=message.text)

    data = await state.get_data()
    chat_id = str(message.chat.id)

    await edit_message_text(
        message_id=message.message_id,
        chat_id=chat_id,
        text=f"Successful.{session_time()}",
        reply_markup=inline_keyboard_menu(chat_id)
    )
    await message.delete()
    await state.clear()

    await show_error(
        title=data["title"],
        message=data["message"]
    )


@router.callback_query(lambda c: c.data == "error_cancel")
async def error_cancel(query: types.CallbackQuery, state: FSMContext):
    chat_id = str(query.message.chat.id)
    current_state = await state.get_state()

    if str(chat_id) in owner and current_state:
        await state.clear()
        await edit_message_text(
            message_id=query.message.message_id,
            chat_id=chat_id,
            text=f"Canceled. {session_time()}",
            reply_markup=inline_keyboard_menu(chat_id)
        )
        await query.answer()
