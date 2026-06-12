# -----------------------------------------------------------------------
# установка библиотеки pytest
# poetry add pytest --group dev
# -----------------------------------------------------------------------
# запуск тестов
# poetry run python -m pytest SkyPro_14_1/tests_14_1_6/test_SkyPro_14_1_6_Testirovanie.py
# -----------------------------------------------------------------------

import pytest

from SkyPro_14_1.SkyPro_14_1_6_Testirovanie import Employee


@pytest.fixture()
def employee_ivan():
    return Employee(name='Ivan', surname='Ivanov', pay=50000)


def test_init(employee_ivan):
    assert employee_ivan.name == 'Ivan'
    assert employee_ivan.surname == 'Ivanov'
    assert employee_ivan.email == 'Ivan.Ivanov@email.com'
    assert employee_ivan.pay == 50000


def test_is_work(employee_ivan):
    assert not employee_ivan.is_work       # или так: assert employee_ivan.is_work == False
    employee_ivan.work()
    assert employee_ivan.is_work           # или так: assert employee_ivan.is_work == True


def test_is_work_not_vacation(employee_ivan):
    employee_ivan.go_to_vacation()
    employee_ivan.work()
    assert not employee_ivan.is_vacation   # или так: assert employee_ivan.is_vacation == False


def test_is_vacation(employee_ivan):
    assert not employee_ivan.is_vacation   # или так: assert employee_ivan.is_vacation == False
    employee_ivan.go_to_vacation()
    assert employee_ivan.is_vacation       # или так: assert employee_ivan.is_vacation == True


def test_is_vacation_not_work(employee_ivan):
    employee_ivan.work()
    employee_ivan.go_to_vacation()
    assert not employee_ivan.is_work       # или так: assert employee_ivan.is_work == False