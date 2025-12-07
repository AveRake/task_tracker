from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import uvicorn

app = FastAPI()

# Модель данных (DTO)
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    is_completed: bool = False

fake_db = []

@app.get("/")
def read_root():
    return {"message": "DevOps Homework App is Running!", "version": "1.0.0"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = len(fake_db) + 1
    fake_db.append(task)
    return task

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)