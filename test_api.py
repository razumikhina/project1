import requests
import pytest

URL = 'https://jsonplaceholder.typicode.com/users'

def test_status():
    response = requests.get(URL)
    assert response.status_code == 200, 'Сервер не отвечает!'

def test_not_empty():
    response = requests.get(URL)
    users = response.json()
    assert len(users) > 0, 'Пришёл пустой список'

def test_has_name_and_email():
    response = requests.get(URL)
    users = response.json()
    for user in users:
        assert 'name' in user, 'Нет поля name'
        assert user['name'] != '', 'Пустое поле name'
        assert 'email' in user, 'Нет поля email'
        assert user['email'] != '', 'Пустое поле email'

def test_count_is_10():
    response = requests.get(URL)
    users = response.json()
    assert len(users) == 10, 'Должно быть 10 пользователей, а пришло ' + str(len(users))
