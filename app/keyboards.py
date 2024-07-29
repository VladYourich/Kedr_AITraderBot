from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'), 
     KeyboardButton(text='Задать вопросы')],
    [KeyboardButton(text='Карзина')]
],
        resize_keyboard=True,
        input_field_placeholder="Выберите пунк меню"
)