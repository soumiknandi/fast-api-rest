from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from datetime import datetime


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    message = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),default=datetime.now(), server_default=text('now()'))
