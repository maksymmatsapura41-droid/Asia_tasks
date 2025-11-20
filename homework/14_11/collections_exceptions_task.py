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
'''

class InvalidGradeError(Exception):
    pass
    
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    grades: dict = field(default_factory=dict)

    def add_grade(self, subject: str, grade: int):
        if grade not in range(1, 6):
            raise InvalidGradeError(f'Available grade range is 1 to 5')
        self.grades.setdefault(subject, []).append(grade)
        # print(self.grades)
    
    def average_grade(self, subject: str = None):
        if subject and subject in self.grades.keys():
            sbj_grades = self.grades[subject]
            return (sum(sbj_grades) / len(sbj_grades), len(sbj_grades))
        
        total_sum = 0
        total_num = 0
        for item in self.grades.values():
            total_sum += sum(item)
            total_num += len(item)
        return ((total_sum / total_num), total_num)
    
    @property
    def subjects(self):
        return set(sbj for sbj in self.grades.keys())

std1 = Student('Bob', 18)
std1.add_grade('Math', 3)
std1.add_grade('Math', 5)
std1.add_grade('Math', 4)
# std1.add_grade('Math', 6)
std1.add_grade('Biology', 4)

print('Student 1 Subjects:', std1.subjects)
print('Student 1 Average Grade:', std1.average_grade()[0])
# print(std1.average_grade('Math'))

std2 = Student('Mary', 19)
std2.add_grade('Math', 1)
std2.add_grade('Literature', 4)
std2.add_grade('Biology', 1)
print('Student 2 Subjects:', std2.subjects)
print('Student 2 Average Grade:', std2.average_grade()[0])

'''
2. Класс Group
Хранит список студентов (list[Student])

Методы:

add_student(student: Student) — добавить студента
remove_student(name: str) — удалить студента по имени; если студента нет, выбросить StudentNotFoundError.
find_student(name: str) — вернуть объект студента; если нет, выбросить StudentNotFoundError.
all_students() — вернуть сет имен студентов
top_student(subject: str = None) — вернуть студента с наивысшей средней оценкой
'''
class StudentNotFoundError(Exception):
    pass

class Group:
    def __init__(self):
        self.students = []
        
    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        target = self.find_student(name)
        self.students.remove(target)

    def find_student(self, name: str):
        for person in self.students:
            if person.name == name:
                return person
        raise StudentNotFoundError('Student not found')        

    def all_students(self):
        return [person.name for person in self.students]
    
    def top_student(self, subject: str = None):
        top_average_grade = 1
        top_student = None
        
        for person in self.students:
            person_average = person.average_grade(subject)[0]
            if person_average > top_average_grade:
                top_average_grade = person_average
                top_student = person.name
            else:
                continue

        return (top_student, top_average_grade)


group1 = Group()
group1.add_student(std1)
group1.add_student(std2)
print('Group 1 Students:', group1.all_students())
# group1.remove_student('Bob')
# print(group1.all_students())
print(group1.top_student('Literature')) # fails if not all students have the same subjects

'''
3. Класс School
Хранит группы: groups = {group_name: Group}

Методы:
add_group(name: str, group: Group)
get_group(name: str) — вернуть объект группы; если нет, выбросить GroupNotFoundError.
all_groups() — сет всех названий групп
school_average(subject: str = None) — средняя оценка по всем студентам школы по предмету или по всем предметам

'''
class GroupNotFoundError(Exception):
    pass

class School:
    def __init__(self):
        self.groups = {}

    def add_group(self, name: str, group: Group):
        self.groups[name] = group
    
    def get_group(self, name: str):
        if name not in self.groups.keys():
            raise GroupNotFoundError('Group not found')
        return self.groups[name]
    
    def all_groups(self):
        return self.groups.keys()

    # среднее_всех_оценок = sum(среднее_студента × количество_оценок) / sum(количество_оценок)
    def school_average(self, subject: str = None):
        grade_summary = 0
        total_marks = 0
        for group in self.groups.values():
            for student in group.students:
                average, number_of_marks = student.average_grade(subject)
                grade_summary += average * number_of_marks
                total_marks += number_of_marks
        print(grade_summary, total_marks)
        return round(grade_summary / total_marks, 2)

school40 = School()
school40.add_group('Group 1', group1)
# print(school40.get_group('Group 1'))
print(school40.all_groups())
print(school40.school_average('Math'))
print(school40.school_average())
