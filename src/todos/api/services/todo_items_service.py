from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from models.todo_item import TodoItem
from todos.api.dtos.todo_items_dto import TodoItemCreate, TodoItemUpdate


async def create(data: TodoItemCreate, db: AsyncSession):
    todo = TodoItem(**data.model_dump())
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def update_one(id: UUID, data: TodoItemUpdate, db: AsyncSession):
    stmt = update(TodoItem).where(TodoItem.id == id).values(**data.model_dump()).returning(TodoItem)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().one()


async def read_all(db: AsyncSession):
    result = await db.execute(select(TodoItem))
    return result.scalars().all()


async def read_one(id: UUID, db: AsyncSession):
    result = await db.execute(select(TodoItem).where(TodoItem.id == id))
    return result.scalars().one()
