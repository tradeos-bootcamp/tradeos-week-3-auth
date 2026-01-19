
#

Инструкция по запуску проекта
Для Windows:
Откройте PowerShell

Перейдите в папку проекта: cd tradeos-week-3-auth

Запустите скрипт настройки: .\setup.ps1

Выполните шаги, которые показывает скрипт

Для Linux/Mac:
Откройте терминал

Перейдите в папку проекта: cd tradeos-week-3-auth

Создайте виртуальное окружение: python3 -m venv venv

Активируйте: source venv/bin/activate

Установите зависимости: pip install -r requirements.txt

Настройте .env: cp .env.example .env && nano .env

Запустите БД: docker-compose up -d

Инициализируйте миграции: make init-db

Запустите сервер: make dev

Быстрые команды:
Windows:
powershell

## Активация окружения

venv\Scripts\activate

## Установка зависимостей

pip install -r requirements.txt

## Запуск БД

docker-compose up -d postgres

## Миграции

alembic upgrade head

## Создание админа

python scripts/create_admin.py

## Запуск сервера

uvicorn app.main:app --reload

Linux/Mac:
bash

## Активация окружения Linux/Mac

source venv/bin/activate

## Все команды через make

make install      # установить зависимости
make docker-up    # запустить БД
make migrate      # применить миграции
make create-admin # создать админа
make dev         # запустить сервер
make test        # запустить тесты
Тестирование API:
Откройте браузер: <http://localhost:8000/docs>

Создайте пользователя через POST /auth/register

Авторизуйтесь через POST /auth/login

Скопируйте access_token из ответа

Нажмите "Authorize" в Swagger UI и вставьте токен

Тестируйте защищенные endpoints
