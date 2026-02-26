from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, String, BigInteger, ForeignKey
from app.database.base import TimeBaseModel
from typing import TYPE_CHECKING, List
from app.repo.base_repo import BaseRepository

if TYPE_CHECKING:
    from .order import Order, OrderItem


class Book(TimeBaseModel, BaseRepository["Book"]):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(BigInteger, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)

    order_items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem", back_populates="book"
    )
    orders: Mapped[List["Order"]] = relationship("Order",secondary="order_items", back_populates="books")
