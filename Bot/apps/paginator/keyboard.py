from aiogram import types


def paginate_buttons(
        buttons: list,
        page: int,
        buttons_per_page: int = 4,
        back_callback_data: str = "back_to_menu",
        add_button: dict = None
):
    start_index = (page - 1) * buttons_per_page
    end_index = start_index + buttons_per_page
    page_buttons = buttons[start_index:end_index]

    inline_buttons = []

    for row in page_buttons:
        inline_buttons.append([
            types.InlineKeyboardButton(text=btn['text'], callback_data=btn['callback_data'])
            for btn in row
        ])

    if add_button:
        inline_buttons.append([
            types.InlineKeyboardButton(
                text=add_button['text'], callback_data=add_button['callback_data']
            )
        ])

    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data=f"prev_page_{page - 1}")
        )
    navigation_buttons.append(
        types.InlineKeyboardButton(
            text="Back",
            callback_data=back_callback_data
        )
    )
    if end_index < len(buttons):
        navigation_buttons.append(
            types.InlineKeyboardButton(
                text="➡️",
                callback_data=f"next_page_{page + 1}"
            )
        )

    if navigation_buttons:
        inline_buttons.append(navigation_buttons)

    return types.InlineKeyboardMarkup(inline_keyboard=inline_buttons)
