# Тестовое задание

***
## Описание

Веб-приложение для заказчиков и исполнителей. 

Аутентификация использует переопределенный класс django User. В него были добавлены некоторые поля.

Так же существует два личных кабинета (ЛК). 
В ЛК исполнителя содеражится следующая информация:

1. Фамилия
2. Имя
3. Email
4. Telegram
5. Дата регистрации
6. О себе
7. Опыт работы

А в ЛК заказчика содеражится следующая информация:

1. Фамилия
2. Имя
3. Email
4. Telegram
5. Дата последнего захода на сайт

В ЛК пользователи могут редактировать некоторые поля.
Исполнители: 'О себе', 'Телеграм', 'Опыт работы'
Заказчики: 'Телеграм'


Админ панель - админка django. 

## Установка

Для установки зависимостей лучше использовать Poetry.

```
pip install poetry
poetry install
```

Если вы используете `pip` напрямую, можно воспользоваться командой:

`pip install -r poetry.lock`

Создайте файл .env и задайте значения следующим переменным:
  1. DB_NAME - название базы данных
  2. HOST - имя хоста
  3. PORT - порт
  4. USER - пользователь
  5. PASS - пароль
