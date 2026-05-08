from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Day 3 - Dynamic APIs"}


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": f"Student with ID {student_id} retrieved successfully"
    }


# @app.get("/products/{product_name}")
# async def get_product(product_name: str):
#     return {
#         "product": product_name
#     }


@app.get("/students")
async def list_students(limit: int = 10):
    return {
        "message": f"Returning {limit} students"
    }


@app.get("/search")
async def search_student(name: str, age: int):
    return {
        "name": name,
        "age": age
    }


@app.get("/users/{username}")
async def get_username(username: str):
    return {
        "username": username
    }

@app.get("/products/search")
async def search_product(category: str , price:int):
    return {
        "category": category,
        "max_price": price
    }

