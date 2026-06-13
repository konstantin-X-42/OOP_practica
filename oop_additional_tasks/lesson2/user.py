"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    def __init__(self, name: str, password: str):
        """Класс, описывающий пользователя с системой авторизации и прав

        защищенные атрибуты (с нижним подчеркиванием) - инкапсуляция данных"""
        self._name = name
        self._password = password  # присваивает значение аргумента password свойству (атрибуту) self.password конкретного объекта
        self._is_admin = False  # По умолчанию пользователь не админ
        self._is_logged_in = False  # Флаг состояния авторизации

    # Превращаем метод в свойство с помощью @property
    @property
    def name(self) -> str:
        """Свойство, которое возвращает имя пользователя"""
        return self._name

    # Превращаем метод в свойство с помощью @property
    # @property декоратор позволяет читать скрытое значение без скобок
    @property
    def password(self) -> str:
        """Свойство, возвращающее текущий пароль (обычно скрыто или хешировано)"""
        return self._password

    # @password.setter декоратор сеттер позволяет безопасно это значение перезаписывать (изменять) через обычный знак равенства =
    @password.setter
    def password(self, new_password: str) -> None:
        """Свойство-сеттер, которое позволяет изменить пароль пользователя"""
        if len(new_password) >= 4:  # Можно добавить базовую проверку длины
            self._password = new_password
        else:
            print("Пароль слишком короткий!")

    @property
    def is_admin(self) -> bool:
        """Свойство, которое возвращает, является ли пользователь администратором"""
        return self._is_admin

    # @is_admin.setter — декоратор-сеттер для свойства is_admin, используется, чтобы контролировать
    # и проверять процесс назначения пользователю прав администратора
    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        """Сеттер для изменения статуса администратора (управляет _is_admin)"""
        self._is_admin = value

    def login(self, password: str) -> bool:
        """Метод, который проверяет, соответствует ли введенный пароль паролю пользователя"""
        if self._password == password:
            self._is_logged_in = True
            print(f"Пользователь {self._name} успешно вошел в систему")
            return True
        else:
            print("Неверный пароль!")
            return False

    def logout(self) -> None:
        """Метод, который выходит из аккаунта пользователя (сбрасывает флаг _is_logged_in)"""
        if self._is_logged_in:
            self._is_logged_in = False
            print(f"Пользователь {self._name} вышел из аккаунта")
        else:
            print("Пользователь и так не залогинен")


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # >>> Alice
print(user1.password)  # >>> qwerty
print(user1.is_admin)  # >>> False

user1.password = "newpassword"
print(user1.password)  # >>> newpassword

# назначаем user1 администратором через сеттер (нет подчёркивания user1.is_admin)
# назначаем user1 администратором минуя сеттер (метод обхода user1._is_admin)
user1.is_admin = True
print(user1.is_admin)  # >>> True

user1.login("newpassword")  # >>> True
user1.logout()
# >>> Пользователь Alice успешно вошел в систему
# >>> Пользователь Alice вышел из аккаунта
