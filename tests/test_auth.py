# tests/test_auth.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.models.user import User, UserRole
from app.core.security import get_password_hash

def test_register_user(client: TestClient, db: Session):
    """Тест регистрации пользователя"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123",
            "password_confirm": "testpass123",
            "full_name": "Test User"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert data["role"] == "user"
    assert data["is_active"] == True
    assert "hashed_password" not in data

def test_register_duplicate_email(client: TestClient, db: Session):
    """Тест регистрации с существующим email"""
    # Создаем первого пользователя
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "user1",
            "password": "password123",
            "password_confirm": "password123"
        }
    )
    
    # Пытаемся создать второго с тем же email
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "user2",
            "password": "password123",
            "password_confirm": "password123"
        }
    )
    
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_login_success(client: TestClient, db: Session):
    """Тест успешного входа"""
    # Сначала регистрируем пользователя
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123",
            "password_confirm": "testpass123"
        }
    )
    
    # Теперь логинимся
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpass123"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client: TestClient, db: Session):
    """Тест входа с неправильным паролем"""
    # Сначала регистрируем пользователя
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123",
            "password_confirm": "testpass123"
        }
    )
    
    # Пытаемся войти с неправильным паролем
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]

def test_get_current_user(client: TestClient, db: Session, normal_user_token_headers: dict):
    """Тест получения информации о текущем пользователе"""
    response = client.get(
        "/api/v1/auth/me",
        headers=normal_user_token_headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "username" in data
    assert "role" in data

def test_access_protected_endpoint_without_token(client: TestClient):
    """Тест доступа к защищенному endpoint без токена"""
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Test Product",
            "price": 100.0,
            "category": "test"
        }
    )
    
    assert response.status_code == 401

def test_access_protected_endpoint_with_token(client: TestClient, normal_user_token_headers: dict):
    """Тест доступа к защищенному endpoint с токеном обычного пользователя"""
    response = client.post(
        "/api/v1/products/",
        headers=normal_user_token_headers,
        json={
            "name": "Test Product",
            "price": 100.0,
            "category": "test"
        }
    )
    
    # Обычный пользователь не может создавать товары
    assert response.status_code == 403

def test_access_admin_endpoint_as_admin(client: TestClient, admin_token_headers: dict):
    """Тест доступа к админскому endpoint как администратор"""
    response = client.get(
        "/api/v1/auth/users",
        headers=admin_token_headers
    )
    
    assert response.status_code == 200

def test_access_admin_endpoint_as_user(client: TestClient, normal_user_token_headers: dict):
    """Тест доступа к админскому endpoint как обычный пользователь"""
    response = client.get(
        "/api/v1/auth/users",
        headers=normal_user_token_headers
    )
    
    assert response.status_code == 403

def test_refresh_token(client: TestClient, db: Session):
    """Тест обновления токена"""
    # Регистрируем и логинимся
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123",
            "password_confirm": "testpass123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpass123"
        }
    )
    
    refresh_token = login_response.json()["refresh_token"]
    
    # Обновляем токен
    response = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data