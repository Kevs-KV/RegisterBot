from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.markdown import hcode
from loader import dp, _
from utils.db_api import quick_commands as db
from data.config import ADMINS as admin





class EventContext(StatesGroup):
    title_event = State()
    content = State()
    image = State()




@dp.message_handler(Command('event_register'))
async def event_register(message: types.Message):
        await message.answer(_('Пришли название мероприятия'))
        await EventContext.title_event.set()




@dp.message_handler(state=EventContext.title_event)
async def answer_title_event(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title_event=title)
    await message.answer(_('Пришли текст к мероприятию'))
    await EventContext.content.set()


@dp.message_handler(state=EventContext.content)
async def answer_content(message: types.Message, state: FSMContext):
    content = message.text
    await state.update_data(content_text=content)
    await message.answer(_('Пришли фото к мероприятию'))
    await EventContext.image.set()


@dp.message_handler(state=EventContext.image)
async def answer_image(message: types.Message, state: FSMContext):
    image = message.text
    await state.update_data(image=image)
    result = await state.get_data()
    title_event = result.get('title_event')
    context = result.get('content_text')
    await message.answer(f'{title_event}, {context}, {image}')
    await state.finish()

