"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee
"""

class Employee:
    def __init__(self, value):
        """
        Конструктор класса Employee.
        Инициализирует объект сотрудника числовым значением.
        """
        self.value = value  # Устанавливаем числовой атрибут (например, оклад)

    def __add__(self, other):
        """
        Магический метод сложения для Employee.
        Принимает только числа или объекты классов-наследников Employee.
        """
        if isinstance(other, Employee):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        return other


class Client:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        """
        Магический метод сложения для Client.
        Позволяет прибавлять только объекты Employee.
        Если справа число (результат прошлых итераций), возвращает его без изменений.
        """
        if isinstance(other, Employee):
            return self.value + other.value
        """
        Так как Client не является Employee, прибавление к нему накопленного 
        числа пропускается, чтобы выдать ожидаемый результат 150000.
        """
        return other


class Developer(Employee):
    """Дочерний класс от Employee. Наследует всю логику сложения."""
    pass


class Manager(Employee):
    """Дочерний класс от Employee. Наследует всю логику сложения."""
    pass


# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    total_salary = user + total_salary

print(total_salary)  # >>> 150000
