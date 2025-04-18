from aiogram import Router, F
from aiogram.types import Message
import config as conf
import logging
from functions import parse_file_to_json

router: Router = Router()


@router.message(F.video)
async def bot_get_video_info(message: Message):
    try:
        json_data = parse_file_to_json(message, 'video')
        if message.from_user.id != 539491282:
            logging.info(message.from_user)
        video_id = message.video.file_id
        file_info = await conf.bot.get_file(video_id)
        await message.answer(f'<b>Video id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
        await message.answer(f'<b>Video size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
        await message.answer(f'<b>Video unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
        await conf.bot.send_document(message.chat.id, json_data)
    except Exception as e:
        logging.warning(e)
        await message.answer(f'{e}')

