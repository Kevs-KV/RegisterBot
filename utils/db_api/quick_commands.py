from aiogram import types
from asyncpg import UniqueViolationError

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



async def drop_register_users(user_id):
    user = await get_user(user_id)
    await user.update(status_register=False).apply()




async def register_user_db(name, username, country, location, age, email, phone):
    user_id = types.User.get_current().id
    user = await get_user(user_id)
    await user.update(name=name, email=email, username=username,
                      country=country, location=location,
                      age=age, phone=phone, status_register=True).apply()


async def select_all_users():
    users = await User.query.gino.all()
    return users



async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user



async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()



async def update_user_username(telegram_id, name):
    user = await User.get(telegram_id)
    await user.update(name=name).apply()


async def set_status_register(user_id):
    user = await get_user(user_id)
    if user:
        return user.status_register


async def set_language(language):
    user_id = types.User.get_current().id
    user = await get_user(user_id)
    await user.update(language=language).apply()



async def select_country(user_id):
    user = await get_user(user_id)
    if user:
        print(user.country)
        return user.country

