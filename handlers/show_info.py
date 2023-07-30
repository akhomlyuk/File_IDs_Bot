from aiogram import Router, F
from aiogram.types import Message
from texts import desc
import logging
from icecream import ic

router: Router = Router()
show_info_commands = ['!help', 'help']


@router.message(F.text)
async def show_info(message: Message):
    try:
        if message.from_user.id != 539491282:
            logging.info(message.from_user)
        msg = message.text
        if msg.lower() in show_info_commands:
            await message.answer(desc.show_info, parse_mode='HTML')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')
