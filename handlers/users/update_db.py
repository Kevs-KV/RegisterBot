from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from keyboards.inline.languages_callback import languages_markup_update
from loader import dp, _
from states.registerstate import RegisterUsers
from utils.db_api import quick_commands as db
from utils.db_api.commands_admin import all_register_users


@dp.message_handler(Command('update_language'))
async def update_language(message: types.Message):
    await message.answer('Пришли мне язык', reply_markup=languages_markup_update)



@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    # Достаем последние 2 символа (например ru)
    command_update = call.data.split('_')
    language = command_update[-1]
    await db.set_language(language)
    # После того, как мы поменяли язык, в этой функции все еще указан старый, поэтому передаем locale=lang
    await call.message.answer(_("Язык был установлен"))
    if command_update[0] == 'lang':
        await call.message.answer(_('Пришли свое имя'))
        await RegisterUsers.name.set()





# @dp.callback_query_handler(text_contains="update")
# async def call_update_language(call: CallbackQuery):
#     await call.message.edit_reply_markup()
#     # Достаем последние 2 символа (например ru)
#     language = call.data[-2:]
#     print('call_update_language')
#     try:
#         await db.set_language(language)
#         await call.message.answer(_("Ваш язык был изменен"))
#     except:
#         await call.message.answer(_("Вас нет в базе"))

    # После того, как мы поменяли язык, в этой функции все еще указан старый, поэтому передаем locale=lang
# @dp.message_handler(state='email')
# async def enter_username(message: types.Message, state: FSMContext):
#     email = message.text
#     await db.update_user_email(email=email, id=message.from_user.id)
#     user = await db.select_user(id=message.from_user.id)
#     await message.answer('Данные обновлены. Запись в бд: \n' +
#                          hcode(f'id={user.id}\n'
#                                f'name={user.name}\n'
#                                f'email={user.email}'))
#     await state.finish()



# @dp.message_handler(Command('language'))
# async def update_language(message: types.Message, state: FSMContext):
#     await message.answer('Пришли мне язык')
#     await state.set_state('language')



# @dp.message_handler(state='language')
# async def enter_language(message: types.Message, state: FSMContext):
#     language = message.text
#     await db.set_language(language=language)
#     user = await db.select_user(id=message.from_user.id)
#     await message.answer(_('Данные обновлены. Запись в бд: \n' +
#                          hcode(f'id={user.id}\n'
#                                f'name={user.name}\n'
#                                f'email={user.email}\n'
#                                f'language={user.language}')))
#     await state.finish()