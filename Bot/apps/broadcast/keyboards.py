from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def broadcast_cancel():
    buttons = [
        [
            InlineKeyboardButton(
                text="Cancel",
                callback_data="broadcast_cancel"
            )
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
