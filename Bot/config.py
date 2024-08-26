from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

from services.config import load_config

load_dotenv()
API_TOKEN = getenv("API_TOKEN")

owner = getenv("OWNER").split(",")
allowed_chat_ids = getenv("ALLOWED_CHAT_IDS").split(",") + owner

config = load_config()
started_session = config["session_time"]

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
