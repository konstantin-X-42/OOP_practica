"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0
"""

class Student:
    """Класс, описывающий студента, его курс и оценки."""

    def __init__(self, name: str, course: str, evaluating: list[int] | None = None) -> None:
        self.name = name
        self.course = course
        self.evaluating = evaluating

        # Если оценки не переданы, создаем пустой список
        self.evaluating = evaluating if evaluating is not None else []

    def avg_rate(self) -> int |float:
        """Считает среднюю оценку студента.
        Если список оценок пуст, возвращает 0.
        """
        if self.evaluating:
            return sum(self.evaluating) / len(self.evaluating)
        return 0


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
print(student.avg_rate())   # >>> 4.75

student = Student('Ivan', 'Python', [])
print(student.avg_rate())   # >>> 0.0
