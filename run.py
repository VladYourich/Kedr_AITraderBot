import asyncio
import os
import logging
from typing import Optional

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers.handlers import router
from config.config import TOKEN

async def main():
    load_dotenv()
    #bot = Bot(token=os.getenv('TOKEN'))
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print("Хмм...! Выходим 8(((")