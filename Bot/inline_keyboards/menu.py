from aiogram import types
from Bot.helpers.access import get_from_json_owners


def get_main_menu(chat_id: str):
    buttons = [
        [
            types.InlineKeyboardButton(text="Main Functions", callback_data="main_functions"),
            types.InlineKeyboardButton(text="Photo Options", callback_data="photo_options")
        ]
    ]
    if chat_id in get_from_json_owners():
        buttons.append([types.InlineKeyboardButton(text="Admin Options", callback_data="admin_options")])

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_functions_page(page: int = 1):
    functions = [
        [
            {"text": "Shutdown", "callback_data": "shutdown"},
            {"text": "Prank", "callback_data": "prank"},
        ]
    ]
    return paginate_buttons(functions, page)


def get_photo_options_page(
        chat_id: str,
        page: int = 1
):
    functions = [
        [
            {"text": "Upload photo", "callback_data": "upload_photo"}
        ]
    ]
    if chat_id in get_from_json_owners():
        functions[0].append(
            {"text": "Tape photo", "callback_data": "take_photo"}
        )
    return paginate_buttons(functions, page)


def get_admin_options_page(page: int = 1):
    functions = [
        [
            {"text": "Settings", "callback_data": "settings"},
        ]
    ]
    return paginate_buttons(functions, page)


def paginate_buttons(buttons, page, buttons_per_page=4):
    start_index = (page - 1) * buttons_per_page
    end_index = start_index + buttons_per_page
    page_buttons = buttons[start_index:end_index]

    inline_buttons = []

    for row in page_buttons:
        inline_buttons.append([
            types.InlineKeyboardButton(text=btn['text'], callback_data=btn['callback_data'])
            for btn in row
        ])

    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(
            types.InlineKeyboardButton(
                text="Previous",
                callback_data=f"prev_page_{page - 1}")
        )
    navigation_buttons.append(
        types.InlineKeyboardButton(
            text="Menu",
            callback_data="back_to_menu"
        )
    )
    if end_index < len(buttons):
        navigation_buttons.append(
            types.InlineKeyboardButton(
                text="Next",
                callback_data=f"next_page_{page + 1}"
            )
        )

    if navigation_buttons:
        inline_buttons.append(navigation_buttons)

    return types.InlineKeyboardMarkup(inline_keyboard=inline_buttons)
