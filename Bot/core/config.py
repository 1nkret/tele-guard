import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

from services.config import load_config

load_dotenv()
API_TOKEN = getenv("API_TOKEN")
owner_url = getenv("OWNER_TELEGRAM_URL")

logging.basicConfig(filename="logs/bot.log", level=logging.INFO)
logger = logging.getLogger(__name__)

config = load_config()

started_session = datetime.now()
session_update = started_session

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
