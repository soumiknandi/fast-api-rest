from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    message: str
    class Config:
        from_attributes = True


class AddTodo(TodoBase):
    class Config:
        from_attributes = True
        
class GetTodo(TodoBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True