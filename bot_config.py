from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
storage = MemoryStorage()
database = Database("reviews.db")
dp = Dispatcher(bot, storage=storage)