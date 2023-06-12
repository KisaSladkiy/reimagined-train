from env import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Диспетчер принимает запросы пользователя
bot = Bot(token=TOKEN)
dp = Dispatcher(bot) #Диспатчер
#
#КНОПКА ДЛЯ ПРОСМОТРА ТАРИФА И ОБРАТНОЙ СВЯЗИ
#
@dp.message_handler(commands=['start'])
async def button(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_rate = InlineKeyboardButton(text = "Тариф",callback_data = "butt_id1")
    button_feedback = InlineKeyboardButton(text = "Обратная связь", callback_data = "butt_id2")
    markup.add(button_rate,button_feedback)
    await bot.send_message(message.chat.id, "Вас приветствует компания ВВП-Бампер.Выберите нужную опцию", reply_markup=markup)
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
    await bot.send_message(call.message.chat.id, "Whatsapp: +79174938295 \n Telegram: @kls1337")




executor.start_polling(dp)