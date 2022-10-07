
from bot_create import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#проверка модератора по ID
@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def check_moder(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'У вас достаточно прав доступа', reply_markup=admin_kb.btn_case_admin)
    await message.delete()

#начинает диалог нового пункта меню
async def load_start(message: types.Message):
    if message.from_user.id == ID: #определяет доступ только для модератра
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')

#Отмена состояний
async def cancel_load(message: types.Message, state: FSMContext):
    if message.from_user.id == ID: #определяет доступ только для модератра
        current_data = await state.get_state()
        if current_data is None:
            return
        await state.finish()
        await message.reply('Ну, как желаете')

#принятие первого ответа
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID: #определяет доступ только для модератра
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Введите название')

#принятие второго ответа
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID: #определяет доступ только для модератра
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите описание')

#принятие третьего ответа
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID: #определяет доступ только для модератра
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Укажите цену')

#приняте четвертого (последнего) ответа
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID: #определяет доступ только для модератра
        async with state.proxy() as data:
            data['price'] = float(message.text)
        
        await sqlite_db.sql_add(state)          #добавление записи в БД
        await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:{ret[2]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='\U00002B06 \U00002B06 \U00002B06', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))



#регитрация хэндлегов
def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(check_moder, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_load, state="*", commands=['отмена'])
    dp.register_message_handler(cancel_load, Text(equals='отмена', ignore_case=True), state="*")    
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_item, commands=['Удалить'])
    
