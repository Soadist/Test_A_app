# Tracker
#### Основные технологии:
Python 3.9.5
Django 3.2.6
Django REST Framework 3.12.4
### Описание
API для мобильного приложения фитнес трекера.
### Алгоритм регистрации пользователей:
Пользователь регистрируется в приложении с помощью электронной почты с подтверждением адреса.
#### Команда клонирования репозитория:
```bash
git clone https://v.gitlab.getsarafan.com/a.polyanchev/app.git
```
#### Установка дополнительных библиотек:
```bash
- pip install -r requirements.txt
```
#### Запуск сервера:
```bash
python manage.py runserver
```
#### Первоначальная настройка Django:
```bash
- python manage.py makemigrations --noinput
- python manage.py migrate --noinput
```
#### Создание суперпользователя:
```bash
- python manage.py createsuperuser
```
#### Заполнение .env:
Чтобы добавить переменную в .env необходимо открыть файл .env в директории проекта ./test_project/ и поместить туда переменную в формате имя_переменной=значение.</br>
Пример .env файла:
```.env
DB_ENGINE=my_db
DB_NAME=db_name
POSTGRES_USER=my_user
POSTGRES_PASSWORD=my_pass
DB_HOST=db_host
DB_PORT=db_port
DJANGO_SECRET_KEY=django_secret
```
#### Superuser pass&email:
email: admin@example.com</br>
pass: admin</br>

### Основные endpoint'ы:
Все запросы, требующие авторизации, должны передаваться с ключом Authorization: Token \<Token\> в заголовке запроса.</br>

#### Регистрация пользователя:
POST /api/users/</br>
Пример тела запроса:</br>
```json
{
    "email": "test_1@example.com",
    "username": "test_1",
    "password": "test_1",
    "first_name": "test_1",
    "last_name": "test_1"
}
```

#### Активация пользователя:
POST /api/users/activation/</br>
В заголовке передаются ключи uid и token с данными из email-сообщения со ссылкой для активации.</br>
Ссылка для активации пользователя в email-сообщении имеет вид http://domain.com/activate/{uid}/{token}/</br>

#### Получение токена авторизации:
POST /api/auth/token/login/</br>
В теле запроса передаются ключи 'password' c паролем и 'email' с email пользователя. </br>
В теле ответа передаётся ключ 'auth_token' с токеном авторизации.</br>
Не требуется авторизация.</br>

#### Удаление токена авторизации:
POST /api/auth/token/logout/</br>
Требуется авторизация.</br>

#### Добавление отчёта на сервер:
POST /api/reports/ </br>
Пример тела запроса в json:</br>
```json
{
    "start_datetime": "2021-07-30T12:53:30+03:00",
    "end_datetime": "2021-07-30T13:53:45+03:00",
    "activity_type": "running",
    "distance": 100,
    "calories": 2000
}
```
В теле ответа будет копия тела запроса при успешном добавлении, либо сообщение об ошибке.</br> 
Требуется авторизация.</br>

#### Получение списка отчётов для текущего пользователя:
GET /api/reports/</br>
Пример ответа в json:</br>
```json
[
    {
        "user": 1,
        "start_datetime": "2021-08-31T12:53:30+03:00",
        "end_datetime": "2021-08-31T13:53:45+03:00",
        "activity_type": "bike",
        "distance": 10,
        "calories": 1000
    },
    {
        "user": 1,
        "start_datetime": "2021-07-30T12:53:30+03:00",
        "end_datetime": "2021-07-30T13:53:45+03:00",
        "activity_type": "running",
        "distance": 100,
        "calories": 2000
    }
]
```
Требуется авторизация.</br>

#### Получение статистики по отчётам:
GET /api/reports/stats/</br>
Пример ответа в json:</br>
```json
{
    "count": 2,
    "total_calories": 3000,
    "total_distance": 110,
    "total_duration": "02:00:30"
}
```
Требуется авторизация.</br>

#### Получение статистики по отчётам за текущий день с агрегацией по часам:
GET /api/reports/stats/hourly/</br>
```json
[
    {
        "count": 1,
        "total_calories": 1000,
        "total_distance": 10,
        "total_duration": "01:00:15",
        "hour": 9
    }
]
```
Требуется авторизация.</br>

#### Получение статистики по отчётам за текущий месяц с агрегацией по дням:
GET /api/reports/stats/daily/</br>
```json
[
    {
        "count": 1,
        "total_calories": 1000,
        "total_distance": 10,
        "total_duration": "01:00:15",
        "day": 31
    }
]
```
Требуется авторизация.</br>

#### Автор:
Алексей Полянцев.
