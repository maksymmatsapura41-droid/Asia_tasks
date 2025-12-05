import sys
from loguru import logger
import random
import uuid

logger.remove()
logger.add(sys.stdout, level="TRACE", format="{message} | {level} | {extra}")

GLOBAL_ID = 100000


logger.info("info message", extra=random.randint(0, 100), filename=str(uuid.uuid4()) + '.txt', global_id=GLOBAL_ID)
logger.warning(f"warning message {GLOBAL_ID}", extra=random.randint(0, 100), filename=str(uuid.uuid4()) + '.txt')