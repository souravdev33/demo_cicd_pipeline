from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

# Todo model
class Todo(BaseModel):
    id: int
    table: str
    description: str

# In-memory storage
todos: List[Todo] = []

@api.get("/")
def home():
    return {"message": "Hello World"}

@api.get("/todo")
def get_todo():
    return todos

@api.post("/todo")
def add_todo(todo: Todo):
    todos.append(todo)
    return todos

@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return todos
    return {"message": "Error in updation"}

@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return todos
    return {"message": "Error in deletion"}
