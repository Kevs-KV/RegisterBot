import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()

    print('Добавляем')
    await quick_commands.add_user(id=1, fullname_tg='Dmitry', language='ru')
    await quick_commands.add_user(id=2, fullname_tg='Kevin', language='ru')
    print('Готово')

    count_users = await quick_commands.select_all_users()
    print(f'Получаем всей юзеров {count_users}')

    user = await quick_commands.select_user(id=1)
    print(f'Получил пользователя: {user}')


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
