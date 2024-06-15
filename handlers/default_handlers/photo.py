from telebot.types import Message
from loader import bot
import os

PHOTO_SAVE_PATH = os.getenv("PHOTO_SAVE_PATH", "photos")
os.makedirs(PHOTO_SAVE_PATH, exist_ok=True)

@bot.message_handler(content_types=["photo"])
def handle_photo(message: Message):
    photo = message.photo[-1]  # Получаем фото с максимальным разрешением
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    photo_path = os.path.join(PHOTO_SAVE_PATH, f"{photo.file_id}.jpg")
    with open(photo_path, "wb") as photo_file:
        photo_file.write(downloaded_file)
    
    bot.reply_to(message, f"Фото сохранено как {photo.file_id}.jpg")

@bot.message_handler(content_types=["document"])
def handle_document(message: Message):
    document = message.document
    file_info = bot.get_file(document.file_id)
    file_extension = os.path.splitext(document.file_name)[1].lower()
    if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
        downloaded_file = bot.download_file(file_info.file_path)

        document_path = os.path.join(PHOTO_SAVE_PATH, document.file_name)
        with open(document_path, "wb") as document_file:
            document_file.write(downloaded_file)
        
        bot.reply_to(message, f"Изображение сохранено как {document.file_name}")
    else:
        bot.reply_to(message, f"Файл не является изображением и не был сохранен.")

