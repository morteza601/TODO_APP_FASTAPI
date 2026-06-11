from sqlalchemy import Integer, Text, String, Column, Boolean, func, DateTime
from core.database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    descreption = Column(String(500), nullable=True)
    is_completed = Column(Boolean, default=False)

    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )
