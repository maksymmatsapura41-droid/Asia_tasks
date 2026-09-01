# Found users older than 18 and name starts with "O"
users = [
    {"name": "Anna", "age": 22},
    {"name": "Oleg", "age": 17},
    {"name": "Ivan", "age": 30},
    {"name": "Olga", "age": 19}
]

print(list(filter(lambda x: x["age"] > 18 and x["name"].startswith("O"), users)))
