"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, возвращает текущий баланс счета
- deposit(self, amount): метод, позволяет внести деньги насчет
- withdraw(self, amount): метод, позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    """Класс, описывающий работу банковского счета"""

    def __init__(self, balance: int | float):
        """Конструктор, принимающий начальный баланс счета.

        Используем защищенный атрибут с нижним подчеркиванием,
        чтобы с ним работал декоратор @property

        Защищенный атрибут с нижним подчеркиванием (self._balance) используется для
        инкапсуляции — это базовый принцип ООП, который защищает данные внутри объекта
        от случайной порчи извне"""

        self._balance = balance


    # @property это декоратор. Он говорит интерпретатору Python: «Сделай так, чтобы методы, написанные ниже,
    # можно было вызывать без скобок, как будто это простое свойство объекта».
    @property
    def balance(self) -> float | int:
        """Свойство, возвращающее текущий баланс счета"""
        return self._balance


    #  Создаём свой собственный метод (метод класса), который назвали deposit
    def deposit(self, amount: float | int):
        """Метод, позволяющий внести деньги на счет"""
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма пополнения должна быть больше 0")


    #  Создаём свой собственный метод (метод класса), который назвали withdraw
    def withdraw(self, amount: float | int):
        """Метод, позволяющий снять деньги со счета"""
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств или указана неверная сумма")


    #  Создаём свой собственный метод (метод класса), который назвали close
    def close(self) -> float | int:
        """Метод, который закрывает счет и возвращает оставшиеся на нем деньги"""
        remaining_balance = self._balance
        self._balance = 0   # Счёт обнуляется после закрытия
        return remaining_balance



# код для проверки 
account = BankAccount(1000)
print(account.balance)  # >>> 1000

account.deposit(500)
print(account.balance)  # >>> 1500

account.withdraw(200)
print(account.balance)  # >>> 1300

account.close()
print(account.balance)  # >>> 0
