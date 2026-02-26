from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, String, BigInteger
from app.database.base import TimeBaseModel
from app.database.models.user import String, mapped_column


class Book(TimeBaseModel):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    
