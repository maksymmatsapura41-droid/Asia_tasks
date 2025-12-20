from loguru import logger

logger.remove()
logger.add(
    "logs/app_json.json",
    serialize=True,
    format="{time} | {level} | {message}"
)

logger.info("Application started")
logger.warning("Memory usage high")