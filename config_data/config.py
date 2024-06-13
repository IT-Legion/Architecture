import os
from dotenv import load_dotenv, find_dotenv



if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()



BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
TEXT_SAVE_PATH = os.getenv("TEXT_SAVE_PATH", "texts")
PHOTO_SAVE_PATH = os.getenv("PHOTO_SAVE_PATH", "photos")
VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", "videos")
AUDIO_SAVE_PATH = os.getenv("AUDIO_SAVE_PATH", "audios")

#RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)
