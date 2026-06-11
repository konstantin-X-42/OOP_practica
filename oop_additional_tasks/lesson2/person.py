from datetime import datetime
"""Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""


class Person:
    """Класс, описывающий человека"""

    def __init__(self, name, age):
        """Конструктор, принимающий имя и возраст человека"""
        self.name = name
        self.age = age

    def display(self) -> None:
        """Метод, выводящий на экран имя и возраст человека"""
        print(f"Имя: {self.name}, Возраст: {self.age}")


# Декораторы @classmethod и @staticmethod меняют поведение методов класса. Они позволяют
# вызывать методы напрямую через имя класса, вообще не создавая конкретный объект (экземпляр) через __init__.

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """Класс-метод, вычисляющий возраст по году рождения и возвращающий объект Person

        .now() метод запрашивает у ОС компьютера текущую дату и точное время до миллисекунд
        .year — обращение к конкретному свойству (атрибуту) полученного объекта даты,
        «отрезает» всё лишнее забирает только цифры года"""

        current_year = datetime.now().year
        age = current_year - birth_year

        # Создаем и возвращаем новый объект класса Person (cls)
        # Переменная cls (сокращение от class) — это ссылка на сам класс, внутри которого находимся
        # Запись cls(name, age) — это абсолютно то же самое, что и Person(name, age)
        return cls(name, age)

    @staticmethod
    def is_adult(age: int):
        """Статический метод, проверяющий совершеннолетие (18 лет и старше)"""
        return age >= 18


# код для проверки 
person1 = Person("John", 28)
person1.display()                                               # >>> John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
person2.display()                                               # >>> Mike is 26 years old

print(Person.is_adult(20))                                      # >>> True
print(Person.is_adult(15))                                      # >>> False

# В консоль:
# >>> Имя: John, Возраст: 28
# >>> Имя: Mike, Возраст: 31
# >>> True
# >>> False