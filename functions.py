from aiogram.types import Message, FSInputFile
import json


def parse_file_to_json(message: Message, file_obj: str):
    msg_obj = message.model_dump(mode='python')
    data = {}
    for key, value in msg_obj[file_obj].items():
        if value is not None:
            data[key] = value

    with open('~/python_bots/File_IDs_Bot/data.json', 'w') as json_file:
        json.dump(data, json_file)

    # json_data = json.dumps(data)
    file = FSInputFile("~/python_bots/File_IDs_Bot/data.json")
    return file
