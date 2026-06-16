from fastapi import FastAPI
from app.core.database import engine, Base
from app.features.students import models
from app.features.students.router import router as student_router

#call alchemy to create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Student Management System",
    description = "Vertical Slice Architecture with FastAPI and SQLAlchemy",
    version = "1.0.0"
)

app.include_router(student_router)
@app.get("/")
def read_root():
    return {"status": "Healthy", "message": "Welcome to the Student Management System API!"}


