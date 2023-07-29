from aiogram import Router, F
from aiogram.types import Message
import config as conf

router: Router = Router()


@router.message(F.photo)
async def bot_get_photo_info(message: Message):
    photo_id = message.photo[0].file_id
    file_info = await conf.bot.get_file(photo_id)
    await message.answer(f'<b>Photo id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Photo size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Photo unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
