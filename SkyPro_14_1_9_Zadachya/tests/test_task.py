def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.discription == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "12.06.2026"
