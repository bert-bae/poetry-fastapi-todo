from models import TodoItem

from models.todo_item import StatusEnum
import pytest


@pytest.fixture
def create_todo_item(async_db):
    def _create_todo_item(
        description=str,
        status=StatusEnum.pending,
    ):
        """A callable fixture to create a TodoItem object in the database."""
        user = TodoItem(description=description, status=status)
        return user

    return _create_todo_item
