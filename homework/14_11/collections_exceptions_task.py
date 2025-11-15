'''
Задание: Менеджер Учебной Школы с Кастомными Исключениями
1. Класс Student (можно использовать dataclass)
Поля:
name: str
age: int
grades: dict[str, list[int]] — ключ — предмет, значение — список оценок

Методы:
add_grade(subject: str, grade: int) — добавить оценку; если оценка не от 1 до 5, выбросить кастомное исключение InvalidGradeError.
average_grade(subject: str = None) — средняя оценка по предмету или по всем предметам, если subject=None.
subjects() — вернуть сет всех предметов студента.

2. Класс Group
Хранит список студентов (list[Student])

Методы:

add_student(student: Student) — добавить студента
remove_student(name: str) — удалить студента по имени; если студента нет, выбросить StudentNotFoundError.
find_student(name: str) — вернуть объект студента; если нет, выбросить StudentNotFoundError.
all_students() — вернуть сет имен студентов
top_student(subject: str = None) — вернуть студента с наивысшей средней оценкой

3. Класс School
Хранит группы: groups = {group_name: Group}

Методы:
add_group(name: str, group: Group)
get_group(name: str) — вернуть объект группы; если нет, выбросить GroupNotFoundError.
all_groups() — сет всех названий групп
school_average(subject: str = None) — средняя оценка по всем студентам школы по предмету или по всем предметам

'''