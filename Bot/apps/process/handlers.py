from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from Bot.apps.process.keyboards import process_manager_menu, process_manager_pid_profile
from Bot.utils.system.process import get_process, count_processes_by_name, kill_process_by_pid

router = Router()


@router.message(Command("process"))
async def process_manager_handler(event: types.Message):
    await event.answer(
        text="Process manager",
        reply_markup=process_manager_menu()
    )


@router.callback_query(lambda c: c.data == "process_manager")
async def process_manager_callback_handler(event: types.CallbackQuery):
    await event.message.edit_text(
        text="Process manager",
        reply_markup=process_manager_menu()
    )


@router.callback_query(lambda c: c.data.startswith("process_manage_"))
async def process_manager_pid_callback_handler(event: types.CallbackQuery):
    process_pid = event.data[len("process_manage_"):]
    about_pid = get_process(process_pid)
    process_count = count_processes_by_name(about_pid["name"])
    text = (f"<b>{about_pid['name']}</b>\n\n"
            f"CPU: {about_pid['cpu']}%\n"
            f"Memory: {about_pid['memory']:.2f}%\n"
            f"Process count: {process_count}")

    await event.message.edit_text(
        text=text,
        parse_mode="HTML",
        reply_markup=process_manager_pid_profile(
            pid=process_pid,
            name=about_pid['name']
        )
    )


@router.callback_query(lambda c: c.data.startswith("process_manager_kill_"))
async def process_manager_kill_process(event: types.CallbackQuery):
    pid = event.data[len("process_manager_kill_"):]
    text = kill_process_by_pid(pid)

    await event.message.edit_text(
        text=text,
        reply_markup=process_manager_menu()
    )


@router.callback_query(lambda c: c.data.startswith("process_manager_update_"))
async def process_manager_updater(event: types.CallbackQuery):
    page = event.data[len("process_manager_update_"):]

    try:
        await event.message.edit_reply_markup(
            reply_markup=process_manager_menu(int(page))
        )
    except TelegramBadRequest:
        pass

    await event.answer()

