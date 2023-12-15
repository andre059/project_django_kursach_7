# "Атомные привычки"

В 2018 году Джеймс Клир написал книгу «Атомные привычки»,
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Заказчик прочитал книгу, впечатлился и обратился с запросом реализовать трекер полезных привычек.

Тут реализована бэкенд-часть SPA веб-приложения.

# Установка

1. ### Установите Python 3.11 и выше
2. ### Создайте папку, куда будете клонировать проект
3. ### Скачайте репозиторий проекта:
   ### git clone https://github.com/andre059/project_django_kursach_7
4. ### Установите виртуальное окружение:
   ### env и активируйте его env\Scripts\activate.ps1
5. ### Установите зависимости из файла requirements.txt:
   ### pip install -r requirements.txt
6. ### Настройте файл settings.py находящийся в папке config:
    
    -DATABASES_NAME = Название папки куда вы клонировали проект
    
    -DATABASES_USER = Переменная, которая должна содержать имя пользователя для подключения к базе данных PostgreSQL
    
    -DATABASES_PASSWORD = Пароль к вашей базе данных
    
    -SECRET_KEY = 'тут должен быть ваш секретный ключь'
    
    -CUR_API_KEY = 'Доступа к сервису с курсами валют'
    
    -STRIPE_SECRET_KEY = 'Секретный ключ Stripe API используется для аутентификации запросов и обеспечения безопасности при передаче платежных данных, ключь начинается на sk_test'
    
    -EMAIL_HOST_USER ='Значение этой переменной должно быть установлено на адрес электронной почты, который вы хотите использовать для отправки писем'
    
    -EMAIL_HOST = 'Адрес SMTP-сервера, который будет использоваться для отправки электронных писем из приложения'
    
    -EMAIL_HOST_PASSWORD ='Пароль для учетной записи электронной почты, используемой для отправки электронных писем с помощью SMTP'
    
    -TELEGRAM_TOKEN = 'Телеграм токен'
    
    -CSU_SET_PASSWORD = 'Пароль для файла csu.py'
    
7. Запустите проект:
   python manage.py runserver 
