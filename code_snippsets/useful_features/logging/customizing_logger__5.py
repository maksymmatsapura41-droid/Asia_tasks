import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{name} {time} {message}", level="DEBUG")
logger.debug("debug message")
logger.info("info message")

logger.add(
    sys.stderr,
    format="[{time:HH:mm:ss}] >> {name}:{line} >> {level}: {message}"
)

logger.add(
    sys.stdout,
    format="[{time:HH:mm:ss}] >> {name}:{line} >>"
           "<green>{level}</green>: {message}"
)

logger.error("error message")

logger.add(
    sys.stdout,
    format="[{time:HH:mm:ss}] >> {name}:{line} >>"
           "<green>{level}</green>: <level>{message}</level>"
)

logger.error("error message")
# {time}: Timestamp
# {level}: Log level
# {message}: The actual log message
# {name}: Module name
# {line}: Line number