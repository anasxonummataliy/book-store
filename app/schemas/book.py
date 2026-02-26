from pydantic import BaseModel
from typing import Optional
from app.schemas.category import CategoryResponse


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    stock: int
    category_id: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None


class BookResponse(BookBase):
    id: int
    category: Optional[CategoryResponse] = None

    model_config = {"from_attributes": True}
