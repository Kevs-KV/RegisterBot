from aiogram import executor
import logging
import filters
from utils.db_api import db_gino
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await db_gino.on_sturtap(dp)

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

