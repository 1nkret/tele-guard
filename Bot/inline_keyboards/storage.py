from aiogram import types


def storage_main_menu():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="back",
                callback_data="menu"
            )
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
