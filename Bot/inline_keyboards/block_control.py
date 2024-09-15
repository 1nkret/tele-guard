from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bot.helpers.access import read_json


def menu_block_control():
    settings = read_json("settings.json")["blockerator_cursor"]
    buttons = [
        [
            InlineKeyboardButton(
                text="🖱️ Unblock Cursor" if settings else "🖱️ Block Cursor",
                callback_data="unblock_cursor" if settings else "block_cursor"
            ),
            InlineKeyboardButton(
                text="🗑️ Close all windows",
                callback_data="close_windows"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="admin_options"
            )
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
