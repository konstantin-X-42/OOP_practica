# ================================
# --------- ПОЛИМОРФИЗМ ----------
# ================================


class JavaDeveloper:
    """Класс для представления Java-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Java-разработчике."""
        print(f"Я {self.name} - Java разработчик.")

    def code(self):
        """Метод для программирования на языке Java."""
        print("class Привет мир { public static void main(String[] args)...")


class PythonDeveloper:
    """Класс для представления Python-разработчиков."""

    def __init__(self, name):
        """Метод, инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Python-разработчике."""
        print(f"Я {self.name} - Python разработчик.")

    def code(self):
        """Метод для программирования на языке Python."""
        print("print('Привет мир')")


# --- ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА ---
if __name__ == "__main__":
    # Создаем список из разработчиков разных направлений
    developers = [JavaDeveloper("Ivan"), PythonDeveloper("Petr")]

    # Полиморфизм в действии: вызываем одинаковые методы в одном цикле, но каждый объект реагирует по-своему!
    for dev in developers:
        dev.info()
        dev.code()
