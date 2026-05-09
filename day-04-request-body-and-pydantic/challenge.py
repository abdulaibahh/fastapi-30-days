from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Teacher(BaseModel):
    name: str
    department: str
    salary: float
    email: None | str = None


@app.post("/teachers")
async def create_teacher(teacher: Teacher):
    return {
        "message": "Teacher created succsessfully",
        "teacher_data": teacher 
    }


