from aiogram import types, Dispatcher
from bot_create import dp, bot
import re


NON_LETTERS = re.compile('[^а-яё \-]+', flags=re.UNICODE)


async def echo_message(message: types.Message):
    words = message.text.split()
    word = NON_LETTERS.sub("", words[-1].lower() or words[0].lower())
    if word[:4] == "пизд":
        # await message.reply('Можно не материться ?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:2] == "ху":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:3] == "aху":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:3] == "оху":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:4] == "наху":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:4] == "говн":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    if word[:4] == "поху":
        # await message.reply('Можно не материться?')
        await bot.delete_message(message.chat.id, message.message_id)
        # print(message.text)
    else:
        print(message.text)

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_message)