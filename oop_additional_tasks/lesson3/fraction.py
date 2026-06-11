import math

"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
  можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    """Класс, представляющий собой математическую дробь"""

# В этой строке мы не присваиваем значение атрибуту, потому что сначала обязаны выполнить валидацию
# (проверку на ошибку) [stem-calculative-problem-solving]. Если знаменатель равен нулю,
# то создавать дробь математически бессмысленно — программа всё равно упадет с ошибкой деления
# на ноль в будущем [stem-calculative-problem-solving].
# Поэтому логика конструктора работает как строгий охранник на входе.
    def __init__(self, numerator: float | int, denominator: float | int):
        """Конструктор, принимающий числитель и знаменатель дроби"""
        if denominator ==0:
            raise ValueError("Знаменатель не может быть равен нулю")

        # Находим наименьший общий делитель числителя и знаменателя
        common_divisor = math.gcd(numerator, denominator)
        # Сокращаем числитель и знаменатель перед сохранением
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor


    def __repr__(self):
        """Магический метод для технического представления объекта"""
        return f"fraction({self.numerator}, {self.denominator})"


    def __str__(self) -> str:
        """Магический метод для пользовательского отображения дроби"""
        return f"{self.numerator}/{self.denominator}"


    def __add__(self, other: "Fraction") -> "Fraction":
        """Магический метод, позволяющий складывать две дроби."""
        if not isinstance(other, Fraction):
            raise TypeError("Складывать можно только объекты класса Fraction")

        # Формула сложения дробей: (a/b) + (c/d) = (a*d + c*b) / (b*d)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)



# код для проверки 
fraction1 = Fraction(1, 2)
print(repr(fraction1))                         # >>> Fraction(1, 2)
print(str(fraction1))                          # >>> 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)                               # >>> 5/4
