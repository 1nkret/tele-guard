import logging

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bot.utils.access.json import read_json, write_json


def menu_block_control():
    try:
        settings = read_json("settings.json")["blockerator_cursor"]
    except KeyError:
        settings = False
        write_json({"blockerator_cursor": False}, "settings.json")
        logging.error("key blockerator_cursor not found in settings.json ")

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
