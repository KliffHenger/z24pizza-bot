from aiogram import types, Dispatcher
from bot_create import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Бот стесняется и не может написать первым, напишите ему:\n ###########')

async def pizza_time(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 22:00, Сб-Вс с 10:00 до 23:00')

async def pizza_address(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул.Ленина 1')

async def menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_time, commands=['Время_работы'])
    dp.register_message_handler(pizza_address, commands=['Адрес'])
    dp.register_message_handler(menu_command, commands=['Меню'])