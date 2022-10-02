from aiogram import *
from aiogram.dispatcher.filters import Text

bot = Bot(token='5137903807:AAEtrp9rSqXKStp93h2_Q_OhNfey1QUJXoo')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def hello(message:types.message):
    await message.answer(f'Привет {message.from_user.username}, я бот-повторюшка ^.^')
    await message.answer('Напиши мне что-нибудь')

@dp.message_handler()
async def eho(message:types.message):
    await message.answer(message.text)
    
def main():
    executor.start_polling(dp)
    
if __name__ == '__main__':
    main()