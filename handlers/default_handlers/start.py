from telebot.types import Message

from loader import bot
from utils.logger import log_usage


@bot.message_handler(commands=["start"])
@log_usage
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
