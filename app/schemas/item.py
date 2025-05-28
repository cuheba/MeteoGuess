# app/schemas/item.py
from pydantic import BaseModel, ConfigDict # Важно импортировать ConfigDict
from typing import Optional

# Базовая схема для элемента
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

# Схема для создания элемента
class ItemCreate(ItemBase):
    pass

# Схема для чтения элемента (response_model)
class Item(ItemBase):
    id: int
    owner_id: int # Если у вас есть связь с пользователем/владельцем

    model_config = ConfigDict(from_attributes=True)


# Пример другой схемы
class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None