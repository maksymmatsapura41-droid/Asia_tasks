import json
from loguru import logger

def simple_serializer(record): # parse log record
    subset = {
        "time": record["time"].timestamp(),
        "level": record["level"].name,
        "message": record["message"],
        "context": record["extra"]
    }
    return json.dumps(subset)

def add_serialization(record):
    record["extra"]["json_output"] = simple_serializer(record)

# Create the add_serialization() function that will be applied to each log record.
# This function calls simple_serializer()
# and stores the resulting JSON in the record’s extra dictionary under the "json_output" key.

logger.remove()
logger = logger.patch(add_serialization)
# Patches the logger with the add_serialization() function using .patch(),
# which ensures every future log record is processed by this function.
logger.add("custom.json", format="{extra[json_output]}")
logger.bind(user="john").info("User logged in")
logger.bind(order_id=12345).info("Order processed")