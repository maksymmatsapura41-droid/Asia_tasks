from loguru import logger
import time

logger.remove()
logger.add("logs/app.log", level="INFO" ,format="{message} | {time} | {name} ", rotation="10 B", retention="5 seconds")
logger.info("User started a session")

for i in range(10):
    logger.info(f"debug message{i}")
    time.sleep(2)



# examples
logger.add(
    "logs/app.log",
    rotation="10 MB",          # every 10 creating new file
    retention="7 days",        # save only 7 days
    compression="zip",         # old files archive
)

logger.add(
    "logs/{time:YYYY-MM-DD}.log",
    rotation="00:00",      # create new log at midnight
    retention="30 days"
)

logger.add("logs/app.log", rotation=1000, retention="10 days")  # generate new log after 1000 records

# add files with different level
logger.add("logs/info.log", level="INFO", rotation="5 MB")
logger.add("logs/error.log", level="ERROR", rotation="2 MB")


# When critical rotate file

def should_rotate(message, file):
    return "CRITICAL" in message.record["message"]

logger.add(
    "logs/custom.log",
    rotation=should_rotate,
    retention="14 days"
)

# logs by service

SERVICE = "worker-1"

logger.add(
    f"logs/{SERVICE}/{{time:YYYY-MM-DD}}.log",
    rotation="1 day",
    retention="10 days"
)
