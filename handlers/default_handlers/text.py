import os
from telebot.types import Message
from loader import bot

# Получаем путь для сохранения текстовых файлов из переменных окружения
TEXT_SAVE_PATH = os.getenv("TEXT_SAVE_PATH", "texts")
os.makedirs(TEXT_SAVE_PATH, exist_ok=True)

@bot.message_handler(content_types=['document'])
def handle_document(message: Message):
    document = message.document

    # Проверяем размер файла
    MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB
    if document.file_size > MAX_FILE_SIZE:
        bot.reply_to(message, "Файл слишком большой. Пожалуйста, отправьте файл размером до 20 МБ.")
        return

    # Скачиваем файл на сервер
    file_info = bot.get_file(document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Сохраняем файл в указанную директорию
    file_path = os.path.join(TEXT_SAVE_PATH, document.file_name)
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)

    # Отправляем подтверждение о сохранении файла
    bot.reply_to(message, f"Файл '{document.file_name}' сохранен.")
