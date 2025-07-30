import sqlite3

from deep_translator import GoogleTranslator
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states.word_states import WordStates


message_router = Router()
translator = GoogleTranslator(source='en', target='ru')

@message_router.message(WordStates.waiting_for_word)
async def add_word_db(message: Message, state: FSMContext):
    user_word = message.text.split(' ')
    user_id = message.from_user.id
    word = user_word[0]
    word_usertrans = user_word[1]
    word_googltrans = translator.translate(word)

    con = sqlite3.connect("data_base.db")
    cur = con.cursor()
    cur.execute("""
            INSERT INTO words (
                user_id,
                word,
                word_usertrans,
                word_googltrans
            )
            VALUES (?, ?, ?, ?)""", (
            user_id,
            word,
            word_usertrans,
            word_googltrans)
            )
    con.commit()
    con.close()
    await state.clear()
