'''Создай два декоратора:
to_json - возвращает результат функции в виде JSON-строки.
from_json - преобразует JSON-строку в объект Python и передаёт его в функцию.'''

from functools import wraps
import json
from datetime import datetime


#@to_json / use json.dumps(result, ensure_ascii=False, default=str)
def get_data():
    user = {
        "id": 42,
        "username": "max",
        "email": "max@example.com",
        "is_active": True,
        "roles": ["student", "admin"],
        "created_at": datetime(2025, 1, 10, 14, 30)
    }
    return user

# @from_json
def print_user(data):
    required_fields = ("id", "username", "email")

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    print(data["username"], data["email"])

json_str = get_data()
print(json_str)
print_user(json_str)

#Expected result
# {"id": 42, "username": "max", "email": "max@example.com", "is_active": true, "roles": ["student", "admin"], "created_at": "2025-01-10 14:30:00"}
# max max@example.com