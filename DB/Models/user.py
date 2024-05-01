import enum
from ..db_setup import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from .mixins import Timestamp


class Role(enum.IntEnum):
    teacher = 1
    student = 2

class User(Timestamp, Base):
    __tablename__ = "users"
    # columns of table
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role)) # 1 for teacher, 2 for student
    is_active = Column(Boolean, default=False)
    
    profile = relationship("Profile", back_populates="owner", uselist=False) # one to one relationship with profile table
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship("CompletedContentBlock", back_populates="student")

class Profile(Timestamp, Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # foreign key to users table
    
    owner = relationship("User", back_populates="profile") # one to one relationship with user table