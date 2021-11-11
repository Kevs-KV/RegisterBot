from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from geopy.geocoders import Nominatim

from keyboards.default.cancel_button import cancel_register_button
from keyboards.default.contact_button import keyboard_contact_button
from keyboards.default.location_button import keyboard_location_button
from keyboards.inline.country_callback import country_markup_register
from keyboards.inline.languages_callback import languages_markup
from loader import dp, _
from middlewares.language_moddleware import get_lang
from states.registerstate import RegisterUsers
from utils.db_api.quick_commands import add_user, register_user_db, set_status_register, drop_register_users
from utils.validations_state import validations_phone, validations_email, validations_fullname


@dp.message_handler(state='*', text=['Отмена', 'Cancel'])
async def cancel_register_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(_('Регистрация прервана'), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command('register'))
async def register_users(message: types.Message):
    user_id = message.from_user.id
    user_lang = await get_lang(user_id)
    user_status_register = await set_status_register(user_id)
    if not user_status_register or user_status_register is None:
        if not user_lang:
            await add_user(fullname_tg=message.from_user.full_name, id=message.from_user.id)
            await message.answer(_('Пришли мне язык'), reply_markup=languages_markup)
        else:
            cancel_markup = await cancel_register_button()
            await message.answer(_('Начнем регистрацию'))
            await message.answer(_('Пришли свое имя'), reply_markup=cancel_markup)
            await RegisterUsers.name.set()
    else:
        await message.answer(_('Вы уже зарегестрированы'))


@dp.message_handler(state=RegisterUsers.name)
async def register_name_user(message: types.Message, state: FSMContext):
    name = message.text
    valid_name = await validations_fullname(name)
    if valid_name:
        cancel_markup = await cancel_register_button()
        await state.update_data(name=name)
        await message.answer(_('Пришли свою фамилию'), reply_markup=cancel_markup)
        await RegisterUsers.username.set()
    else:
        await message.answer(_('Странное имя... Пришли имя заново'))
        await RegisterUsers.name.set()


@dp.message_handler(state=RegisterUsers.username)
async def register_username_user(message: types.Message, state: FSMContext):
    username = message.text
    valid_username = await validations_fullname(username)
    if valid_username:
        keyboard_location = await keyboard_location_button()
        await state.update_data(username=username)
        await message.answer(_('Пришли свою страну'), reply_markup=keyboard_location)
        await RegisterUsers.country.set()
    else:
        await message.answer(_('Странная фамилия... Пришли фамилию заново'))


@dp.message_handler(state=RegisterUsers.country, content_types=types.ContentTypes.LOCATION)
async def register_country(message: types.Message, state: FSMContext):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = message.location
    letitude = location.latitude
    longitude = location.longitude
    location_users = str(geolocator.reverse(str(letitude) + "," + str(longitude)))
    print(location_users)
    location = location_users
    country = (location_users.split(', '))[-1]
    cancel_markup = await cancel_register_button()
    await state.update_data(country=country, location=location)
    await message.answer(_('Пришли свой возраст'), reply_markup=cancel_markup)
    await RegisterUsers.age.set()


@dp.callback_query_handler(state=RegisterUsers.country, text_contains="country")
async def register_country(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    command_country = call.data.split('_')
    country = command_country[1]
    await state.update_data(country=country)
    cancel_markup = await cancel_register_button()
    await call.message.answer(_('Пришли свой город'), reply_markup=cancel_markup)
    await RegisterUsers.city.set()


@dp.message_handler(state=RegisterUsers.country)
async def error_register_country(message: types.Message):
    country_markup = await country_markup_register()
    await message.answer(_('Выберите страну из меню'), reply_markup=country_markup)
    await RegisterUsers.country.set()


@dp.message_handler(state=RegisterUsers.city)
async def register_city_user(message: types.Message, state: FSMContext):
    location = message.text
    await state.update_data(location=location)
    cancel_markup = await cancel_register_button()
    await message.answer(_('Пришли свой возраст'), reply_markup=cancel_markup)
    await RegisterUsers.age.set()


@dp.message_handler(state=RegisterUsers.age)
async def register_country_user(message: types.Message, state: FSMContext):
    try:
        if message.text in ['Cancel', 'Отмена']:
            await cancel_register_users(message, state)
        else:
            age = int(message.text)
            if 80 >= age >= 18:
                await state.update_data(age=age)
                cancel_markup = await cancel_register_button()
                await message.answer(_('Пришли свой email'), reply_markup=cancel_markup)
                await RegisterUsers.email.set()
            else:
                await message.answer(_('К сожалению ваш возраст не подходит'))
                await cancel_register_users(message, state)
    except:
        await message.answer(_('Неправильно вводимые данные, введите возраст заново'))
        await RegisterUsers.age.set()


@dp.message_handler(state=RegisterUsers.email)
async def register_email_user(message: types.Message, state: FSMContext):
    email = message.text
    valid_email = await validations_email(email)
    if valid_email:
        await state.update_data(email=email)
        keyboard_contact = await keyboard_contact_button()
        await message.answer(_('Пришли свой номер телефона'), reply_markup=keyboard_contact)
        await RegisterUsers.phone.set()
    else:
        await RegisterUsers.email.set()
        await message.answer(_('Почтовое имя на валидно, введи email заново'))


@dp.message_handler(state=RegisterUsers.phone, content_types=types.ContentTypes.CONTACT)
async def register_phone_keyboard(message: types.Message, state: FSMContext):
    phone = message.contact['phone_number']
    await state.update_data(phone=phone)
    await finish_register(state)
    await message.answer(_('Регистрация завершена'), reply_markup=ReplyKeyboardRemove())
    await message.answer(_('Отменить регистрацию - /cancel_register'))


@dp.message_handler(state=RegisterUsers.phone)
async def register_phone_user(message: types.Message, state: FSMContext):
    state_result = await state.get_data()
    country = state_result.get('country')
    text = message.text
    phone = await validations_phone(phone=text, country=country)
    if phone:
        await state.update_data(phone=phone)
        await finish_register(state)
        await message.answer(_('Регистрация завершена'), reply_markup=ReplyKeyboardRemove())
        await message.answer(_('Отменить регистрацию - /cancel_register'))
    else:
        await message.answer(_('Номер не валидный'))
        await message.answer(_('Пришлите номер заново'))
        await RegisterUsers.phone.set()


async def finish_register(state: FSMContext):
    result = await state.get_data()
    print(result)
    name = result.get('name')
    username = result.get('username')
    country = result.get('country')
    age = result.get('age')
    email = result.get('email')
    phone = result.get('phone')
    location = result.get('location')
    await register_user_db(name=name, username=username, country=country, age=age,
                           email=email, phone=phone, location=location)
    print('Запись выполнена')
    await state.finish()


@dp.message_handler(Command('cancel_register'))
async def cancel_status_register_users(message: types.Message):
    user_id = message.from_user.id
    await drop_register_users(user_id)
    await message.answer(_('Регистрация отменена'))
