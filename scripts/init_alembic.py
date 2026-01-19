#!/usr/bin/env python3
"""
Скрипт для инициализации Alembic в проекте.
Запускать только один раз при первом создании проекта.
"""

import os
import subprocess
import sys

def init_alembic():
"""Инициализировать Alembic миграции"""

text
print("Инициализация Alembic...")

# Проверяем, существует ли уже папка migrations
if os.path.exists("migrations"):
    print("Папка migrations уже существует. Пропускаем инициализацию.")
    return

try:
    # Инициализируем Alembic
    result = subprocess.run(
        ["alembic", "init", "migrations"],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)
    
    # Обновляем env.py для работы с нашими моделями
    env_py_path = "migrations/env.py"
    if os.path.exists(env_py_path):
        with open(env_py_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Добавляем импорт наших моделей
        new_content = content.replace(
            'target_metadata = None',
            'import sys\nimport os\nsys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom app.database import Base\nfrom app.models.user import User\nfrom app.models.product import Product\n\ntarget_metadata = Base.metadata'
        )
        
        with open(env_py_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("env.py успешно обновлен для работы с нашими моделями.")
    
    print("Alembic успешно инициализирован!")
    
except subprocess.CalledProcessError as e:
    print(f"Ошибка при инициализации Alembic: {e}")
    print(f"STDOUT: {e.stdout}")
    print(f"STDERR: {e.stderr}")
    sys.exit(1)
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
    sys.exit(1)
if name == "main":
init_alembic()
