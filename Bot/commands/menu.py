from aiogram import types, Router
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from typing import Union

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.get_session_time import session_time
from Bot.helpers.access import get_from_json_members

from Bot.inline_keyboards.menu import (
    get_main_menu,
    get_main_functions_page,
    get_photo_options_page,
    get_admin_options_page
)

router = Router()


@router.callback_query(lambda c: c.data == "menu")
@router.message(Command("menu"))
async def handle_menu(event: Union[types.CallbackQuery, types.Message]):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_members():
        text = f"Main menu. {session_time()}"

        if is_message:
            await event.answer(
                text=text,
                reply_markup=get_main_menu(chat_id)
            )
        else:
            await event.message.answer(
                text=text,
                reply_markup=get_main_menu(chat_id)
            )


@router.callback_query(lambda c: c.data == "back_to_menu")
async def handle_back_to_menu(event: Union[types.CallbackQuery, types.Message]):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_members():
        text = f"Main menu. {session_time()}"

        try:
            await event.message.edit_text(
                text=text,
                reply_markup=get_main_menu(chat_id)
            )
        except TelegramBadRequest:
            await event.message.answer(
                text=text,
                reply_markup=get_main_menu(chat_id)
            )


@router.callback_query(lambda c: c.data in ["main_functions", "photo_options", "admin_options"] or c.data.startswith(
    ("prev_page_", "next_page_")))
async def handle_callback(event: types.CallbackQuery):
    data = event.data
    chat_id = str(event.message.chat.id)

    if data == "main_functions":
        await event.message.edit_text(
            text="Main Functions"+session_time(),
            reply_markup=get_main_functions_page()
        )
    elif data == "photo_options":
        await event.message.edit_text(
            text="Photo Options"+session_time(),
            reply_markup=get_photo_options_page(chat_id)
        )
    elif data == "admin_options":
        await event.message.edit_text(
            text="Admin Options"+session_time(),
            reply_markup=get_admin_options_page()
        )
    elif data.startswith("prev_page_") or data.startswith("next_page_"):
        _, page = data.rsplit("_", 1)
        current_menu = event.message.text.lower().replace(" ", "_")
        if current_menu == "main_functions":
            await event.message.edit_reply_markup(reply_markup=get_main_functions_page(int(page)))
        elif current_menu == "photo_options":
            await event.message.edit_reply_markup(reply_markup=get_photo_options_page(chat_id, int(page)))
        elif current_menu == "admin_options":
            await event.message.edit_reply_markup(reply_markup=get_admin_options_page(int(page)))
