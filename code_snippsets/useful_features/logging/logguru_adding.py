import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="TRACE")
logger.trace("trace message")
logger.debug("debug message")