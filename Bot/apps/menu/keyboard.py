from aiogram import types
from Bot.utils.access.members import get_from_json_owners
from Bot.apps.paginator.keyboard import paginate_buttons


def get_main_menu(chat_id: str):
    buttons = [
        [
            types.InlineKeyboardButton(text="Main", callback_data="main_functions"),
            types.InlineKeyboardButton(text="Photo", callback_data="photo_options")
        ]
    ]
    if chat_id in get_from_json_owners():
        buttons.append([types.InlineKeyboardButton(text="Admin Menu", callback_data="admin_options")])

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_functions_page(page: int = 1):
    functions = [
        [
            {"text": "💣 Shutdown", "callback_data": "shutdown"},
            {"text": "💿 Prank", "callback_data": "prank"},
        ]
    ]
    return paginate_buttons(functions, page)


def get_photo_options_page(
        chat_id: str,
        page: int = 1
):
    functions = [
        [
            {"text": "🖥 Upload photo", "callback_data": "upload_photo"}
        ],
        []
    ]
    if chat_id in get_from_json_owners():
        functions[0].append(
            {"text": "📸 Tape photo", "callback_data": "take_photo"}
        )
        functions[1].append(
            {"text": "Screenshot", "callback_data": "screenshot"}
        )
    return paginate_buttons(functions, page)


def get_admin_options_page(page: int = 1):
    functions = [
        [
            {"text": "⚙️ Settings", "callback_data": "settings"},
            {"text": "⛔️ Block Control", "callback_data": "block_control"},
        ],
        [
            {"text": "🛠️ Process Manager", "callback_data": "process_manager"},
            {"text": "Update", "callback_data": "update_project"},
        ]
    ]
    return paginate_buttons(functions, page)
