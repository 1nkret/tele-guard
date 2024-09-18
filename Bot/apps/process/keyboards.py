from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bot.utils.system.process import get_process_iter
from Bot.apps.paginator.keyboard import paginate_buttons


def process_manager_menu(page: int = 1):
    cache = get_process_iter()
    process = []
    for el in cache:
        process.append(
            {"text": f"{el['name']} {el['cpu']}%, {el['memory']:.2f}%", "callback_data": f"process_manage_{el['pid']}"}
        )

    buttons = [process[i:i + 1] for i in range(0, len(process), 1)]

    other_button = {"text": "UPDATE PAGE", "callback_data": f"process_manager_update_{page}"}

    return paginate_buttons(
        buttons=buttons,
        back_callback_data="admin_options",
        page=page,
        add_button=other_button,
        buttons_per_page=10,
    )


def process_manager_pid_profile(
        pid,
        name
):
    buttons = [
        [
            InlineKeyboardButton(
                text="❌ Kill ❌",
                callback_data=f"process_manager_kill_{pid}"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="process_manager"
            )
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
