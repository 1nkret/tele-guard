from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def back_to_menu():
    button = [
        [
            InlineKeyboardButton(text="Back", callback_data="back_to_menu")
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=button)
