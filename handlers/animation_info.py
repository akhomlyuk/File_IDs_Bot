from aiogram import Router, F
from aiogram.types import Message
import config as conf
import logging

router: Router = Router()


@router.message(F.animation)
async def bot_get_animation_info(message: Message):
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    animation_id = message.animation.file_id
    file_info = await conf.bot.get_file(animation_id)
    await message.answer(f'<b>Animation id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Animation size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Animation unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
