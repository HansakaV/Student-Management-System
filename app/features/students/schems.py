from pydantic import BaseModel
from typing import Optional

# Schemas for student model frontend to backend communication
class studentCreate(BaseModel):
    name:str
    age:int
    address:str
    email:str

#api response schema backend to frontend communication
class studentResponse(BaseModel):
    id:int
    name:str
    age:int
    address:str
    email:str
    is_active:bool
    joined_date:str

#allowd pyntic to read data  and convert to json
    class Config:
        from_attributes = True