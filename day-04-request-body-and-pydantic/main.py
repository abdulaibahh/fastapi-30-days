from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#PYDANTIC MODEL
class Student(BaseModel):
    name: str
    age: int
    course: str

#HOME ROUTE
@app.get("/")
async def home():
    return {"message": "Day 4 - Request Body and Pydantic"}


#CREATE STUDENT
@app.post("/students")
async def create_student(student: Student):
    return {
        "message": "Student created succsessfully",
        "student_data": student
    } 


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    return {
        "meassage": f"Stydent with ID {student_id} updated successfully",
        "updated_data": student 
    }




