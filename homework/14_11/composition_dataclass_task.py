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


3. Класс Registry
Поля:
словарь репозиториев: repo_name → Repository


Методы:
add_repo(repo: Repository) — добавить репозиторий
get_repo(name: str) — вернуть репозиторий или None
total_size() — суммарный размер всех образов во всех репозиториях
list_all() — вернуть список всех образов всех репозиториев в формате:
 "<repo_name> | <image_full_name> | <size_mb> MB | created: <дата>"


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