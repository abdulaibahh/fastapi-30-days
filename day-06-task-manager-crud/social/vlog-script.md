# Day 6 Vlog Script - Task Manager CRUD API

## Video Format

- Platform: TikTok, Facebook Reels, Facebook page video
- Account handles: `lafwol.dev`, `Lafwol.Dev`
- Length: 45-60 seconds
- Layout: Vertical, 1080x1920
- Style: Screen recording + short face camera intro/outro

## Story

Today I repeated CRUD with a more realistic mini-project: a Task Manager API.

The goal was not only to make endpoints work, but to think more like a backend developer by using better status codes, filtering, helper functions, and separate schemas for create and update actions.

## Shot List and Narration

| Time | Visual | Narration | On-screen Caption |
|---|---|---|---|
| 0-4s | Face camera or title screen | Day 6 of learning FastAPI. Today I built a Task Manager CRUD API. | Day 6: Task Manager API |
| 4-10s | Show project folder | Yesterday I learned CRUD with students. Today I practiced the same backend pattern with tasks. | Repeating CRUD builds skill |
| 10-18s | Show `TaskCreate` and `TaskUpdate` | I separated create and update schemas so each endpoint accepts the right data. | Cleaner schemas |
| 18-27s | Show `/tasks` endpoints in Swagger | The API can create, list, filter, read one, replace, partially update, and delete tasks. | Full CRUD routes |
| 27-36s | Test POST and GET | I used `201 Created` when a task is created and `GET` to retrieve tasks. | Better status codes |
| 36-45s | Test query filter | I added filtering with `completed=true` or `completed=false`. | Query filtering |
| 45-55s | Test PATCH and DELETE | I also practiced `PATCH` for partial updates and `DELETE` for removing a task. | PATCH and DELETE |
| 55-60s | Show Git branch or commit | Day 6 is committed to its own branch and merged into main. | Branch, commit, merge |

## Voiceover Script

```text
Day 6 of my FastAPI backend journey.

Today I built a Task Manager CRUD API.

Day 5 taught me the CRUD pattern with students. Today I repeated the same idea with tasks, because repetition is how backend concepts become real skill.

This API can create tasks, get all tasks, filter tasks by completed status, get one task, replace a task, partially update a task, and delete a task.

I also learned cleaner backend habits.

I used status code 201 when a task is created, 404 when a task is missing, and 400 when a user sends an empty partial update.

I separated create and update schemas with Pydantic, and I used a helper function to avoid repeating task lookup logic in every route.

The data is still in memory for now, but the API structure is getting closer to how real backend systems are designed.

Day 6 complete. CRUD is becoming muscle memory.
```

## B-roll Checklist

- Show branch: `day-06`
- Show folder: `day-06-task-manager-crud`
- Show `TaskCreate` and `TaskUpdate`
- Show `find_task()` helper
- Show Swagger `/tasks` routes
- Create one task
- Filter tasks by `completed=false`
- Update with `PATCH`
- Delete task
- Show Git commit or GitHub branch

## Render Note

The final vertical video render should be generated after confirming:

- Mood
- Light or dark canvas
- Brand colors or visual references
