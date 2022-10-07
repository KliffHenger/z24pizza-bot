from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))
token = "5687565025:AAEV0mq_a20k9Rs0FYCduewQaNNgP2qHC8Q"
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)

