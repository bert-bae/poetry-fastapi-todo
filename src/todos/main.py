from todos import create_app
import uvicorn

app = create_app()


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("todos.main:app", host="0.0.0.0", port=8000, reload=True)
