from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def error_cancel_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Cancel",
                                     callback_data="error_cancel")
            ]
        ]
    )
