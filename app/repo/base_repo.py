from typing import TypeVar, Generic, Any
from sqlalchemy import Sequence, select
from sqlalchemy.engine.create import Type

from app.database.session import AsyncSession
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    @classmethod
    async def create(cls, db: AsyncSession, **kwargs) -> ModelType:
        obj = cls(**kwargs)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @classmethod
    async def get(cls, db: AsyncSession, _id: Any) -> ModelType | None:
        result = await db.execute(select(cls).where(cls.id == _id))
        return result.scalar()

    @classmethod
    async def get_all(cls, db: AsyncSession) -> Sequence[ModelType]:
        result = await db.execute(select(cls))
        return result.scalars().all()

    @classmethod
    async def update(cls, db: AsyncSession, _id: Any, **kwargs) -> ModelType | None:
        obj = await cls.get(db, _id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            await db.commit()
            await db.refresh(obj)
        return obj

    @classmethod
    async def delete(cls, db: AsyncSession, _id: Any) -> None:
        obj = await cls.get(db, _id)
        if obj:
            await db.delete(obj)
            await db.commit()
