from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.book import Book
from app.database.models.order import Order
from app.database.models.user import User
from app.schemas.user import UserCreate
from app.schemas.book import BookCreate, BookUpdate
from app.schemas.order import OrderCreate
from pwdlib import PasswordHash


from app.database.session import get_db

router = APIRouter()

pwd_context = PasswordHash.recommended()


@router.get("/books")
async def get_books(db: AsyncSession = Depends(get_db)):
    books = await Book.get_all(db)
    return books


@router.post("/books")
async def post_books(book: BookCreate, db: AsyncSession = Depends(get_db)):
    new_book = await Book.create(db, **book.model_dump())
    return "Book created successfully", new_book


@router.get("/books/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await Book.get(db, book_id)
    return book


@router.put("/books/{book_id}")
async def put_book(
    book_id: int, book_update: BookUpdate, db: AsyncSession = Depends(get_db)
):
    updated_book = await Book.update(
        db, book_id, **book_update.model_dump(exclude_unset=True)
    )
    return updated_book


@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    await Book.delete(db, book_id)


@router.post("/users")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User.create(db,
        username=user.username,
        email=user.email,
        hashed_password=user.hash_password,
        is_active=True,
    )
    return "User created successfully", new_user


@router.post("/orders")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    new_order = await Order.create(db, **order.model_dump())
    return "Order created successfully", new_order


@router.get("/orders/{order_id}")
async def get_order(order_id: int, db: AsyncSession = Depends(get_db)):
    order = await Order.get(db, order_id)
    return order


@router.post("/categories")
async def create_category(name: str, db: AsyncSession = Depends(get_db)):
    from app.database.models.category import Category

    new_category = await Category.create(db, name=name)
    return "Category created successfully", new_category
