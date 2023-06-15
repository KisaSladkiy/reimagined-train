from env import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
import os
#
# Диспетчер принимает запросы пользователя
#
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())  # Диспатчер
admin_id = 5208563645
#
#
#
if not os.path.exists("database.json"):
    with open("database.json", "x") as file:
        temp = {"users": []}
        json.dump(temp, file, indent=4)

with open("database.json", "r") as file:
    database = json.load(file)
    database: dict[str, list[dict]]
#
# ЮЗЕРНЕЙМ ПОЛЬЗОВАТЕЛЯ
#
#
# КНОПКА ДЛЯ ПРОСМОТРА ТАРИФА И ОБРАТНОЙ СВЯЗИ
#
@dp.message_handler(commands=['start'])
async def button(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2)
    button_rate = InlineKeyboardButton(text="Прайс-лист",
                                       url="https://docs.google.com/spreadsheets/d/1hqbRithEEBsBCVnOWXWAKvYNkkY4pMiTzIGCQxflW5g/edit#gid=901990233")
    button_feedback = InlineKeyboardButton(text="Обратная связь", callback_data="butt_id2")
    button_help = InlineKeyboardButton(text="Помощь", callback_data="butt_id3")
    button_info = InlineKeyboardButton(text="Информация", callback_data="butt_id4")
    markup.add(button_rate, button_feedback, button_help, button_info,)
    await bot.send_message(message.chat.id, "🚘Вас приветствует компания ВВП-Бампер.🚘\nВыберите нужную опцию:",
                           reply_markup=markup)

    existing_users = database["users"]
    user_id = message.from_id

    for user in existing_users:
        if user_id == user["id"]:
            break
    else:
        existing_users.append({"id": user_id, "url": message.from_user.url, "username": message.from_user.username})
#
# ОТВЕТ ОТ НАЖАТИЯ ОБРАТНОЙ СВЯЗИ
#
@dp.callback_query_handler(lambda c: c.data == "butt_id2")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Узнать о наличии товара на складе, вы можете по номеру телефона:")
    await bot.send_message(call.message.chat.id,
                           "Рабочий телефон: +79177655343\nWhatsApp: +79170427776\nTelegram: @kls1337")
    await bot.send_message(call.message.chat.id, "Время работы: Ежедневно с 07:00 - 16:00 МСК")
#
#ОТВЕТ ОТ КНОПКИ ПОМОЩИ
#
@dp.callback_query_handler(lambda d: d.data == "butt_id3")
async def to_help(call: types.callback_query):
    await bot.send_message(call.message.chat.id, "Команды бота:\n /help - показывает все команды бота.\n /start - перезапускает бота.\n /info - узнать информацию о компании\n /availability - узнать о наличие товара на складе ")
#
#
#
@dp.callback_query_handler(lambda f: f.data == "butt_id4")
async def to_info(call: types.callback_query):
    await bot.send_message(call.message.chat.id, "ВВП-бампер - компания основанная в 2020 году, за 3 года мы получили доверие множества довольных клиентов.\nНаши преимущества:\n " \
                                                             "⭐️Качественное обслуживание️\n ⭐️Лучшее качество деталей ️\n ⭐️Большой ассортимент\n ⭐️Быстрая скорость доставки️")
#@dp.callback_query_handler(lambda g: g.data == "butt_id5")
#async def to_info(call: types.callback_query):
   #await call.message.delete()


try:
    executor.start_polling(dp)
finally:
    with open("database.json", "w") as file:
        json.dump(database, file, indent=4)
