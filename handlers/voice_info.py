from aiogram import Router, F
from aiogram.types import Message
import config as conf
import logging

router: Router = Router()


@router.message(F.voice)
async def bot_get_voice_info(message: Message):
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    voice_id = message.voice.file_id
    file_info = await conf.bot.get_file(voice_id)
    await message.answer(f'<b>Voice id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Voice size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Voice unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
