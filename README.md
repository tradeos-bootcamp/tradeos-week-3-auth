# 🛡️ Неделя 3: Аутентификация и авторизация | TradeOS Bootcamp

## 🎯 Цели недели

1. **Настроить** JWT-аутентификацию в FastAPI
2. **Реализовать** регистрацию и авторизацию пользователей
3. **Создать** ролевую модель (RBAC) - admin, manager, user
4. **Защитить** endpoints с помощью зависимостей
5. **Протестировать** систему безопасности

## ⚡ Быстрый старт

```bash
# Клонируйте ваш репозиторий
git clone https://github.com/tradeos-bootcamp/ваш-репозиторий.git
cd week-3-auth

# Создайте виртуальное окружение
python -m venv venv

# Активируйте (Windows)
venv\Scripts\activate
# Или (Mac/Linux)
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt

# Настройте .env файл
cp .env.example .env
# Отредактируйте .env файл

# Запустите PostgreSQL
docker-compose up -d postgres

# Инициализируйте Alembic (если первый раз)
alembic init migrations

# Примените миграции
alembic upgrade head

# Создайте администратора
python scripts/create_admin.py

# Запустите сервер
uvicorn app.main:app --reload
📋 Структура проекта
text
tradeos-week-3-auth/
├── app/                          # Основной код приложения
│   ├── models/                   # SQLAlchemy модели
│   ├── schemas/                  # Pydantic схемы
│   ├── crud/                     # CRUD операции
│   ├── core/                     # Конфигурация и утилиты
│   └── api/                      # API endpoints
├── tests/                        # Тесты
├── migrations/                   # Миграции Alembic
├── scripts/                      # Вспомогательные скрипты
├── requirements.txt              # Зависимости
├── docker-compose.yml            # Конфигурация Docker
├── .env.example                  # Пример переменных окружения
└── README.md                     # Этот файл
🎯 Задания недели
Обязательная часть:
✅ Реализовать модель User с ролями

✅ Создать endpoints регистрации и авторизации

✅ Настроить JWT токены

✅ Добавить ролевую модель (RBAC)

✅ Защитить существующие endpoints

Дополнительная часть:
🔄 Реализовать refresh токены

🧪 Написать тесты для всех endpoints

🔐 Добавить валидацию паролей

👤 Реализовать профиль пользователя

🧪 Тестирование
bash
# Запуск всех тестов
pytest

# Запуск тестов аутентификации
pytest tests/test_auth.py -v

# С отчетом о покрытии
pytest --cov=app --cov-report=html
🔧 Полезные команды
bash
# Создать новую миграцию
alembic revision --autogenerate -m "Описание"

# Применить миграции
alembic upgrade head

# Откатить миграцию
alembic downgrade -1

# Показать историю
alembic history --verbose
📊 Критерии оценки
Максимум: 25 баллов

Обязательные (15 баллов):
Модель User и миграции (3 балла)

Регистрация/авторизация (3 балла)

JWT токены (3 балла)

Ролевая модель (3 балла)

Защита endpoints (3 балла)

Дополнительные (до 10 баллов):
Refresh токены (2 балла)

Тесты (3 балла)

Валидация паролей (3 балла)

Профиль пользователя (2 балла)

Проходной балл: 10

⏰ Дедлайны
🟢 Основное задание: Воскресенье, 23:59

🟡 Code review: Понедельник-вторник

🔴 Исправления: До среды

📞 Поддержка
💬 Telegram чат: [ссылка в Classroom]

📢 Канал: @tradeos_bootcamp

👨‍🏫 Консультации: Пн-Пт 19:00-20:00

Версия задания: 3.0 | TradeOS Bootcamp © 2024
