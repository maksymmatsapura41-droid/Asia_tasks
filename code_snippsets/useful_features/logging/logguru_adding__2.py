import sys
from loguru import logger

# logger.remove()
logger.add(sys.stdout, level="TRACE")
logger.trace("trace message")
logger.debug("debug message")