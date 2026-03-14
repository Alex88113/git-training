import pytest

from processing_user_data import User

@pytest.mark.parametrize("name, age, email, password, expected_result", [
    ("Sasha", 18, 'sanya.kucheryavyh84@bk.ru', '1212121212', {
        'name': 'Sasha', 'age': 18,
        'email': 'sanya.kucheryavyh84@bk.ru',
        'password': '1212121212'
    })
])

def test_print_info(name, age, email, password, expected_result):
    user = User(name, age, email, password)
    assert user.print_data_user() == expected_result


@pytest.mark.parametrize("name, age, email, password, expected_result", [
    ('  misha', 19, 'misha.crashavchick8@.com', '23323232323', 'Misha'),
('  dima', 20, 'dima.crashavchick8@.com', '23323232323', 'Dima')
])

def test_process_name(name, age, email, password, expected_result):
    user = User(name, age, email, password)
    assert user.processing_name() == expected_result