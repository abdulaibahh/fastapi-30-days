# Day 5 Vlog Script - CRUD API with FastAPI

## Video Format

- Platform: TikTok, Facebook Reels, Facebook page video
- Account handles: `lafwol.dev`, `Lafwol.Dev`
- Length: 45-60 seconds
- Layout: Vertical, 1080x1920
- Style: Screen recording + face camera intro/outro

## Story

Today I moved from simple API routes into a real backend pattern: CRUD.

CRUD means Create, Read, Update, and Delete. I used FastAPI to build a student API that can add students, list them, view one student, update a student, and delete a student.

## Shot List and Narration

| Time | Visual | Narration | On-screen Caption |
|---|---|---|---|
| 0-4s | Face camera or title screen | Day 5 of learning FastAPI backend development. Today I built my first real CRUD API. | Day 5: CRUD API |
| 4-10s | Show `main.py` | CRUD means Create, Read, Update, and Delete. These are the actions behind most real apps. | Create. Read. Update. Delete. |
| 10-18s | Show `Student` model | I used a Pydantic model to define the data my API accepts: name, age, and course. | Request body validation |
| 18-28s | Show Swagger `/students` endpoints | Then I created REST endpoints using POST, GET, PUT, and DELETE. | REST endpoints |
| 28-38s | Test POST and GET in Swagger | I tested creating a student and fetching students through the API docs. | Test in Swagger UI |
| 38-48s | Test PUT and DELETE | I also learned how to update and delete records, plus return a 404 error when data is missing. | Handle updates and errors |
| 48-58s | Show Git branch or repo | Finally, I committed Day 5 to its own branch and merged it into main. | Branch, commit, merge |

## Voiceover Script

```text
Day 5 of my FastAPI backend journey.

Today I built my first real CRUD API.

CRUD means Create, Read, Update, and Delete. These are the basic actions behind most backend systems, from school apps to e-commerce platforms.

I created a Student model with Pydantic so FastAPI can validate the request body automatically.

Then I built endpoints to create a student, get all students, get one student, update a student, and delete a student.

I also practiced proper error handling with HTTPException, so the API returns a 404 when a student is not found.

The data is still stored in a Python list for now, but the structure is the same pattern I will later connect to a real database.

Day 5 complete. CRUD finally makes backend APIs feel real.
```

## B-roll Checklist

- Show the repo folder: `day-05-crud-api`
- Show `Student` model in `main.py`
- Show all `/students` routes in Swagger
- Create one student with POST
- Fetch the student with GET
- Update the student with PUT
- Delete the student with DELETE
- Show the Git commit or GitHub branch

## Render Note

The final vertical video render should be generated after confirming:

- Mood
- Light or dark canvas
- Brand colors or visual references
