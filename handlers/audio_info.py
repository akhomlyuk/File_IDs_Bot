from aiogram import Router, F
from aiogram.types import Message
import config as conf

router: Router = Router()


@router.message(F.audio)
async def bot_get_audio_info(message: Message):
    audio_id = message.audio.file_id
    file_info = await conf.bot.get_file(audio_id)
    await message.answer(f'<b>Audio id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Audio size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Audio unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
