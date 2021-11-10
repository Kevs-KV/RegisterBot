from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from data import config
from loader import dp, db, _
from utils.db_api.commands_admin import all_register_users, count_users


@dp.message_handler(Command('all_register_users'))
async def get_all_register_users(message: types.Message):
    admins = [int(admin) for admin in config.ADMINS]
    if message.from_user.id in admins:
        users = await all_register_users()
        count = await count_users()
        await message.answer(_('Всего пользователей: {}, зарегестривованые из них: {}').format(count, len(users)))
        for user in users:
            await message.answer(user)
    else:
        await message.answer(_('Вы не администратор'))


@dp.message_handler(Command('drop_all_users'))
async def drop_all_users(message: types.Message):
    admins = [int(admin) for admin in config.ADMINS]
    if message.from_user.id in admins:
        await db.set_bind(config.POSTGRES_URL)
        await db.gino.drop_all()
        await db.gino.create_all()
        await message.answer(_('База пользователей удалена'))
    else:
        await message.answer(_('Вы не администратор'))
