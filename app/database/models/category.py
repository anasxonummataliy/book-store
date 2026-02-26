from sqlalchemy import String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import TimeBaseModel
from app.repo.base_repo import BaseRepository

class Category(TimeBaseModel, BaseRepository["Category"]):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
