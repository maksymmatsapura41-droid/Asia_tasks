'''
Задание: Docker Registry (Image → Repository → Registry)
Реализовать систему управления Docker-образами с использованием dataclass и композиции классов.
1. Dataclass Image
Поля:
name: str
tag: str
size_mb: int
created_at: datetime

Методы:
full_name() — возвращает строку "<name>:<tag>"
age_days() — возвращает возраст образа в днях
В __post_init__ проверить, что size_mb > 0
'''

from dataclasses import dataclass, field
from datetime import datetime
from itertools import chain  

@dataclass
class Image:
    name: str
    tag: str
    size_mb: int
    created_at: datetime

    def full_name(self):
        return f'{self.name}:{self.tag}'
    
    def age_days(self):
        current_datetime = datetime.now()
        return (current_datetime - self.created_at).days
    
    def __post_init__(self):
        if self.size_mb <= 0:
            raise ValueError("Size can not be negative or zero")        



'''
2. Класс Repository
Поля:
name: str
список образов (list[Image])

Методы:
add(image: Image) — добавить образ
remove(name: str, tag: str) — удалить образ по имени и тегу
find(name: str) — вернуть список образов с указанным именем
cleanup(max_age_days: int) — удалить образы старше указанного количества дней
total_size() — суммарный размер образов
list_all() — список строк вида: "<name>:<tag> | <size_mb> MB | created: <дата>"
'''

@dataclass
class Repository:
    name: str
    records: list = field(default_factory=list)

    def add(self, image: Image):
        self.records.append(image)
    
    def remove(self, name: str, tag: str):
        for item in self.records:
            if item.name == name and item.tag == tag:
                self.records.remove(item)
    
    def find(self, name: str):
        return [item for item in self.records if item.name == name]
    
    def cleanup(self, max_age_days: int):
        to_remove = []
        for item in self.records:
            print(item.age_days(), max_age_days)
            if item.age_days() > max_age_days:
                to_remove.append(item)
                
        for item in to_remove:
            self.records.remove(item)
    
    def total_size(self):
        total_size = 0
        for item in self.records:
            total_size += item.size_mb
        return total_size
    
    def list_all(self):
        return [f'{item.name}:{item.tag} | {item.size_mb} MB | created: {item.created_at}' for item in self.records]

'''
3. Класс Registry
Поля:
словарь репозиториев: repo_name → Repository

Методы:
add_repo(repo: Repository) — добавить репозиторий
get_repo(name: str) — вернуть репозиторий или None
total_size() — суммарный размер всех образов во всех репозиториях
list_all() — вернуть список всех образов всех репозиториев в формате:
 "<repo_name> | <image_full_name> | <size_mb> MB | created: <дата>"
'''
@dataclass
class Registry:
    records: dict = field(default_factory=dict)

    def add_repo(self, name: str, repo: Repository):
        self.records[name] = repo
    
    def get_repo(self, name: str):
        return self.records.get(name)

    def total_size(self):
        total_size = 0
        for item in self.records.values():
            total_size += item.total_size()
        return total_size

    def list_all(self):
        return [f'{key} | {value.list_all()}' for key, value in self.records.items()] # how to flatted the list {value.list_all()} ?

'''
4. Тестовый сценарий
Создать несколько образов: backend:v1, backend:v2, frontend:v1, worker:v1
Создать два репозитория: backend и frontend
Добавить образы в соответствующие репозитории
Создать Registry и добавить оба репозитория

Вывести:
все образы в репозиториях
суммарный размер реестра
удалить старые образы через cleanup и показать результат
'''

im1 = Image('backend', 'v1', 50, datetime(2025, 11, 10, 12, 00, 45))
im2 = Image('backend', 'v2', 55, datetime(2025, 11, 18, 12, 30, 45))
im3 = Image('frontend', 'v1', 15, datetime(2024, 11, 18, 12, 30, 45))
im4 = Image('worker', 'v1', 50, datetime(2025, 10, 18, 12, 30, 45))
print(im1.age_days())

backend = Repository('Backend')
backend.add(im1)
backend.add(im2)

frontend = Repository('Frontend')
frontend.add(im3)
frontend.add(im4)
print(frontend.list_all())
print(backend.list_all())

registry = Registry()
registry.add_repo(backend.name, backend)
registry.add_repo(frontend.name, frontend)

print(registry.list_all())
print(registry.total_size())

print('Frontend before cleanup', frontend.list_all())
frontend.cleanup(10)
print('Frontend after cleanup', frontend.list_all())


print('Backend before cleanup', backend.list_all())
backend.cleanup(10)
print('Backend after cleanup', backend.list_all())