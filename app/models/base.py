# app/models/base.py
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from app.database import Base

class TimeStampedModel:
    """Базовая модель с timestamp полями"""
    
    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now())
    
    @declared_attr
    def updated_at(cls):
        return Column(DateTime(timezone=True), onupdate=func.now())

class BaseModel(Base, TimeStampedModel):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)