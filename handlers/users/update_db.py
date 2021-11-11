from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from handlers.users.start import continue_start_register_callback
from keyboards.inline.languages_callback import languages_markup_update
from loader import dp, _
from states.registerstate import RegisterUsers
from utils.db_api import quick_commands as db


@dp.message_handler(Command('update_language'))
async def update_language(message: types.Message):
    await message.answer(_('Выберите язык для обновления'), reply_markup=languages_markup_update)


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    command_update = call.data.split('_')
    language = command_update[-1]
    await db.set_language(language)
    await call.message.answer(_("Язык был установлен", locale=language))
    if command_update[0] == 'start':
        await continue_start_register_callback(call.message, language)
    if command_update[0] == 'lang':
        await call.message.answer(_('Пришли свое имя', locale=language))
        await RegisterUsers.name.set()
