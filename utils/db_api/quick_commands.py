from asyncpg import UniqueViolationError
from aiogram import types

from loader import db
from utils.db_api.schemas.user import User




async def add_user(id: int, fullname_tg: str, language: str = None):
    try:
        user = User(id=id, fullname_tg=fullname_tg, language=language)

        await user.create()

    except UniqueViolationError:
        pass


async def get_user(user_id: int):
    user = await User.query.where(User.id == user_id).gino.first()
    return user



async def register_user_db(name, username, email, phone):
    user_id = types.User.get_current().id
    user = await get_user(user_id)
    await user.update(name=name, email=email, username=username, phone=phone, status_register=True).apply()


async def select_all_users():
    users = await User.query.gino.all()
    return users



async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    print(user)
    return user



async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()





async def update_user_username(telegram_id, name):
    user = await User.get(telegram_id)
    await user.update(name=name).apply()





async def set_language(language):
    user_id = types.User.get_current().id
    user = await get_user(user_id)
    await user.update(language=language).apply()


