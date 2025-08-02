from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import main_menu_key

start_router = Router()


@start_router.message(Command('start'))
async def start_comand(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f'👋 {user_name}', reply_markup=main_menu_key()
    )


