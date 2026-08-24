from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teacher"
    
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    group_id = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Teacher(id={self.teacher_id}, email={self.email})>"