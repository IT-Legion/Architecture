import os
from telebot.types import Message
from loader import bot
from utils.logger import log_usage

# Получаем путь для сохранения аудио из переменных окружения
AUDIO_SAVE_PATH = os.getenv("AUDIO_SAVE_PATH", "audios")
os.makedirs(AUDIO_SAVE_PATH, exist_ok=True)

@bot.message_handler(content_types=['voice', 'audio'])
@log_usage
def handle_audio(message: Message):
    # Определяем тип сообщения (аудио или голосовое сообщение)
    if message.voice:
        audio_file = message.voice.file_id
    elif message.audio:
        audio_file = message.audio.file_id
    else:
        return

    # Сохраняем ID аудиофайла в файл
    with open('combined_audio.txt', 'a') as f:
        f.write(f'{audio_file}\n')

    # Отправляем подтверждение о сохранении файла
    bot.reply_to(message, "Аудио получено и сохранено.")

    # Скачиваем аудиофайл на сервер
    file_info = bot.get_file(audio_file)
    downloaded_file = bot.download_file(file_info.file_path)

    # Сохраняем аудиофайл в указанную директорию
    audio_path = os.path.join(AUDIO_SAVE_PATH, f'{audio_file}.ogg')
    with open(audio_path, 'wb') as f:
        f.write(downloaded_file)
