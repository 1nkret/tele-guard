from aiogram import types, Router
from aiogram.filters import Command

from Bot.core.config import bot, owner_url

from Bot.utils.system.webcam import webcam
from Bot.utils.chat.check_chat_id import check_chat_id
from Bot.utils.system.open_image_fullscreen import open_image_fullscreen
from Bot.utils.time.get_session_time import session_time
from Bot.utils.access.members import get_from_json_owners, is_whitelisted, focus_mode_immunity
from Bot.utils.access.status import is_blocked

from Bot.apps.menu.keyboard import get_main_menu
from Bot.apps.takephoto.keyboard import upload_to_monitor

router = Router()


@router.callback_query(lambda c: c.data == "take_photo")
@router.message(Command("take_photo"))
async def take_photo_command(event: types.Message or types.CallbackQuery):
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
        msg = await bot.send_message(
            chat_id=chat_id,
            text="Uploading photo..."
        )
        await open_image_fullscreen(
            image_path=query.data[len("upload_photo_"):],
            title="BOO"
        )
        msg.edit_text(
            text=f"Successful. {focus_mode_immunity(chat_id)}{session_time()}",
            reply_markup=get_main_menu(chat_id)
        )
