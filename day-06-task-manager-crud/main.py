from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Day 6 - Task Manager CRUD API",
    version="1.0.0",
    description="An in-memory CRUD API for managing tasks.",
)


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)
    description: str = Field(min_length=5, max_length=300)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=80)
    description: str | None = Field(default=None, min_length=5, max_length=300)
    completed: bool | None = None


tasks: list[dict] = []
next_task_id = 1


def find_task(task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/")
async def home():
    return {
        "message": "Day 6 - Task Manager CRUD API",
        "docs": "/docs",
        "resource": "/tasks",
    }


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    global next_task_id

    task_data = task.model_dump()
    task_data["id"] = next_task_id
    next_task_id += 1

    tasks.append(task_data)

    return {
        "message": "Task created successfully",
        "task": task_data,
    }


@app.get("/tasks")
async def get_tasks(completed: bool | None = None):
    if completed is None:
        filtered_tasks = tasks
    else:
        filtered_tasks = [
            task for task in tasks if task["completed"] == completed
        ]

    return {
        "count": len(filtered_tasks),
        "tasks": filtered_tasks,
    }


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = find_task(task_id)
    return {"task": task}


@app.put("/tasks/{task_id}")
async def replace_task(task_id: int, updated_task: TaskCreate):
    task = find_task(task_id)

    task["title"] = updated_task.title
    task["description"] = updated_task.description
    task["completed"] = updated_task.completed

    return {
        "message": "Task replaced successfully",
        "task": task,
    }


@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: TaskUpdate):
    task = find_task(task_id)
    update_data = updated_task.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update",
        )

    task.update(update_data)

    return {
        "message": "Task updated successfully",
        "task": task,
    }


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = find_task(task_id)
    tasks.remove(task)

    return {
        "message": "Task deleted successfully",
        "deleted_task": task,
    }
