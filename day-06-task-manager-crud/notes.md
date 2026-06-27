# Day 6 Notes - Task Manager CRUD API

## What CRUD Means

CRUD is the basic lifecycle of data in backend systems:

- Create data
- Read data
- Update data
- Delete data

In FastAPI, CRUD usually maps to HTTP methods:

| CRUD action | HTTP method | Example route |
|---|---|---|
| Create | POST | `/tasks` |
| Read all | GET | `/tasks` |
| Read one | GET | `/tasks/{task_id}` |
| Replace | PUT | `/tasks/{task_id}` |
| Partial update | PATCH | `/tasks/{task_id}` |
| Delete | DELETE | `/tasks/{task_id}` |

## What I Built

I built a Task Manager API with:

- Create task
- Get all tasks
- Filter tasks by completion status
- Get a single task by ID
- Replace a full task
- Update part of a task
- Delete a task

## New Things I Learned

### `status.HTTP_201_CREATED`

When a new resource is created, the API should return status code `201`.

```python
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
```

### Query Parameter Filtering

This route can return:

- all tasks
- only completed tasks
- only incomplete tasks

```text
/tasks
/tasks?completed=true
/tasks?completed=false
```

### Helper Function

Instead of repeating the same loop in every route, I created a helper:

```python
def find_task(task_id: int) -> dict:
```

This keeps the route functions cleaner.

### `PATCH` vs `PUT`

`PUT` replaces the full task.

`PATCH` updates only the fields I provide.

## Important Reminder

The tasks are stored in a Python list.

That means:

- data is temporary
- data disappears when the server restarts
- this is good for learning
- a real API will later use a database

## Reflection

Today helped me understand CRUD more deeply because I repeated the pattern with a different resource: tasks.

I also started thinking more like a backend developer by using better status codes, cleaner schemas, and reusable helper logic.
