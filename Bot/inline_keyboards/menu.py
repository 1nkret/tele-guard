from aiogram import types

from Bot.config import owner


def inline_keyboard_menu(chat_id: str):
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Shutdown",
                callback_data="shutdown"
            ),
            types.InlineKeyboardButton(
                text="Prank",
                callback_data="prank"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Upload photo",
                callback_data="upload_photo"
            )
        ]
    ]

    if chat_id in owner:
        buttons.insert(1, [
            types.InlineKeyboardButton(
                text="Tape photo",
                callback_data="take_photo"
            ),
            types.InlineKeyboardButton(
                text="Error",
                callback_data="error"
            )
        ]
                       )

    builder = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )

    return builder
