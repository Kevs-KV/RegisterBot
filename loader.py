from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


from utils.db_api.db_gino import db

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = db



from middlewares.language_moddleware import setup_middleware
# Настроим i18n middleware для работы с многоязычностью
i18n = setup_middleware(dp)
# Создадим псевдоним для метода gettext
_ = i18n.gettext