import math

"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника
  и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
  если это квадрат, и False в противном случае
"""


class Rectangle:
    """Класс, описывающий прямоугольник"""

    def __init__(self, width: float | int, height: float | int):
        """Конструктор, принимающий ширину и высоту прямоугольника"""

        self.width = width  # присваивает значение аргумента width свойству (атрибуту) self.width конкретного объекта
        self.height = height

    def area(self) -> int | float:
        """Метод, возвращающий площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self) -> int | float:
        """Метод, возвращающий периметр прямоугольника"""
        return 2 * (self.width + self.height)

    @classmethod
    # -> "Rectangle": аннотация возвращаемого значения. Метод вернет готовый объект класса Rectangle.
    # Строчные кавычки нужны, так как сам класс внутри себя еще полностью не объявлен.
    def from_diagonal(
        cls, diagonal: float | int, aspect_ratio: float | int
    ) -> "Rectangle":
        """Класс-метод, создающий прямоугольник по диагонали и соотношению сторон"""

        # Используем теорему Пифагора: d^2 = w^2 + h^2, где w = h * aspect_ratio
        # d^2 = (h * aspect_ratio)^2 + h^2 = h^2 * (aspect_ratio^2 + 1)

        # math.sqrt(...) — функция из модуля math, извлекает квадратный корень из всего что внутри скобок
        # ** означают возведение в степень ** 2 - в квадрат

        height = diagonal / math.sqrt(aspect_ratio**2 + 1)
        width = height * aspect_ratio
        return cls(width, height)

    # Статический метод (@staticmethod) — ничего не знает ни о классе, ни об объекте.
    # Просто принимает аргументы, делает расчет и возвращает результат.
    @staticmethod
    def is_square(width: int | float, height: int | float):
        return width == height


# код для проверки
rectangle = Rectangle(4, 5)
# площадь
print(rectangle.area())  # >>> 20
# периметр
print(rectangle.perimeter())  # >>> 18

rectangle2 = Rectangle.from_diagonal(5, 2)
# прямоугольник по диагонали и соотношению сторон
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

# выводит результат по заданным параметрам квадрат - True
print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
