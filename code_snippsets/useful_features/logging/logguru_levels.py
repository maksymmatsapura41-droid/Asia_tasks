# first of all install loguru
from loguru import logger

logger.trace("trace message")	#5 Extremely detailed information for debugging
logger.debug("debug message")	#10 Information useful during development
logger.info("info message")	#20 General information about what’s happening in the code
logger.success("success message")	#25 Notifications of successful operations
logger.warning("warning message")	#30 Warnings about something unexpected but not necessarily problematic
logger.error("error message")	#40 Errors for when something fails but the application continues running
logger.critical("critical message")	#50 Critical errors that are serious and urgent