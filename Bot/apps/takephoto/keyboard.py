from aiogram import types


def upload_to_monitor(file_path: str) -> types.InlineKeyboardMarkup:
    buttons = [
                [
                    types.InlineKeyboardButton(
                        text="🖥 UPLOAD TO MONITOR 🖥",
                        callback_data="upload_photo_" + file_path
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        text="🏠 Home 🏠",
                        callback_data="menu"
                    )
                ]
            ]

    return types.InlineKeyboardMarkup(
            inline_keyboard=buttons
        )
