from aiogram import Router, types
from aiogram.filters import Command

from Bot.utils.updater.update_bot import update_project, restart_script, stop_script

router = Router()

@router.message(Command("update"))
async def update_handler(message: types.Message):
    await message.answer("Starting updater...")
    await update_project(message.chat.id)
    restart_script()
    stop_script()
