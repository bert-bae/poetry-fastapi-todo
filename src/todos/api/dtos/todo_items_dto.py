from uuid import UUID
from pydantic import BaseModel

from models.todo_item import StatusEnum


class TodoItemRead(BaseModel):
    id: UUID
    description: str | None
    status: StatusEnum

    class Config:
        orm_mode = True


class TodoItemCreate(BaseModel):
    description: str


class TodoItemUpdate(BaseModel):
    description: str | None = None
    status: StatusEnum | None = None


class TodoRead(BaseModel):
    id: UUID

    class Config:
        orm_mode = True
