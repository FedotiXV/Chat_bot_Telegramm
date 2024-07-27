import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboards import kb1, kb2
from random_fox import fox
from random import randint


API_TOKEN = config.token


logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет!, {name}", reply_markup=kb1)


#Хендлер на команду /fox
@dp.message(Command("fox"))
@dp.message(Command("Лиса"))
@dp.message(F.text.lower()=='покажи лису')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи лису, {name}")
    await message.answer_photo(photo=img_fox)

@dp.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")

@dp.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer('Ура-ура!')
    

@dp.message(F.text)
async def echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'кинь кубик' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'Лиса' in msg_user:
        await message.answer(f'Смотри какой я красивый, {name}', reply_markup=kb2)

    else:
        await message.answer(f'Я не знаю такого слова')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
