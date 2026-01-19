.PHONY: help install dev test migrate create-admin

help:
@echo "Доступные команды:"
@echo " make install - Установить зависимости"
@echo " make dev - Запустить проект локально"
@echo " make test - Запустить тесты"
@echo " make migrate - Применить миграции"
@echo " make create-admin - Создать администратора"
@echo " make docker-up - Запустить Docker контейнеры"
@echo " make docker-down - Остановить Docker контейнеры"

install:
pip install -r requirements.txt

dev:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
pytest -v

migrate:
alembic upgrade head

create-admin:
python scripts/create_admin.py

docker-up:
docker-compose up -d

docker-down:
docker-compose down

init-db:
python scripts/init_alembic.py
alembic upgrade head
python scripts/create_admin.py

clean:
find . -type d -name "pycache" -exec rm -rf {} +
find . -type f -name ".pyc" -delete
find . -type f -name ".pyo" -delete
find . -type f -name ".pyd" -delete
find . -type f -name ".coverage" -delete
find . -type d -name ".egg-info" -exec rm -rf {} +
find . -type d -name ".egg" -exec rm -rf {} +
find . -type d -name ".pytest_cache" -exec rm -rf {} +
find . -type d -name "htmlcov" -exec rm -rf {} +
find . -type f -name ".DS_Store" -delete'
