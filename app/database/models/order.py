from typing import List
from sqlalchemy import String, BigInteger, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import TimeBaseModel, Base



class Order(TimeBaseModel):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="pending")

    order_items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="order")
    books: Mapped[List["Book"]] = relationship("Book", secondary="order_items", viewonly=True)

class OrderItem(Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(BigInteger, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="order_items")
    book: Mapped["Book"] = relationship("Book", back_populates="order_items")
