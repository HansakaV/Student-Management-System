from fastapi import FastAPI
from app.core.database import engine, Base
from app.core.config import settings
from app.features.students.router import router as student_router

#call alchemy to create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Student Management System",
    description = "Vertical Slice Architecture with FastAPI and SQLAlchemy",
    version = "1.0.0",
    debug=settings.DEBUG_MODE
)

app.include_router(student_router)
@app.get("/")
def read_root():
    return {
        "status": "Healthy", 
        "app_name": settings.APP_NAME,
        "mode" : "Development" if settings.DEBUG_MODE else "Production"
    }


