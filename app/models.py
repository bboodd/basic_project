from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(128))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class fruit(Base):
    __tablename__ = 'fruits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    price = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    