import os

from aiogram import types, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from Bot.config import allowed_chat_ids, bot
from Bot.forms.PhotoUpload import PhotoUploadStates
from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.open_image_fullscreen import open_image_fullscreen
from Bot.inline_keyboards.upload_cancel import upload_cancel_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "upload_photo")
@router.message(Command("uploadphoto"))
async def upload_photo_to_monitor(event: types.CallbackQuery or types.Message, state: FSMContext):
    chat_id = check_chat_id(event)

    if chat_id in allowed_chat_ids:
        await state.set_state(PhotoUploadStates.waiting_for_photo)
        await bot.send_message(
            chat_id=chat_id,
            text="Send your image (required 1920x1080 or 2K)",
            reply_markup=upload_cancel_keyboard()
        )


@router.message(PhotoUploadStates.waiting_for_photo)
async def handle_photo_upload(message: types.Message, state: FSMContext):
    chat_id = check_chat_id(message)
    if message.photo:
        photo_id = message.photo[-1].file_id
        file = await bot.get_file(file_id=photo_id)
        file_path = file.file_path

        save_dir = f'media/upload_photos/'+chat_id
        os.makedirs(
            name=save_dir,
            exist_ok=True
        )
        local_path = os.path.join(save_dir, f'{photo_id}.jpg')

        await bot.download_file(
            file_path=file_path,
            destination=local_path
        )

        await bot.send_message(chat_id, "Successful.")
        await state.clear()

        await open_image_fullscreen(image_path=local_path)
    else:
        await bot.send_message(
            chat_id=chat_id,
            text="This is not photo. Send your image (required 1920x1080 or 2K)",
            reply_markup=upload_cancel_keyboard())
        await state.set_state(PhotoUploadStates.waiting_for_photo)


@router.callback_query(StateFilter(PhotoUploadStates.waiting_for_photo), lambda c: c.data == "upload_cancel")
async def cancel_upload_photo(query: types.CallbackQuery, state: FSMContext):
    chat_id = query.message.chat.id

    if str(chat_id) in allowed_chat_ids:
        await state.clear()
        await bot.send_message(
            chat_id=chat_id,
            text="Canceled."
        )
        await query.answer()
