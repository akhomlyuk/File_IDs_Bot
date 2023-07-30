from aiogram import Router, F
from aiogram.types import Message
import config as conf
import logging
from functions import parse_file_to_json

router: Router = Router()


@router.message(F.sticker)
async def bot_get_sticker_info(message: Message):
    json_data = parse_file_to_json(message, 'sticker')
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    sticker_id = message.sticker.file_id
    file_info = await conf.bot.get_file(sticker_id)
    await message.answer(f'<b>Sticker id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
    await message.answer(f'<b>Sticker size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
    await message.answer(f'<b>Sticker unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
    await conf.bot.send_document(message.chat.id, json_data)
