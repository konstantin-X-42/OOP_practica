"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в него будет производиться запись логов;
- __call__(self, message): магический метод, позволяет использовать объект класса Logger как функцию,
  принимающую сообщение и записывающую его в файл.
"""


class Logger:
    """Класс для записи логов в текстовый файл"""
    def __init__(self, filename: str):
        """Конструктор, принимающий имя файла для логов"""
        self.filename = filename


    def __call__(self, message: str) -> None:
        """Магический метод, позволяющий использовать объект как функцию.
        Принимает сообщение и дописывает его в файл.
        """
        # Режим 'a' (append) открывает файл для добавления записей в конец
        with open(self.filename, mode="a", encoding="utf-8") as file:
            file.write(message + "\n")


# код для проверки 
logger = Logger("log.txt")
logger("This is a test message.")
