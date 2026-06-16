from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.features.students import models, schems   

#create router instance
router = APIRouter(
    prefix = "/students",
    tags = ["Students"]
)

#student registration endpoint
@router.post("/", response_model=schems.studentResponse, status_code=status.HTTP_201_CREATED)

def create_student(
    student: schems.studentCreate,
    db: Session = Depends(get_db)
):
    #check if email already exists
    exiting_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if exiting_student:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    #conver pydantic model to sqlalchemy model
    new_student = models.Student(**student.model_dump())
    
    #approve data to database
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    #return response to frontend
    return new_student
