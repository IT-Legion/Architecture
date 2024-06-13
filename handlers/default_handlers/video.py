from telebot.types import Message
from loader import bot
import os

# Получаем путь для сохранения видео из переменных окружения
VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", "videos")

# Создаем директорию для сохранения видео, если она не существует
os.makedirs(VIDEO_SAVE_PATH, exist_ok=True)

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB

@bot.message_handler(content_types=["video", "video_note"])
def handle_video(message: Message):
    if message.content_type == "video_note":
        video = message.video_note
    else:
        video = message.video

    if video.file_size > MAX_FILE_SIZE:
        bot.reply_to(message, "Видео слишком большое. Пожалуйста, отправьте файл размером до 20 МБ.")
        return

    file_info = bot.get_file(video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    video_path = os.path.join(VIDEO_SAVE_PATH, f"{video.file_id}.mp4")
    with open(video_path, "wb") as video_file:
        video_file.write(downloaded_file)
    
    bot.reply_to(message, f"Видео сохранено как {video.file_id}.mp4")

@bot.message_handler(content_types=["document"])
def handle_document(message: Message):
    document = message.document
    file_extension = os.path.splitext(document.file_name)[1].lower()
    if file_extension in ['.mp4', '.mkv', '.avi', '.mov']:
        if document.file_size > MAX_FILE_SIZE:
            bot.reply_to(message, "Видео слишком большое. Пожалуйста, отправьте файл размером до 20 МБ.")
            return

        file_info = bot.get_file(document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        document_path = os.path.join(VIDEO_SAVE_PATH, document.file_name)
        with open(document_path, "wb") as document_file:
            document_file.write(downloaded_file)
        
        bot.reply_to(message, f"Видео сохранено как {document.file_name}")
    else:
        bot.reply_to(message, f"Файл не является видео и не был сохранен.")
