import requests

def get_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    if response.status_code != 200:
        print('Ошибка! Сервер не отвечает')
        return []
    users = response.json()
    return users

def check_users(users):
    problems = []
    for user in users:
        user_id = user.get('id', 'неизвестно')
        name = user.get('name', '')
        email = user.get('email', '')
        if name == '' or email == '':
            problems.append('У пользователя ' + str(user_id) + ' нет имени или емейла')
    return problems

def main():
    print('Начинаю проверку...')
    users = get_users()
    if len(users) == 0:
        print('Данные не получены, проверьте интернет')
        return
    print('Пришло пользователей: ' + str(len(users)))
    errors = check_users(users)
    if len(errors) == 0:
        print('Всё хорошо, ошибок нет!')
    else:
        print('Найдены проблемы:')
        for error in errors:
            print(' - ' + error)
    print('\nПример данных:')
    for user in users[:3]:
        print(user['name'] + ' - ' + user['email'])

if __name__ == '__main__':
    main()
