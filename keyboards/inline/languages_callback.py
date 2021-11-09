from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import _

languages_markup = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
        [
            InlineKeyboardButton(text="English", callback_data="lang_en")
        ]
    ]
)



languages_markup_update = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Русский", callback_data="update_lang_ru")],
        [
            InlineKeyboardButton(text="English", callback_data="update_lang_en")
        ]
    ]
)


languages_markup_start = InlineKeyboardMarkup(
    inline_keyboard =
    [
        [
            InlineKeyboardButton(text="Русский", callback_data="start_lang_ru")],
        [
            InlineKeyboardButton(text="English", callback_data="start_lang_en")
        ]
    ]
)



start_markup_register = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_("Да"), callback_data="startregister")],
        [
            InlineKeyboardButton(text=_("Нет"), callback_data="noregister")
        ]
    ]
)

country_markup_register = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=_('Беларусь'), callback_data='country_Belarus')
        ],
        [
            InlineKeyboardButton(text=_('Россия'), callback_data='country_Russia')
        ],
        [
            InlineKeyboardButton(text=_('Великобритания'),  callback_data='country_England')
        ]

    ]
)