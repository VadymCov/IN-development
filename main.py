import asyncio
from aiogram import Bot, Dispatcher


from config import YOUR_TOKEN

from handlers.start import start_router

bot = Bot(YOUR_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())