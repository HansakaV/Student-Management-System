from sqlalchemy import Column, Integer, String , Boolean
from app.core.database import Base
from datetime import datetime

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    joined_date = Column(String, default=datetime.utcnow().isoformat())