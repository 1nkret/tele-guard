from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Bot.core.config import bot, owner_url

from Bot.utils.chat.check_chat_id import check_chat_id
from Bot.utils.time.get_session_time import session_time
from Bot.utils.access.members import get_from_json_owners, is_whitelisted, focus_mode_immunity
from Bot.utils.access.status import is_blocked

from Bot.apps.error.keyboard import error_cancel_keyboard
from Bot.apps.menu.keyboard import get_main_menu

from Bot.apps.error.forms import ErrorForm


router = Router()


@router.callback_query(lambda c: c.data == "error")
@router.message(Command("error"))
async def error_command(event: types.Message or types.CallbackQuery, state: FSMContext):
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
    if chat_id in get_from_json_owners():
        if is_message:
            await state.set_state(ErrorForm.title)
            await bot.send_message(
                chat_id=chat_id,
                text="Tittle:",
                reply_markup=error_cancel_keyboard()
            )
        else:
            await state.set_state(ErrorForm.title)
            await event.message.edit_text(
                text="Title:",
                reply_markup=error_cancel_keyboard()
            )


@router.message(ErrorForm.title)
async def state_error_form_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(ErrorForm.message)

    await message.answer(
        text=f"Now type message_echo:",
        reply_markup=error_cancel_keyboard()
    )


@router.message(ErrorForm.message)
async def state_error_successful(message: types.Message, state: FSMContext):
    from services.console_messanger import show_error

    await state.update_data(message=message.text)

    data = await state.get_data()
    chat_id = str(message.chat.id)

    await message.answer(
        text=f"Successful. {focus_mode_immunity(chat_id)}{session_time()}",
        reply_markup=get_main_menu(chat_id)
    )
    await state.clear()

    await show_error(
        title=data["title"],
        message=data["message_echo"]
    )


@router.callback_query(lambda c: c.data == "error_cancel")
async def error_cancel(query: types.CallbackQuery, state: FSMContext):
    chat_id = str(query.message.chat.id)
    current_state = await state.get_state()

    if str(chat_id) in get_from_json_owners() and current_state:
        await state.clear()
        await query.message.answer(
            text=f"Canceled. {focus_mode_immunity(chat_id)}{session_time()}",
            reply_markup=get_main_menu(chat_id)
        )
    elif not current_state:
        await query.message.delete()

