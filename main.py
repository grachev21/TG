
from aiogram import Bot, Dispatcher, executor, types


# Adding token
bot = Bot("6789289219:AAFwyqu5yEhghRAXMO-WffI0K5FHPXcn4vQ")

# add dispatcher
dp = Dispatcher(bot=bot)

# Create a decorator and pass the start command
@dp.message_handler(commands=["start"])

# Adding an asynchronous function
async def cmd_start(message: types.Message):
    # Send a message to the user when they enter start.
    # Passing the username through the f string
    await message.answer(f"{message.from_user.first_name} Добро пожаловать в магазин наклеек")


# This function processes messages from the user
@dp.message_handler()
async def answer(message: types.Message):
    # 'reply' responds to a user's message
    await message.reply("Я тебя не понимаю")

if __name__ == "__main__":
    executor.start_polling(dp)
