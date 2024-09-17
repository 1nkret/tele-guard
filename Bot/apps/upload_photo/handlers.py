import os

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Bot.core.config import bot, owner_url
from Bot.apps.upload_photo.forms import PhotoUploadStates

from Bot.utils.chat.check_chat_id import check_chat_id
from Bot.utils.system.open_image_fullscreen import open_image_fullscreen
from Bot.utils.time.get_session_time import session_time
from Bot.utils.access.members import get_from_json_members, is_whitelisted, focus_mode_immunity
from Bot.utils.access.status import is_blocked

from Bot.apps.upload_photo.keyboard import upload_cancel_keyboard
from Bot.apps.menu.keyboard import get_main_menu


router = Router()


@router.callback_query(lambda c: c.data == "upload_photo")
@router.message(Command("uploadphoto"))
async def upload_photo_to_monitor(event: types.CallbackQuery or types.Message, state: FSMContext):
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

    if chat_id in get_from_json_members():
        if is_message:
            await state.set_state(PhotoUploadStates.waiting_for_photo)
            await event.message.answer(
                text="Send your image (required 1920x1080 or 2K)",
                reply_markup=upload_cancel_keyboard()
            )
        else:
            await state.set_state(PhotoUploadStates.waiting_for_photo)
            await event.message.edit_text(
                text="Send your image (required 1920x1080 or 2K)",
                reply_markup=upload_cancel_keyboard()
            )


@router.message(PhotoUploadStates.waiting_for_photo)
async def handle_photo_upload(message: types.Message, state: FSMContext):
    chat_id, is_message = check_chat_id(message)

    if message.photo:
        photo_id = message.photo[-1].file_id
    elif message.document:
        if not message.document.mime_type.startswith('image/'):
            await message.answer(
                text="This is not image. Try again.",
                reply_markup=upload_cancel_keyboard())
            return
        elif message.document.file_name.lower().endswith(".heic"):
            await message.answer(
                text="This format is not supported. Convert to JPG or PNG. ",
                reply_markup=upload_cancel_keyboard())
            return
        photo_id = message.document.file_id
    else:
        await message.answer(
            text="This is not photo. Send your image (required 1920x1080 or 2K)",
            reply_markup=upload_cancel_keyboard())
        return

    file = await bot.get_file(file_id=photo_id)
    file_path = file.file_path

    save_dir = f'media/upload_photos/{chat_id}'
    os.makedirs(save_dir, exist_ok=True)
    local_path = os.path.join(save_dir, f'{photo_id}.jpg')

    await bot.download_file(file_path=file_path, destination=local_path)

    await message.answer(
        text=f"Successful. {focus_mode_immunity(chat_id)}{session_time()}",
        reply_markup=get_main_menu(chat_id))
    await state.clear()

    await open_image_fullscreen(
        image_path=local_path,
        title=message.from_user.first_name
    )


@router.callback_query(lambda c: c.data == "upload_cancel")
async def cancel_upload_photo(query: types.CallbackQuery, state: FSMContext):
    chat_id = str(query.message.chat.id)
    current_state = await state.get_state()

    if chat_id in get_from_json_members() and current_state:
        await state.clear()
        await query.message.answer(
            text=f"Canceled. {focus_mode_immunity(chat_id)}{session_time()}",
            reply_markup=get_main_menu(chat_id)
        )
    elif not current_state:
        await query.message.delete()
