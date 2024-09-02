from aiogram import types, Router

from Bot.helpers.get_session_time import session_time
from Bot.inline_keyboards.menu import get_main_functions_page, get_photo_options_page, get_admin_options_page
from Bot.inline_keyboards.settings import settings_access_menu

router = Router()


@router.callback_query(lambda c: c.data in ["main_functions", "photo_options", "admin_options"] or c.data.startswith(
    ("prev_page_", "next_page_")))
async def paginator_handle_callback(event: types.CallbackQuery):
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
        if current_menu.startswith("main_functions"):
            await event.message.edit_reply_markup(reply_markup=get_main_functions_page(int(page)))
        elif current_menu.startswith("photo_options"):
            await event.message.edit_reply_markup(reply_markup=get_photo_options_page(chat_id, int(page)))
        elif current_menu.startswith("admin_options"):
            await event.message.edit_reply_markup(reply_markup=get_admin_options_page(int(page)))
        elif current_menu.startswith("access_manager"):
            await event.message.edit_reply_markup(reply_markup=settings_access_menu(int(page)))
