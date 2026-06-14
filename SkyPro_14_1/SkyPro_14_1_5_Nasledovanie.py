# ================================
# -------- НАСЛЕДОВАНИЕ ---------
# ================================


class Employee:
    """Класс сотрудника, который обладает общими свойствами и методами"""

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def work(self):
        print("Do some work")

    def go_to_vacation(self):
        print("Go to vacation")


# При наследовании указываем имя родительского класса в круглых скобках (Employee) при объявлении дочернего класса
class Developer(
    Employee
):  # <--- Developer наследует ВСЕ свойства и методы класса Employee
    """Дочерний класс от класса работника, который принимает и переопределяет некоторые свойства"""

    def __init__(self, name: str, surname: str, language: str, level: str):

        # super() — это встроенная функция Python, находит класс-родитель (Employee)
        # super() вызывает конструктор родительского класса (Employee) и передает туда name и surname
        super().__init__(name, surname)

        # Дополнительные свойства, которые есть только у разработчика
        self.language = language
        self.level = level

    def work(self):
        # Переопределенный метод (полиморфизм)
        print("Write code")

    def read_documentation(self):
        print("Read documentation")


if __name__ == "__main__":
    dev = Developer(name="Ivan", surname="Ivanov", language="Python", level="Junior")

    print(dev.name)  # Выведет: Ivan (унаследовано от Employee)
    dev.go_to_vacation()  # Выведет: Go to vacation (унаследовано от Employee)
    dev.work()  # Выведет: Write code (собственный переопределенный метод)
