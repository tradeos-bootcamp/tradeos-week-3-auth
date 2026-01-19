#!/usr/bin/env python3
"""
Скрипт для инициализации Alembic в проекте.
Запускать только один раз при первом создании проекта.
"""

import os
import subprocess
import sys

def init_alembic():
    print("Инициализация Alembic...")
    
    # Проверяем, существует ли уже папка migrations
    if os.path.exists("migrations"):
        print("Папка migrations уже существует. Пропускаем инициализацию.")
        return True  # Выходим нормально
    
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
                '''import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import Base
# Импортируйте ваши модели здесь
# from app.models.user import User
# from app.models.product import Product

target_metadata = Base.metadata'''
            )
            
            with open(env_py_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            
            print("env.py успешно обновлен для работы с нашими моделями.")
        
        print("✓ Alembic успешно инициализирован!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при инициализации Alembic: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False

if __name__ == "__main__":
    success = init_alembic()
    sys.exit(0 if success else 1)