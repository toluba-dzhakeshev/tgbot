import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# from transliterate import translit (tak perevod ne po gostu poluchalsya)

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher() 
logging.basicConfig(level=logging.INFO)

translation_of_letters = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
    'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}

def my_translator(text, trans_let):
    return ''.join(trans_let.get(char, char) for char in text)

@dp.message(Command(commands=['start']))
async def proceed_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Privet, {user_name}!'
    logging.info(f'{user_name} {user_id} zapustil bota')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    
    name_parts = text.split()
    if len(name_parts) != 3:
        await message.answer(text='Please enter correctly')

    last_name, first_name, middle_name = name_parts
    last_name = my_translator(last_name, translation_of_letters)
    first_name = my_translator(first_name, translation_of_letters)
    middle_name = my_translator(middle_name, translation_of_letters)
    
    translated_name = f'{last_name} {first_name} {middle_name}'
    
    logging.info(f'{user_name} {user_id}: {text}, translated to {translated_name}')
    await message.answer(text=f'Your name in english is: {translated_name}')
    
if __name__ == '__main__':
    dp.run_polling(bot)
