# VK Bot Long Poll API
***VK Бот для сообществ поддерживает следующий функционал:***  
- Отправка в личный/общий чат сообщений и фото из БД Postgresql,  
- Реакция на команды,  
- Клавиатура,  
- Подсчет общего времени работы с момента активации,  
- Остановка бота по команде  

Заполнить БД можно следующими способами: 
> - Management команда из CSV (тестовые данные),  
> - Админ панель Django,  
> - PgAdmin 4
> - Django shell

***Для запуска проекта необходимо выполнить действия, описанные ниже.***
 ```bash
git clone <project>
cd <project>
# сделайте копию файла <.env.example> в <.env>
cp .env.example .env
 ```
**VK**  
После клонирования проекта и копирования файла .env необходимо получить ключи доступа к своему сообществу ВК и ID группы.  

*Создать сообщество и выполнить настройки:*  
Управление > Настройки > Работа с API,  
Long Poll API > Настройки - Включено,  
Типы событий > Выбрать типы событий:  
> Оптимально:  
> Сообщения - входящее, исходящее, разрешение на получение  
> Фотографии - добавление  
> Остальное на усмотрение.  

Ключи доступа > Создать ключ  
> Оптимально предоставить полный доступ  

Копируем ключ в файл .env в ACCESS_TOKEN либо FULL_ACCESS  
Копируем ID Сообщества, можно посмотреть в Настройках > Адрес  

>Создан файл .env, добавлены ID VK сообщества и ключ доступа.  
>Разворачиваем проект через Docker.  

**Docker**
 ```bash
cd vk_bot/
docker-compose up -d  #  "-" в зависимости от версии
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
# Для заполнения базы тестовыми данными из CSV:
docker-compose exec backend python manage.py import_data
```
***Bot Start***  
 ```bash
# Если все настройки выполнены и загружены тестовые данные запускаем Бота:
docker-compose exec backend python baking_bot/bot.py
```
Активируем бота в личном/общем чате командой:  
/Бот!  
Остановить:  
/Стоп!  

**PostgreSQL**  
Базу данных можно заполнить одним из следующих способов.  
```bash
# 1. Django admin панель  
# Создаем пользователя  
docker-compose exec backend python manage.py createsuperuser  
# Логинимся  
http://localhost/admin
```
```bash
# 2. PgAdmin 4  
http://localhost:5050/
# Login:
# email -> pgadmin4@pgadmin.org
# password -> admin
# Add New server
# General: # Name -> <Your_name>
# Connection: # Host -> host.docker.internal
# Port -> 5433
# USERNAME -> postgres
# PASSWORD -> postgres
# save
# Servers > Your_server > DB > postgres > Schemas > Tables
```
```bash
# 3. Django shell
docker-compose exec backend python manage.py shell
>>> from baking_bot.models import *
>>> s = SimpleText(title='new', description='new desc')
>>> s.save()
>>> s
<SimpleText: new - new desc>
>>> quit()
```

**Dev**  
Для локальной разработки и подключения к PostgreSQL изменить файлы:  
```bash
settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:postgres@localhost:5433/postgres')}
```
```bash
db.py
# For local dev
conn_url = 'postgresql+psycopg2://postgres:postgres@localhost:5433/postgres'
```
