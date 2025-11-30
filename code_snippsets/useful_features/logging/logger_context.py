import sys
from loguru import logger
import random
import uuid

logger.remove()
logger.add(sys.stdout, level="TRACE", format="{message} | {level} | {extra}")

logger.info("info message", extra=random.randint(0, 100), filename=str(uuid.uuid4()) + '.txt')
logger.warning("warning message", extra=random.randint(0, 100), filename=str(uuid.uuid4()) + '.txt')