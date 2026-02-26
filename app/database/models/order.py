from sqlalchemy import String, BigInteger, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import TimeBaseModel


class Order(TimeBaseModel):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="pending")
