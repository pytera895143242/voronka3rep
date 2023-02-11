from aiogram import types
from misc import dp, bot
from .sqlit import reg_user, get_username
from .callbak_data import reg_p
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001612446247
reg_user(1,'SprintArbitraj')  # Запуск в БД


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, 'SprintArbitraj')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🇷🇺 Россия', callback_data='sprint_online')
    bat_b = types.InlineKeyboardButton(text='🇸🇱 Узбекистан', callback_data='bat_video2')
    bat_c = types.InlineKeyboardButton(text='🇵🇼 Казахстан', callback_data='sprint_online')
    bat_d = types.InlineKeyboardButton(text='🇰🇬 Кыргызстан', callback_data='sprint_online')
    bat_e = types.InlineKeyboardButton(text='🇹🇯 Таджикистан', callback_data='sprint_online')
    bat_f = types.InlineKeyboardButton(text='❓Другая страна', callback_data='sprint_online')

    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    markup.add(bat_f)

    await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 150)
    await bot.send_message(chat_id=message.chat.id, text= "С какой ты страны?", reply_markup=markup)