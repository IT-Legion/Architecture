import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='bot_usage.log', filemode='a',
                    format='%(asctime)s - %(message)s')

def log_usage(func):
    def wrapper(message, *args, **kwargs):
        user = message.from_user
        logging.info(f"User {user.id} ({user.username}) used command {message.text}")
        return func(message, *args, **kwargs)
    return wrapper
