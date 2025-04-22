from fastapi import APIRouter
from fastapi import Depends
from uuid import UUID

from todos.api.dtos.todo_items_dto import TodoItemCreate, TodoItemRead, TodoItemUpdate
from todos.api.services.todo_items_service import create, read_all, read_one, update_one
from todos.db.database_dependency import get_async_db

router = APIRouter()


@router.post('/todo', response_model=TodoItemRead)
async def create_todo(todo: TodoItemCreate, db=Depends(get_async_db)):
    return await create(todo, db)


@router.get('/todo', response_model=list[TodoItemRead])
async def read_todos(db=Depends(get_async_db)):
    return await read_all(db)


@router.get('/todo/{id}', response_model=TodoItemRead)
async def read_todo(id: UUID, db=Depends(get_async_db)):
    return await read_one(id, db)


@router.put('/todo/{id}', response_model=TodoItemRead)
async def update_todo(id: UUID, data: TodoItemUpdate, db=Depends(get_async_db)):
    return await update_one(id, data, db)
