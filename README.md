# Описание.

В данном проекте развернут API для небольшого проекта Yatube.

Для аутентификации использованы JWT-токены.

# Установка.

Cклонируйте репозиторий
```
git clone
```
Создайте виртуальное окружение
```
python3 -m venv venv
```
Запустите виртуальное окружение
```
. venv/bin/activate
```
Обновите PIP.
```
python3 -m pip install --upgrade pip
```
Установить зависимости
```
pip install -r requirements.txt
```
Выполните миграцию
```
python3 manage.py migrate
```
Запустите проект
```
python3 manage.py runserver
```

# Пример

Чтобы получить список всех постов отправьте POST запрос на эндпоинт localhost:8000/api/v1/posts
