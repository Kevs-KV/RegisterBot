from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

keyboard_location = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=_('Лоцакия'),
                           request_location=True,
                           resize_keyboard=True,
                           one_time_keyboard=True)
        ],
        [
            KeyboardButton(text=_('Отмена'),
                           resize_keyboard=True,
                           one_time_keyboard=True)
        ],
        [
            KeyboardButton(text=_('Вручную'),
                           resize_keyboard=True,
                           one_time_keyboard=True
                           )
        ]
    ]
)
