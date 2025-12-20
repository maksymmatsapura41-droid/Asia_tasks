from loguru import logger
import re

SECRET_RE = re.compile(r"token=([A-Za-z0-9-]+)")
def hide_secrets(record):
    msg = record["message"]
    msg = SECRET_RE.sub("token=***", msg)
    record["message"] = msg

logger = logger.patch(hide_secrets)
logger.info("Sending request token=ABC123XYZ")
