from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


async def start_register_callback():
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
    return start_markup_register
