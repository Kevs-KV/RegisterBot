from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


async def country_markup_register():
    country_markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text=_('Беларусь'), callback_data='country_Belarus')
            ],
            [
                InlineKeyboardButton(text=_('Россия'), callback_data='country_Russia')
            ],
            [
                InlineKeyboardButton(text=_('Великобритания'), callback_data='country_England')
            ]

        ]
    )
    return country_markup
