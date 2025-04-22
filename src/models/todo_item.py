from uuid import uuid4
from enum import Enum
from sqlalchemy import Column, UUID, String, Enum as SQLAlchemyEnum
from .base_class import Base


class StatusEnum(str, Enum):
    done = "done"
    pending = "pending"


class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description = Column(String)
    title = Column(String)
    status = Column(SQLAlchemyEnum(StatusEnum), default=StatusEnum.pending)
