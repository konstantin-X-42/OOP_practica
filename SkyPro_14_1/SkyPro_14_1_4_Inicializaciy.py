# ================================
# ---- ИНИЦИАЛИЗАЦИЯ __init__ ----
# ================================

class Employee:
    """Класс для представления сотрудника."""
    name: str
    surname: str
    email: str
    pay: int

    def __init__(self, name, surname, pay):
        """Метод для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра."""
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f'{self.name}.{self.surname}@email.com'

    def work(self):
        pass


emp_1 = Employee(name='Ivan', surname='Ivanov', pay=50_000)

print(emp_1.name)
print(emp_1.surname)
print(emp_1.pay)
print(emp_1.email)