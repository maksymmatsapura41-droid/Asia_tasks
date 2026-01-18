'''Создай два декоратора:
to_json - возвращает результат функции в виде JSON-строки.
from_json - преобразует JSON-строку в объект Python и передаёт его в функцию.'''
import functools
import json
from datetime import datetime

def to_json(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        return json.dumps(fun(*args, **kwargs), ensure_ascii=False, default=str)
    return wrapper

@to_json # / use json.dumps(result, ensure_ascii=False, default=str)
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

def from_json(func):
    @functools.wraps(func)
    def wrapper(data, *args, **kwargs):
        dict_data = json.loads(data)
        return func(dict_data, *args, **kwargs)
    return wrapper

@from_json
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
