from telebot.types import Message

from loader import bot
from utils.logger import log_usage


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
@log_usage
def bot_echo(message: Message):
    bot.reply_to(
        message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
    )
