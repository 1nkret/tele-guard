from aiogram import types, Router
from aiogram.filters import Command


from Bot.config import bot, owner_url

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.get_session_time import session_time
from Bot.helpers.access import get_from_json_owners, is_blocked, is_whitelisted, focus_mode_immunity
from Bot.helpers.blockerator_cursor import blocker_cursor, change_status_blocker, check_blocker_cursor
from Bot.helpers.close_windows import close_all_windows

from Bot.inline_keyboards.block_control import menu_block_control

from Bot.forms.ErrorForm import ErrorForm

from services.console_messanger import spam_on_start
from services.notify import notify_windows

router = Router()


@router.callback_query(lambda c: c.data == "block_control")
@router.message(Command("block_control"))
async def block_control_menu_handler(event: types.Message or types.CallbackQuery):
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
                text="Choose action",
                reply_markup=menu_block_control()
            )
        else:
            await event.message.edit_text(
                text="Choose action",
                reply_markup=menu_block_control()
            )


@router.callback_query(lambda c: c.data == "block_cursor")
async def block_cursor_handler(event: types.CallbackQuery):
    await change_status_blocker(True)
    await event.message.edit_text(
        text="Cursor is blocked",
        reply_markup=menu_block_control()
    )
    await blocker_cursor()


@router.callback_query(lambda c: c.data == "unblock_cursor")
async def unblock_cursor_handler(event: types.CallbackQuery):
    await change_status_blocker(False)
    await event.message.edit_text(
        text="Cursor is unblocked",
        reply_markup=menu_block_control()
    )


@router.callback_query(lambda c: c.data == "close_windows")
async def close_all_windows_handler(event: types.CallbackQuery):
    await event.message.edit_text(
        text="Wait...",
    )
    await notify_windows(title="Administrator", message="HAHAHAHAHAHAHHA 😈😈😈")
    await close_all_windows()
    await notify_windows(title="Administrator", message="Get out from computer.")
    await event.message.edit_text(
        text="Windows are closed.",
        reply_markup=menu_block_control()
    )
