import asyncio
import logging
import os
from aiogram import Dispatcher, types
from aiogram.filters.command import Command
import config as conf
from handlers import sticker_info, photo_info, document_info, video_info, show_info, audio_info, voice_info, animation_info, message_info
from texts import desc
from icecream import ic

os.makedirs('logs', exist_ok=True)

bot = conf.bot
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(sticker_info.router)
dp.include_router(photo_info.router)
dp.include_router(document_info.router)
dp.include_router(video_info.router)
dp.include_router(show_info.router)
dp.include_router(audio_info.router)
dp.include_router(voice_info.router)
dp.include_router(animation_info.router)
dp.include_router(message_info.router)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(desc.show_info, parse_mode='HTML')
    logging.warning(f'New: {message.from_user.id} - {message.from_user.first_name} : {message.from_user.last_name} - {message.from_user.username}')


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(desc.show_info, parse_mode='HTML')


@dp.errors()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Ошибка при обработке запроса {update}: {exception}')


async def main():
    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
        ic('Bot stopped')
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logs/bot.log',
                        format="%(filename)s:%(lineno)d #%(levelname)-8s" "[%(asctime)s] - %(name)s - %(message)s")
    logging.info('Bot starting...')
    asyncio.run(main())
