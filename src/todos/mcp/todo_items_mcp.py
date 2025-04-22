import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from pydantic.json_schema import SkipJsonSchema
from fastapi import Depends
from mcp.server.fastmcp import FastMCP
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from todos.api.dtos.todo_items_dto import TodoItemCreate, TodoItemRead, TodoItemUpdate
from todos.db.database_dependency import get_async_db
from todos.api.services.todo_items_service import create, read_all, read_one, update_one

mcp = FastMCP('TODO ITEMS MCP', '0.1.0')


@mcp.tool()
async def create_todo(data: TodoItemCreate, db: SkipJsonSchema[AsyncSession] = Depends(get_async_db)) -> TodoItemRead:
    todo = await create(data, db)
    return TodoItemRead.model_validate(todo)


@mcp.tool()
async def get_all_todos(db: SkipJsonSchema[AsyncSession] = Depends(get_async_db)) -> list[TodoItemRead]:
    todos = await read_all(db)
    return [TodoItemRead.model_validate(todo) for todo in todos]


@mcp.tool()
async def get_todo(id: UUID, db: SkipJsonSchema[AsyncSession] = Depends(get_async_db)) -> TodoItemRead:
    todo = await read_one(id, db)
    return TodoItemRead.model_validate(todo)


@mcp.tool()
async def update_todo(
    id: UUID, data: TodoItemUpdate, db: SkipJsonSchema[AsyncSession] = Depends(get_async_db)
) -> TodoItemRead:
    todo = await update_one(id, data, db)
    return TodoItemRead.model_validate(todo)
