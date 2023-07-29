from aiogram import Bot
import os
from icecream import ic

bot_token = os.getenv('get_file_id_bot')
bot = Bot(token=bot_token)
