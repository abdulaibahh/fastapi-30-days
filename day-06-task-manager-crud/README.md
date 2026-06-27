# Day 6 - Task Manager CRUD API

## Goal

Build an in-memory Task Manager API using full CRUD operations.

Day 5 introduced CRUD with students. Day 6 repeats the pattern with tasks and adds stronger backend habits:

- Better HTTP status codes
- Cleaner request schemas
- Filtering with query parameters
- Reusable helper logic
- `PUT` for full replacement
- `PATCH` for partial updates

## What I Built

A FastAPI Task Manager API with these endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome route |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?completed=true` | Get completed tasks |
| GET | `/tasks?completed=false` | Get incomplete tasks |
| GET | `/tasks/{task_id}` | Get one task |
| PUT | `/tasks/{task_id}` | Replace a full task |
| PATCH | `/tasks/{task_id}` | Update part of a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Project Files

```text
day-06-task-manager-crud/
├── main.py
├── notes.md
├── requirements.txt
├── README.md
└── social/
    ├── posting-captions.md
    └── vlog-script.md
```

## Run the API

From the repository root:

```bash
cd day-06-task-manager-crud
pip install -r requirements.txt
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Example Task JSON

```json
{
  "title": "Study FastAPI CRUD",
  "description": "Practice creating, reading, updating, and deleting tasks.",
  "completed": false
}
```

## PowerShell Test Commands

Create a task:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks" -Method Post -ContentType "application/json" -Body '{"title":"Study FastAPI CRUD","description":"Practice creating, reading, updating, and deleting tasks.","completed":false}'
```

Get all tasks:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks"
```

Get incomplete tasks:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks?completed=false"
```

Get one task:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/1"
```

Replace a full task with `PUT`:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/1" -Method Put -ContentType "application/json" -Body '{"title":"Finish Day 6","description":"Complete the Task Manager CRUD API lesson.","completed":true}'
```

Partially update a task with `PATCH`:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/1" -Method Patch -ContentType "application/json" -Body '{"completed":true}'
```

Delete a task:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/1" -Method Delete
```

## Git Workflow

```bash
git checkout main
git pull origin main
git checkout -b day-06
git add .
git commit -m "Day 6: Build task manager CRUD API"
git push origin day-06
git checkout main
git merge day-06
git push origin main
```

## Learning Outcome

After Day 6, I can build a complete CRUD API for a resource and understand how each HTTP method maps to backend behavior.

I also understand why real APIs use:

- `201 Created` when a resource is created
- `404 Not Found` when a resource does not exist
- `400 Bad Request` when the user sends an empty partial update
- query parameters to filter resources
