# tests/conftest.py
import pytest
from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.security import create_access_token
from app.models.user import User, UserRole
from app.core.security import get_password_hash
from . import Base, get_db
from app.main import app

# Тестовая база данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем таблицы
Base.metadata.create_all(bind=engine)

def override_get_db():
    """Переопределяем зависимость get_db для тестов"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def db() -> Generator:
    """Фикстура базы данных"""
    yield TestingSessionLocal()

@pytest.fixture(scope="module")
def client() -> Generator:
    """Фикстура тестового клиента"""
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def normal_user(db: Session) -> User:
    """Фикстура обычного пользователя"""
    user = User(
        email="user@example.com",
        username="normaluser",
        hashed_password=get_password_hash("password123"),
        full_name="Normal User",
        role=UserRole.USER,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture(scope="module")
def admin_user(db: Session) -> User:
    """Фикстура администратора"""
    user = User(
        email="admin@example.com",
        username="adminuser",
        hashed_password=get_password_hash("admin123"),
        full_name="Admin User",
        role=UserRole.ADMIN,
        is_active=True,
        is_superuser=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture(scope="module")
def normal_user_token_headers(normal_user: User) -> dict:
    """Фикстура заголовков с токеном обычного пользователя"""
    access_token = create_access_token(data={"sub": normal_user.username})
    return {"Authorization": f"Bearer {access_token}"}

@pytest.fixture(scope="module")
def admin_token_headers(admin_user: User) -> dict:
    """Фикстура заголовков с токеном администратора"""
    access_token = create_access_token(data={"sub": admin_user.username})
    return {"Authorization": f"Bearer {access_token}"}