from aiogram import Bot, Dispatcher
from aiogram.types import Message
import logging
from env import TOKEN

logging.basicConfig(level = logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
all_users = set()

@dp.message_handler(commands = ['start'])
async def _(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in all_users:
        all_users.add(user_id)
    await state.update_data({"user_id": message.from_user.id})
    await message.answer("Привет! Напиши мне что-нибудь!")
    await message.answer(f"Всего пользователей: {len(all_users)}")
    await state.set_state("wait_for_message")



def send_to_all_users(text):
    for user_id in all_users:
        await bot.send_message(user_id, text)



@dp.message_handler(state = "wait_for_message")
async def _(message: Message, state: FSMContext):
    text = f"{message.from_user.username} написал(а):\n{message.text}"