# Описание проекта Api_Yatube

## Описание:
Проект представляет собой социальную сеть для публикации личных дневников. Реализован API для всех моделей приложения. По запросу можно просмотреть все записи автора. Пользователи могут делать запросы к чужим страницам, комментировать записи различных авторов, подписываться на них. API доступен только аутентифицированным пользователям. Реализованы возможность поиска и фильтрации данных. Добавлена пагинация ответов. Модели написаны с использованием вьюсетов.

## Технологии:
Python 3.9, Django 2.2 LTS, Django ORM, Django REST Framework (DRF), REST API, SQLite3, CSRF, Paginator, Simple-JWT, Djoser

<details>
<summary><h2>Как запустить проект:</h2></summary>

### *Клонируйте репозиторий:*
```
git clone https://github.com/EgorGushin/api_final_yatube.git
```

### *Установите и активируйте виртуальное окружение:*
Win:
```
python -m venv venv
venv/Scripts/activate
```

Mac:
```
python3 -m venv venv
source venv/bin/activate
```

### *Установите зависимости из файла requirements.txt:*
```
pip install -r requirements.txt
```

### *Перейдите в директорию с файлом manage.py, создайте и примените миграции (python3 для Mac):*
```
cd backend
python manage.py makemigrations
python manage.py migrate
```

### *Создайте суперпользователя (python3 для Mac):*
```
python manage.py createsuperuser
```

### *Запустите сервер (python3 для Mac):*
```
python manage.py runserver
```

## Настроены такие эндпоинты:

```
    api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
    api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
    api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
    api/v1/groups/ (GET): получаем список всех групп.
    api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
    api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или 
    создаём новый, указав id поста, который хотим прокомментировать.
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или 
    удаляем комментарий по id у поста с id=post_id.
```
## Примеры запросов:

```
- Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/
```
- Пример ответа:
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
} 
```
- Пример GET-запроса: получаем информацию о группе.
GET .../api/v1/groups/2/

- Пример ответа:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```
</details>


## Разработчик:
[Егор Гущин](https://github.com/EgorGushin)
