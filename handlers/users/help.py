from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (("Список команд: ",
             "/start - Начать диалог",
             '/register - начать регистрацию',
             "/help - Получить справку"))

    await message.answer("\n".join(text))


@dp.message_handler(Command('help_admin'))
async def bot_help(message: types.Message):
    text = (("Список команд: ",
             "/all_register_users - Показать всех зарегестрированных пользователей",
             '/drop_all_users - Отлистить базу',
             "/help - Получить справку"))

    await message.answer("\n".join(text))
