"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:
    """Класс, описывающий студента"""

    def __init__(self, name: str, course: int):
        """Инициализация полей студента"""
        self.name = name    # Имя (строка)
        self.course = course  # Курс (целое число)


# Создаем два экземпляра класса Student строго по условию
student_1 = Student(name="Алиса", course=3)
student_2 = Student(name="Маргарита", course=2)


# код для проверки 
print(student_1.name, student_1.course)  # >>> Алиса 3
print(student_2.name, student_2.course)  # >>> Маргарита 2
