"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self):
        print("Прогулка!")


class Dog(Animal):

    def bark(self):
        print("Гав!")


class Cat(Animal):

    def meow(self):
        print("Мяу!")


animals = [Dog("Dog1"), Dog("Dog2"), Cat("Cat1"), Dog("Dog3")]

for animal in animals:
    # Должно выводиться Гав или Мяу в зависимости от того какой класс

    # Проверяем класс животного и вызываем соответствующий метод
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()


