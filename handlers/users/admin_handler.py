import time

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from data import config
from loader import dp, db, _
from utils.db_api.commands_admin import all_register_users, count_users


@dp.message_handler(Command('all_register_users'), user_id=config.ADMINS)
async def get_all_register_users(message: types.Message):
    users = await all_register_users()
    count = await count_users()
    await message.answer(_('Всего пользователей: {}, зарегестривованые из них: {}').format(count, len(users)))
    for user in users:
        time.sleep(0.3)
        await message.answer(user)


@dp.message_handler(Command('drop_all_users'), user_id=config.ADMINS)
async def drop_all_users(message: types.Message):
    await db.set_bind(config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()
    await message.answer(_('База пользователей удалена'))

