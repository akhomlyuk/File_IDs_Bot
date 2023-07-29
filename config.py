from aiogram import Bot
import os

bot_token = os.getenv('get_file_id_bot')
bot = Bot(token=bot_token)
