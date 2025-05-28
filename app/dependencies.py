# app/dependencies.py

# Импортируйте то, что нужно для вашей базы данных.
# Например, для SQLAlchemy:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models # Если у вас есть models/base.py или что-то подобное

# --- НАСТРОЙКИ ВАШЕЙ БАЗЫ ДАННЫХ ---
# Пример URL для SQLite:
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Для PostgreSQL:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"
# Для MySQL:
# SQLALCHEMY_DATABASE_URL = "mysql://user:password@host:port/dbname"

# Создаем движок SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
    # check_same_thread=False нужен только для SQLite, чтобы разрешить
    # несколько запросов к базе данных в разных потоках (потоках FastAPI).
)

# Создаем объект SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем все таблицы (если они не существуют)
# Вам нужно убедиться, что ваши модели импортированы где-то,
# чтобы Base.metadata.create_all их обнаружил.
# Обычно это делается в app/__init__.py или отдельном файле для инициализации БД.
# Если вы используете Base из models/base.py, то:
# from .models.base import Base # Пример, если у вас есть Base в models/base.py
# Base.metadata.create_all(bind=engine) # Это лучше вызывать один раз при запуске приложения,
# например, в @app.on_event("startup") в app/__init__.py,
# или в отдельном скрипте для миграций.

# --- ФУНКЦИЯ ЗАВИСИМОСТИ get_db ---
# Эта функция создает сессию базы данных для каждого запроса.
# FastAPI закроет ее автоматически после завершения запроса.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()