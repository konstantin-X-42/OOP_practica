import pytest

from src.user import User
from src.task import Task


# создаём для проверки: users_count и all_tasks_count
@pytest.fixture
def first_user():
    return User(username="User",
                email="user@mail.ru",
                first_name="User",
                last_name="Userov",
                task_list=[Task("Купить огурцы", "Купить огурцы для салата"),
                           Task("Купить помидоры", "Купить помидоры для салата"),
                           ],
                )

@pytest.fixture
def second_user():
    return User(username="John",
                email="john@mail.ru",
                first_name="John",
                last_name="Doe",
                task_list=[Task("Купить огурцы", "Купить огурцы для салата"),
                           Task("Купить помидоры", "Купить помидоры для салата"),
                           Task("Купить лук","Купить лук для салата"),
                           ],
                )

# фикстура задач

@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="12.06.2026")


