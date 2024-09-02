from aiogram import types, Router
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from typing import Union

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.get_session_time import session_time
from Bot.helpers.access import get_from_json_members, focus_mode_immunity

from Bot.inline_keyboards.menu import (
    get_main_menu
)

router = Router()


@router.callback_query(lambda c: c.data == "menu")
@router.message(Command("menu"))
async def handle_menu(event: Union[types.CallbackQuery, types.Message]):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_members():
        text = f"Main menu  {focus_mode_immunity(chat_id)}{session_time()}"

        if is_message:
            await event.answer(
                text=text,
                reply_markup=get_main_menu(chat_id),
                parse_mode="HTML"
            )
        else:
            await event.message.answer(
                text=text,
                reply_markup=get_main_menu(chat_id),
                parse_mode="HTML"
            )


@router.callback_query(lambda c: c.data == "back_to_menu")
async def handle_back_to_menu(event: Union[types.CallbackQuery, types.Message]):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_members():
        text = f"Main menu  {focus_mode_immunity(chat_id)}{session_time()}"

        try:
            await event.message.edit_text(
                text=text,
                reply_markup=get_main_menu(chat_id),
                parse_mode="HTML"
            )
        except TelegramBadRequest:
            await event.message.answer(
                text=text,
                reply_markup=get_main_menu(chat_id),
                parse_mode="HTML"
            )


