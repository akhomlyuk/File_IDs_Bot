from aiogram import Router, F
from aiogram.types import Message
import config as conf

router: Router = Router()


@router.message(F.animation)
async def bot_get_animation_info(message: Message):
    animation_id = message.animation.file_id
    file_info = await conf.bot.get_file(animation_id)
    await message.answer(f'<b>Animation id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Animation size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Animation unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
