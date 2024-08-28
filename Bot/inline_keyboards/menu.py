from aiogram import types

from Bot.helpers.access import get_json_owners


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

    if chat_id in get_json_owners():
        buttons.append(
            [
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
        buttons.append(
            [
                types.InlineKeyboardButton(
                    text="Settings",
                    callback_data="settings"
                )
            ]
        )

    builder = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )

    return builder
