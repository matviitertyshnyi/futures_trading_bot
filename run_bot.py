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
GROUP_CHAT_ID = getenv("GROUP_CHAT_ID")
if not GROUP_CHAT_ID:
    raise ValueError("No GROUP_CHAT_ID found in environment variables. Create a group, add the bot, and set its ID in .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def on_start(message: types.Message):
    await message.answer(
        "giganiga"
    )
@dp.message(Command("sybau"))
async def on_start(message: types.Message):
    await message.answer(
        "bruh"
    )


@dp.message()
async def handle_messages(message: types.Message):
    """Handle messages in the group chat"""
    # Only respond to messages in the designated group chat
    if str(message.chat.id) == GROUP_CHAT_ID:
        #place to add trading-specific commands and features
        if message.text.startswith('/signal'):

            await message.reply("Processing trading signal...")
            #logic to process the signal can be added below

async def main():
    print("Starting bot...")
    try:
        # Send startup message to the group
        await bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text="test"
        )
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    asyncio.run(main())