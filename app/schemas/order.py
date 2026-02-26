from pydantic import BaseModel
from typing import Optional, List
from app.schemas.book import BookResponse


class OrderItemBase(BaseModel):
    book_id: int
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    book: Optional[BookResponse] = None

    model_config = {"from_attributes": True}


class OrderBase(BaseModel):
    total_price: float
    status: str = "pending"


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    status: Optional[str] = None


class OrderResponse(OrderBase):
    id: int
    user_id: int
    order_items: List[OrderItemResponse] = []

    model_config = {"from_attributes": True}
