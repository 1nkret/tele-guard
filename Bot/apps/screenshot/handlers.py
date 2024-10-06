from aiogram import Router, types

from Bot.core.config import bot
from Bot.utils.system.screenshot import screenshot
from Bot.apps.screenshot.keyboard import back_to_menu

router = Router()

@router.callback_query(lambda c: c.data == "screenshot")
async def screenshot_handler(event: types.CallbackQuery):
    await event.message.answer("wait...")
    screen = screenshot()

    photo = types.FSInputFile(screen)
    await bot.send_photo(event.from_user.id, photo, reply_markup=back_to_menu())
