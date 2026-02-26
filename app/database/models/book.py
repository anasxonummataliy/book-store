from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, String, BigInteger, ForeignKey
from app.database.base import TimeBaseModel
from typing import List


class Book(TimeBaseModel):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(BigInteger, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)

    order_items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem", back_populates="book"
    )
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="books")
