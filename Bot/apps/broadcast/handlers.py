from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from Bot.apps.broadcast.forms import Broadcast
from Bot.apps.broadcast.keyboards import broadcast_cancel
from Bot.apps.menu.keyboard import get_main_menu

from Bot.core.config import bot
from Bot.utils.access.members import get_from_json_members

router = Router()


@router.message(Command("broadcast"))
async def broadcast_handler(event: Message, state: FSMContext):
    if str(event.chat.id) in get_from_json_members():
        await event.answer(
            text="Type your message_echo to alert all:",
            reply_markup=broadcast_cancel()
        )
        await state.set_state(Broadcast.message)


@router.message(Broadcast.message)
async def broadcast_end_handler(event: Message, state: FSMContext):
    await event.answer("Successful.", reply_markup=get_main_menu(str(event.chat.id)))
    await state.clear()
    for aci in get_from_json_members():
        await bot.send_message(
            chat_id=aci,
            text=event.text
        )


@router.callback_query(lambda c: c.data == "broadcast_cancel")
async def broadcast_cancel_handler(event: CallbackQuery, state: FSMContext):
    await state.clear()
    await event.message.answer(
        text="Canceled.",
        reply_markup=get_main_menu(str(event.message.chat.id))
    )
