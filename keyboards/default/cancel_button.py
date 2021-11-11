from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _


async def cancel_register_button():
    cancel_register_markup = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text=_('Отмена'),
                               one_time_keyboard=True,
                               resize_keyboard=True)
            ],
        ]
    )
    return cancel_register_markup
