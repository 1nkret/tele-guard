from aiogram import Router
from aiogram.types import Message

from Bot.core.config import bot
from Bot.utils.access.members import get_from_json_owners


router = Router()

#
# @router.message()
# async def echo(message: Message):
#     for aci in get_from_json_owners():
#         await bot.send_message(
#             chat_id=aci,
#             text=f"{message.from_user.first_name} | {message.text}"
#         )
