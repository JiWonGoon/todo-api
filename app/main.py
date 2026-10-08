from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Todo API",
    version="1.0.0"
)


class Todo(BaseModel):
    title: str


todos = [
    {
        "id": 1,
        "title": "Kubernetes 공부하기"
    }
]


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "1.0.1"
    }


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title
    }

    todos.append(new_todo)

    return new_todo
