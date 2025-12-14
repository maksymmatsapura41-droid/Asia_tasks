from loguru import logger

def patch_message(record):
    record["message"] = f"[patched] {record['message']}"
logger = logger.patch(patch_message)
logger.info("Test")
