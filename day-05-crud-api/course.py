from fastapi import FastAPI
from pydantic import BaseModel
from typing import ClassVar, List

app = FastAPI()

class Course(BaseModel):
    title: str
    duration: str
    instructor: str
    price: float
    is_active: bool

courses: ClassVar[List[dict]] = []

@app.post("/courses")
async def create_course(course: Course):
    course_data = course.dict()
    course_data["id"] = len(courses) + 1
    courses.append(course_data)
    return {
        "message": "Course created successfully",
        "course": course_data
    }

@app.get("/courses")
async def get_courses():
    return {
        "courses": courses
    }

@app.get("/courses/{course_id}")
async def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return {"course": course}

    raise HTTPException(status_code=404, detail="Course not found")

@app.put("/courses/{course_id}")
async def update_course(course_id: int, updated_course: Course):
    for course in courses:
        if course["id"] == course_id:
            course.update(updated_course.dict())
            return {
                "message": "Course updated successfully",
                "course": course
            }

    raise HTTPException(status_code=404, detail="Course not found")

@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return {"message": "Course deleted successfully"}

    raise HTTPException(status_code=404, detail="Course not found") 


