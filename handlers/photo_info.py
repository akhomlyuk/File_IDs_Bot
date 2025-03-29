from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import config as conf
import logging
from icecream import ic
router: Router = Router()


@router.message(F.photo)
async def bot_get_photo_info(message: Message):
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    try:
        with open('~/python_bots/File_IDs_Bot/photo.json', 'w') as file:
            for photo in message.photo:
                file.write(str(photo) + '\n')

        file = FSInputFile("~/python_bots/File_IDs_Bot/photo.json")
        photo_id = message.photo[-1].file_id
        file_info = await conf.bot.get_file(photo_id)
        await message.answer(f'<b>Photo id:</b> <code>{file_info.file_id}</code>', parse_mode='HTML')
        await message.answer(f'<b>Photo size:</b> {file_info.file_size // 1024} Kb', parse_mode='HTML')
        await message.answer(f'<b>Photo unique id:</b> <code>{file_info.file_unique_id}</code>', parse_mode='HTML')
        await conf.bot.send_document(message.chat.id, file)
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')
