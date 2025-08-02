import asyncio
from aiogram import Bot, Dispatcher


from config import YOUR_TOKEN
from database.models import init_db
from handlers.callbacks import callback_router
from handlers.messages import message_router

from handlers.start import start_router

bot = Bot(YOUR_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(message_router)
dp.include_router(callback_router)

async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())