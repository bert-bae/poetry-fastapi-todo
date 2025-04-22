from fastapi import APIRouter
from todos.api.controllers.todo_items_controller import router as todo_items_router

router = APIRouter()

router.include_router(todo_items_router)
