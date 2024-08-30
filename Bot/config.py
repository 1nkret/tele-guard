from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

from services.config import load_config

load_dotenv()
API_TOKEN = getenv("API_TOKEN")

config = load_config()

try:
    started_session = config["session_time"]
except KeyError:
    started_session = datetime.now()

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
