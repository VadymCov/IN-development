from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=
    [
        [InlineKeyboardButton(text="✍ Added", callback_data='add')],
        [InlineKeyboardButton(text="‍👀 Learn", callback_data='show_words')]
    ])
