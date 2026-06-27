# Day 5 - Building a Real CRUD API

## Goal

Build a complete FastAPI CRUD API that can create, read, update, and delete student records.

By the end of this day, you should understand how backend systems manage resources using REST-style endpoints.

## What I Built

- A FastAPI app for managing students
- A second practice API for managing courses
- Request body validation with Pydantic models
- In-memory storage using Python lists
- Error handling with `HTTPException`
- REST-style routes for `POST`, `GET`, `PUT`, and `DELETE`

## Key Concepts

| Concept | Meaning |
|---|---|
| CRUD | Create, Read, Update, Delete |
| POST | Add new data |
| GET | Retrieve data |
| PUT | Update existing data |
| DELETE | Remove data |
| Pydantic model | Defines and validates request body data |
| HTTPException | Returns proper API error responses |

## Project Files

```text
day-05-crud-api/
├── main.py
├── course.py
├── notes.md
├── requirements.txt
└── README.md
```

## Run the Student API

From the repository root:

```bash
cd day-05-crud-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run the Course Practice API

Stop the current server with `CTRL + C`, then run:

```bash
uvicorn course:app --reload
```

Open Swagger UI again:

```text
http://127.0.0.1:8000/docs
```

## Student API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check that the API is running |
| POST | `/students` | Create a student |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get one student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Example Student JSON

```json
{
  "name": "Abdulai",
  "age": 22,
  "course": "FastAPI Backend Development"
}
```

## PowerShell Test Commands

Create a student:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students" -Method Post -ContentType "application/json" -Body '{"name":"Abdulai","age":22,"course":"FastAPI Backend Development"}'
```

Get all students:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students"
```

Get one student:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students/1"
```

Update a student:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students/1" -Method Put -ContentType "application/json" -Body '{"name":"Abdulai Bah","age":23,"course":"Production FastAPI"}'
```

Delete a student:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students/1" -Method Delete
```

## Git Workflow Used

```bash
git checkout main
git pull origin main
git checkout day-05
git add .
git commit -m "Day 5: Complete CRUD API"
git push origin day-05
git checkout main
git merge day-05
git push origin main
```

## Learning Reflection

Today I learned that most backend systems are built around resources. A resource can be a student, user, product, course, order, or post.

CRUD is the foundation of real backend development because almost every app needs to add, view, edit, and remove data.

The API still uses in-memory lists, so the data disappears when the server restarts. That is expected for Day 5. Later, this will be upgraded to a real database.
