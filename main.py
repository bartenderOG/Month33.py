import asyncio

from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters import Command

BOT_TOKEN = "8817249653:AAENiV742M5MveZ-4nuaElc0-noObDcoRNE"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()       #обработчик входящих обновлений

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}! Я бот."
        )
    print(f"Пользователь {message.from_user.first_name} отправил {message} в {message.date}")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Я могу помочь вам с различными задачами.\n\n"
        "Вот список доступных команд:\n"
        "/start - начать взаимодействие с ботом\n"
        "/help - получить справку о боте\n"
        "/about - узнать информацию о боте"
    )


@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "🤖 Я Telegram-бот.\n\n"
        "Мои возможности:\n"
        "• отвечать на команды\n"
        "• помогать пользователям\n"
        "• выполнять различные задачи\n\n"
        "Версия бота: 1.0"
    )

@dp.message(F.from_user.id == 8544992173)
async def get_group(message: Message):
    await message.answer("Привет мой Бон")



async def main():
    await dp.start_polling(bot)     #отправляет запрос на тг-сервер


if __name__ == "__main__":
    asyncio.run(main())     #для запуска функции

