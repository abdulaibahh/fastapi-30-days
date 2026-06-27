# FastAPI Backend Mastery

A 30-day backend engineering journey focused on mastering FastAPI, APIs, databases, authentication, testing, and deployment.

## Structure

Each day contains:
- Notes
- Practice code
- Mini projects
- Exercises

## Daily Progress

| Day | Topic | Status |
|---|---|---|
| Day 1 | API Fundamentals | ✅ Completed |
| Day 2 | First FastAPI Application | ✅ Completed |
| Day 3 | Path and Query Parameters | ✅ Completed |
| Day 4 | Request Body and Pydantic Models | ✅ Completed |
| Day 5 | CRUD API | ✅ Completed |

## Branch Workflow

Each day is developed on its own branch and then merged into `main`.

Example:

```bash
git checkout main
git pull origin main
git checkout -b day-06
```

After completing the day:

```bash
git add .
git commit -m "Day 6: <clear topic>"
git push origin day-06
git checkout main
git merge day-06
git push origin main
```

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest

## Goal
Become production-ready in backend API development.
