from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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




start_markup_register = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Да", callback_data="startregister")],
        [
            InlineKeyboardButton(text="Нет", callback_data="noregister")
        ]
    ]
)