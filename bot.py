from aiogram.utils import executor

from data_base import sqlite_db
from bot_create import dp
from units import client, admin, other


async def startup_bot(_):
    print('Статус бота - Онлайн')
    sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

other.register_handlers_other(dp)





executor.start_polling(dp, skip_updates=True, on_startup=startup_bot)