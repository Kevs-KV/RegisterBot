from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

cancel_register_markup = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=_('Отмена'),
                           one_time_keyboard=True,
                           resize_keyboard=True)
        ],
    ]
)
