from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.features.students import models, schems   
from typing import List

#create router instance
router = APIRouter(
    prefix = "/students",
    tags = ["Students"]
)

#student registration endpoint
@router.post("/", response_model=schems.studentResponse, status_code=status.HTTP_201_CREATED)

#create student function
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

#student getAll endpoint
@router.get("/", response_model=List[schems.studentResponse], status_code=status.HTTP_200_OK)

#get all students function
def get_all_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

#get with path parameter endpoint
@router.get("/{student_id}", response_model=schems.studentResponse, status_code=status.HTTP_200_OK)

#get student by id function
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

#update student endpoint
@router.put("/{student_id}", response_model=schems.studentResponse, status_code=status.HTTP_200_OK)

#update student function
def update_student(
    student_id: int,
    student: schems.studentUpdate,
    db: Session = Depends(get_db)
):
    existing_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not existing_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    #drop fields that are not request in frontend
    updated_fields = student.model_dump(exclude_unset=True)
    
    #update student details
    for key, value in updated_fields.items():
        setattr(existing_student, key, value)
    
    db.add(existing_student)
    db.commit()
    db.refresh(existing_student)
    return existing_student

#delete student endpoint
@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)

#delete student function
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    existing_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not existing_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    db.delete(existing_student)
    db.commit()

    return None