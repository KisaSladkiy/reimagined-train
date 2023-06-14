from env import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#Диспетчер принимает запросы пользователя
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage()) #Диспатчер
admin_id = 5208563645
#
#ЮЗЕРНЕЙМ ПОЛЬЗОВАТЕЛЯ
#
#
#КНОПКА ДЛЯ ПРОСМОТРА ТАРИФА И ОБРАТНОЙ СВЯЗИ
#
@dp.message_handler(commands=['start'])
async def button(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_rate = InlineKeyboardButton(text = "Прайс-лист",url="https://docs.google.com/spreadsheets/d/1hqbRithEEBsBCVnOWXWAKvYNkkY4pMiTzIGCQxflW5g/edit#gid=901990233")
    button_feedback = InlineKeyboardButton(text = "Обратная связь", callback_data = "butt_id2")
    markup.add(button_rate,button_feedback)
    await bot.send_message(message.chat.id, "Вас приветствует компания ВВП-Бампер.\nВыберите нужную опцию:", reply_markup=markup)
    await bot.send_message(admin_id, message.from_user.username)

#
 #ОТВЕТ ОТ НАЖАТИЯ ТАРИФА
 #
@dp.callback_query_handler(lambda b: b.data == "butt_id1")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Кнопка нажата")
#
#ОТВЕТ ОТ НАЖАТИЯ ОБРАТНОЙ СВЯЗИ
#
@dp.callback_query_handler(lambda c: c.data == "butt_id2")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Узнать о наличии товара на складе, вы можете по номеру телефона:")
    await bot.send_message(call.message.chat.id, "Рабочий телефон:+79177655343\nWhatsApp: +79170427776\nTelegram: @kls1337")
    await bot.send_message(call.message.chat.id,"Время работы: Круглосуточно с 07:00 - 16:00 МСК")
#
#
executor.start_polling(dp)