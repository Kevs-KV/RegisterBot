

from loader import dp
from .language_moddleware import setup_middleware
from .throttling import ThrottlingMiddleware



if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
