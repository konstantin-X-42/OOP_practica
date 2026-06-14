"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
  его можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""


class MyList:
    """Класс-обёртка над стандартным списком для изучения магических методов"""

    def __init__(self, data: list):
        """Конструктор, принимающий список элементов"""
        # Превращаем входные данные в настоящий список, чтобы избежать мутаций
        self.data = list(data)

    def __repr__(self) -> str:
        """Магический метод для технического представления объекта"""
        return f"MyList({self.data})"

    def __str__(self) -> str:
        """Магический метод для пользовательского отображения списка"""
        return str(self.data)

    def __len__(self) -> int:
        """Магический метод, возвращающий длину списка"""
        return len(self.data)

    def __add__(self, other: "MyList" | list) -> "MyList":
        """Магический метод для сложения списков.
        Возвращает новый объект класса MyList.
        """
        if isinstance(other, MyList):
            # Если складываем два объекта MyList
            new_data = self.data + other.data
        elif isinstance(other, list):
            # Если к MyList прибавляем обычный список [1, 2, 3]
            new_data = self.data + other
        else:
            raise TypeError("Складывать можно только с MyList или со списком (list).")

        return MyList(new_data)


# код для проверки
my_list1 = MyList([1, 2, 3])
print(repr(my_list1))  # >>> MyList([1, 2, 3])
print(str(my_list1))  # >>> [1, 2, 3]
print(len(my_list1))  # >>> 3

my_list2 = MyList([4, 5, 6])
my_list3 = my_list1 + my_list2
print(my_list3)  # >>> [1, 2, 3, 4, 5, 6]
