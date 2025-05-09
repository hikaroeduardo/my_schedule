from datetime import datetime, date, time
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    name: str = Field(max_length=50)
    username: str
    password: str = Field(max_length=60)
    status: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    tasks: List["Task"] = Relationship(back_populates="user")
    meetings: List["Meeting"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name_task: str = Field(max_length=50)
    task_date: date
    status: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    user: Optional["User"] = Relationship(back_populates="tasks")

class Meeting(SQLModel, table=True):
    __tablename__ = "meetings"

    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    subject_meeting: str = Field(max_length=20)
    location: str = Field(max_length=50)
    date_meeting: date
    meeting_start_time: time
    meeting_end_time: time
    status: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    user: Optional["User"] = Relationship(back_populates="meetings")