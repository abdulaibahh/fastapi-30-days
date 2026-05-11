from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import ClassVar, List

app = FastAPI()


#STUDENT MODEL
class Student(BaseModel):
    name: str
    age: int
    course: str


students: ClassVar[List[dict]] = []

#HOME ROUTE
@app.get("/")
async def home():
    return {"message": "Day 5 - CRUD API"}


#CREATE STUDENT
@app.post("/students")
async def create_student(student: Student):
    student_data = student.dict()

    student_data["id"] = len(students) + 1
    students.append(student_data)
    return {
        "message": "Student created successfully",
        "student": student_data
    }


#GET ALL STUDENTS
@app.get("/students")
async def get_students():
    return {
        "students":students
        }


#GET SINGLE STUDENT
@app.get("/students/{students_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {"student": student}

    raise HTTPException(status_code=404, detail="Student not found")


#UPDATE STUDENT
@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):

    for student in students:
        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return {
                "message": "Student updated successfully", 
                "student": student
                }

    raise HTTPException(status_code=404, detail="Student not found")

#DELETE STUDENT
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:

            students.remove(student)
            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Student not found")

