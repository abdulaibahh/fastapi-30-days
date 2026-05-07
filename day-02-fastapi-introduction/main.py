from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Backend Mastery"}


@app.get("/about")
async def about():
    return {
        "course": "FastAPI Backend Mastery",
        "day": 2,
        "topic": "Introduction to FastAPI"
    }

@app.get("/contact")
async def get_contact():
    return {"email": "abdulai.bah.lafwol@gmail.com"}

@app.get("/status")
async def get_status():
    return {"status": "API is running"}

