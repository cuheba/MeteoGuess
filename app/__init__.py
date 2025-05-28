# app/__init__.py
from fastapi import FastAPI

# Импортируем маршруты из подпапки routers
# Каждый файл в routers (например, items.py, users.py) будет содержать APIRouter
from .routers import items, users # Пример: замените на ваши реальные модули маршрутов

# Импортируем зависимости, если они используются глобально или для инициализации
from .dependencies import get_db # Пример

# Создаем основной экземпляр FastAPI приложения
app = FastAPI(
    title="METEOGUESS API",
    description="API для проекта METEOGUESS",
    version="0.1.0",
    # Можно добавить другие метаданные, такие как contact, license_info
)

# Включаем маршрутизаторы
# Это очень важный шаг, который подключает все ваши эндпоинты к основному приложению
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(users.router, prefix="/users", tags=["Users"])
# Добавьте здесь все ваши маршрутизаторы

# Вы также можете добавить глобальные обработчики событий или middleware здесь
@app.on_event("startup")
async def startup_event():
    print("Application startup...")
    # Здесь можно инициализировать базу данных, загрузить модели и т.д.

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown...")
    # Здесь можно закрыть соединения с базой данных, очистить ресурсы и т.д.

# Если у вас есть корневые эндпоинты, которые не относятся к конкретным маршрутизаторам
@app.get("/")
async def root():
    return {"message": "Welcome to METEOGUESS API!"}