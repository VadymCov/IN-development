import sqlite3

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.keyboards import main_menu_key
from states.word_states import WordStates
callback_router = Router()

@callback_router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    user_name = callback.from_user.first_name
    await callback.message.edit_text(f"👋{user_name}", reply_markup=main_menu_key())


@callback_router.callback_query(F.data == "add")
async def add_text(callback: CallbackQuery, state: FSMContext):
    await state.set_state(WordStates.waiting_for_word)
    await callback.message.edit_text("expirement")
    await callback.answer()


@callback_router.callback_query(F.data.startswith("show_words_"))
async def return_translation(callback: CallbackQuery):
    user_id = callback.from_user.id
    word_id = None

    if callback.data.split("_")[2]:
        word_id = int(callback.data.split("_")[2])

    con = sqlite3.connect("data_base.db")
    cur = con.cursor()
    cur.execute('''
        SELECT id, word, word_usertrans FROM words WHERE user_id = ?''', (user_id,))
    res = cur.fetchall()
    con.close()

    text = "    📑 List of words\n"
    buttons = []

    for w_id, words, word_trans in res:
        if w_id == word_id:
            buttons.append([InlineKeyboardButton(text=word_trans, callback_data=f"show_words_{w_id}" )])
        else:
            buttons.append([InlineKeyboardButton(text=words, callback_data= f"show_words_{w_id}")])

    buttons.append([InlineKeyboardButton(text="👈  back to menu", callback_data="main_menu")])
    keyboards = InlineKeyboardMarkup(inline_keyboard=buttons)

    await callback.message.edit_text(text, reply_markup=keyboards)
    await callback.answer()



