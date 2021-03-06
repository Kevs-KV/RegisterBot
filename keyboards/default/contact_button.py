from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _


async def keyboard_contact_button():
    keyboard_contact = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text=_('Телефон'),
                               request_contact=True,
                               resize_keyboard=True,
                               one_time_keyboard=True
                               )
            ],
            [
                KeyboardButton(text=_('Отмена'),
                               resize_keyboard=True,
                               one_time_keyboard=True)
            ],
        ]
    )
    return keyboard_contact
