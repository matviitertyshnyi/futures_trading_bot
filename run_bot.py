from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("TELEGRAM_API_TOKEN")
if not TOKEN:   
    raise ValueError("No TELEGRAM_API_TOKEN found in environment variables")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("wassup gooner")

async def main():
    print("Starting bot...")
    
    await dp.start_polling(bot, on_startup=on_startup)
    
if __name__ == "__main__":
    asyncio.run(main())