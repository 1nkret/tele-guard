from aiogram import Router, types

from Bot.utils.updater.update_bot import update_project, restart_script, stop_script

router = Router()


@router.callback_query(lambda c: c.data == "update_project")
async def update_handler(query: types.Message):
    await query.message.answer("Starting updater...")
    await update_project(query.from_user.id)
    restart_script()
    stop_script()
