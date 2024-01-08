# *Проект "Атомные привычки"*

В 2018 году Джеймс Клир написал книгу «Атомные привычки»,
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Заказчик прочитал книгу, впечатлился и обратился с запросом реализовать трекер полезных привычек.

Тут реализована бэкенд-часть SPA веб-приложения.
Также представлен API-уровень для облегчения работы.

### Данный проект реализует: 
- создатель привычки
- место, в котором необходимо выполнять привычку
- время, когда необходимо выполнять привычку
- действие, которое представляет из себя привычка
- привычка, которую можно привязать к выполнению полезной привычки
- привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных
- периодичность выполнения привычки для напоминания в днях
- чем пользователь должен себя вознаградить после выполнения
- время, которое предположительно потратит пользователь на выполнение привычки
- привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки

### *Установка*

1. Установите Python 3.11 и выше

2. Создайте папку, куда будете клонировать проект

3. Скачайте репозиторий проекта:
   git clone https://github.com/andre059/project_django_kursach_7

4. Установите виртуальное окружение env python -m venv env :
   активируйте его env\Scripts\activate.ps1

5. Установите зависимости из файла requirements.txt:
   pip install -r requirements.txt

6. Настройте файл settings.py находящийся в папке config: 
    - *DATABASES_NAME = Название папки куда вы клонировали проект*
    
    - *DATABASES_USER = Переменная, которая должна содержать имя пользователя для подключения к базе данных PostgreSQL*
    
    - *DATABASES_PASSWORD = Пароль к вашей базе данных*
    
    - *SECRET_KEY = 'тут должен быть ваш секретный ключь'*
    
    - *CUR_API_KEY = 'Доступа к сервису с курсами валют'*
    
    - *STRIPE_SECRET_KEY = 'Секретный ключ Stripe API используется для аутентификации запросов и обеспечения безопасности при передаче платежных данных, ключь начинается на sk_test'*
    
    - *EMAIL_HOST_USER ='Значение этой переменной должно быть установлено на адрес электронной почты, который вы хотите использовать для отправки писем'*
    
    - *EMAIL_HOST = 'Адрес SMTP-сервера, который будет использоваться для отправки электронных писем из приложения'*
    
    - *EMAIL_HOST_PASSWORD ='Пароль для учетной записи электронной почты, используемой для отправки электронных писем с помощью SMTP'*
    
    - *TELEGRAM_TOKEN = 'Телеграм токен'*
    
    - *CSU_SET_PASSWORD = 'Пароль для файла csu.py'Запустите проекpython manage.py runserverДоступ к веб-интерфейсОткройте браузер и перейдите по адресу http://localhost:8000.


### Стек технологий использованный в проекте:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)


### Реализованный Функционал
- Настроен CORS.
    - CORS_ALLOWED_ORIGINS
    - CSRF_TRUSTED_ORIGINS
- Настроена интеграция с Telegram ботом. services.py
- Реализована пагинацию(и перенесена в settings.py).
    - 'DEFAULT_PAGINATION_CLASS'
- Использованы переменные окружения.
    - Поместите все пароли, токены доступа и другие секреты в файл .env в корне каталога проекта. 
- Описаны модели.
    - Habit
    - User
- реализованы эндпоинты.
    - habit/create/
    - habit/
    - habit/update/<int:pk>/
    - habit/delete/<int:pk>/
    - user-habit/
    - user(UserViewSet)
    - token/
    - token/refresh/
- Валидаторы.
    - TimeToExecuteValidator
    - RelatedHabitAwardValidator
    - RelatedHabitSignPleasantHabitValidator
    - SignPleasantHabitHabitValidator
    - PeriodicityValidator
- Заложены права доступа.
    - IsAuthenticated
    - UserIsStaff
    - DjangoModelPermissionsOrAnonReadOnly
- Настроена отложенная задача через Celery.
- Проект покрыли тестами на 94%.
- Имеется список зависимостей(requirements.txt).
- Результат проверки Flake8 равен 100%, при исключении миграций


### Ресурсы API
- Создание привычки POST: /habit/create/
- Получение списка публичных привычек: GET: /habit/
- Запрос на редактирование привычки: PATCH: /habit/update/<int:pk>/
- Доступ к спискам привычек текущего пользователя: GET: /user-habit/
