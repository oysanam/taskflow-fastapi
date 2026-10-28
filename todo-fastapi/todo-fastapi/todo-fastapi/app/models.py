from datetime import datetime, date
from typing import Optional
from sqlalchemy import String, Boolean, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(String(1000), default=None)
    priority: Mapped[str] = mapped_column(String(10), default="medium")
    category: Mapped[str] = mapped_column(String(50), default="General")
    due_date: Mapped[Optional[date]] = mapped_column(Date, default=None)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)