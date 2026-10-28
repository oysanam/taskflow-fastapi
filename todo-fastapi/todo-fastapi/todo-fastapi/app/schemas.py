from datetime import datetime, date
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    priority: Literal["low", "medium", "high"] = "medium"
    category: str = Field(default="General", min_length=1, max_length=50)
    due_date: Optional[date] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    priority: Optional[Literal["low", "medium", "high"]] = None
    category: Optional[str] = Field(default=None, min_length=1, max_length=50)
    due_date: Optional[date] = None
    done: Optional[bool] = None


class TodoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    priority: str
    category: str
    due_date: Optional[date]
    done: bool
    created_at: datetime
