from loguru import logger


def add_user(record):
    record["extra"]["user_id"] = 42

logger.remove()
logger.add("app.log", format="{time} | {level} | {extra[user_id]} | {message}")
logger = logger.patch(add_user)
logger.info("Hello!")

