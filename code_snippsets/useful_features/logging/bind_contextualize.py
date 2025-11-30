import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")


user_logger = logger.bind(user_id=123)
user_logger.info("User logged in")

user_logger.info("User started a session")
logger.info("User started a session")


with logger.contextualize(user_name="chopchop"):
    logger.info("User started a session")