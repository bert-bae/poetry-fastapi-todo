from http import HTTPStatus

import pytest
from models.todo_item import StatusEnum


def get_todo_items_url(app):
    return f'{app.url_path_for("read_todos")}'


@pytest.mark.anyio
async def test_get_todo_items(async_app, async_client, async_db, create_todo_item):
    # Create test todo items
    items = [
        create_todo_item(description='Task 1', status=StatusEnum.pending),
        create_todo_item(description='Task 2', status=StatusEnum.done),
    ]
    async_db.add_all(items)
    await async_db.commit()

    # Test the GET /todo endpoint
    resp = await async_client.get(get_todo_items_url(async_app))
    assert resp.status_code == HTTPStatus.OK

    data = resp.json()
    assert len(data) == 2  # Ensure two items are returned

    # Validate the response data
    assert data[0]['description'] == 'Task 1'
    assert data[0]['status'] == StatusEnum.pending.value
    assert data[1]['description'] == 'Task 2'
    assert data[1]['status'] == StatusEnum.done.value
