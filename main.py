import json
import logging
import time

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


async def handler(event, context):
    body = json.loads(event['body'])
    update = types.Update.parse_obj(body)
    await dp.feed_webhook_update(bot, update)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text='Привет', parse_mode='HTML')


@dp.message(Command('help'))
async def cmd_start(message: types.Message):
    await message.answer(text='Помощь', parse_mode='HTML')


@dp.message(F.text)
async def cmd_start(message: types.Message):
    await message.answer(text=message.text, parse_mode='HTML')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
