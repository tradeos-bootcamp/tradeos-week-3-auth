
#Скрипт быстрой настройки проекта для Windows
Write-Host "=== Настройка проекта TradeOS Week 3 ===" -ForegroundColor Green

#Проверка Python
Write-Host "`n1. Проверка Python..." -ForegroundColor Cyan
$pythonVersion = python --version
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python найден: $pythonVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Python не найден. Установите Python 3.11+" -ForegroundColor Red
    exit 1
}

#Создание виртуального окружения
Write-Host "`n2. Создание виртуального окружения..." -ForegroundColor Cyan
if (!(Test-Path "venv")) {
    python -m venv venv
    Write-Host "✓ Виртуальное окружение создано" -ForegroundColor Green
}
else {
    Write-Host "✓ Виртуальное окружение уже существует" -ForegroundColor Yellow
}

#Активация виртуального окружения
Write-Host "`n3. Активация виртуального окружения..." -ForegroundColor Cyan
Write-Host "Запустите: venv\Scripts\activate" -ForegroundColor Yellow

Установка зависимостей
Write-Host "`n4. Установка зависимостей..." -ForegroundColor Cyan
Write-Host "Запустите: pip install -r requirements.txt" -ForegroundColor Yellow

#Настройка .env файла
Write-Host "`n5. Настройка окружения..." -ForegroundColor Cyan
if (!(Test-Path ".env") -and (Test-Path ".env.example")) {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ .env файл создан из примера" -ForegroundColor Green
    Write-Host " Отредактируйте .env файл: notepad .env" -ForegroundColor Yellow
}
elseif (Test-Path ".env") {
    Write-Host "✓ .env файл уже существует" -ForegroundColor Yellow
}

#Проверка Docker
Write-Host "`n6. Проверка Docker..." -ForegroundColor Cyan
$dockerVersion = docker --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Docker найден: $dockerVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Docker не найден. Установите Docker Desktop" -ForegroundColor Red
}

Write-Host "n=== Настройка завершена ===" -ForegroundColor Green Write-Host "nСледующие шаги:" -ForegroundColor Cyan
Write-Host "1. Активируйте окружение: venv\Scripts\activate" -ForegroundColor Yellow
Write-Host "2. Установите зависимости: pip install -r requirements.txt" -ForegroundColor Yellow
Write-Host "3. Запустите БД: docker-compose up -d postgres" -ForegroundColor Yellow
Write-Host "4. Инициализируйте миграции: python scripts/init_alembic.py" -ForegroundColor Yellow
Write-Host "5. Примените миграции: alembic upgrade head" -ForegroundColor Yellow
Write-Host "6. Создайте админа: python scripts/create_admin.py" -ForegroundColor Yellow
Write-Host "7. Запустите сервер: uvicorn app.main:app --reload" -ForegroundColor Yellow
