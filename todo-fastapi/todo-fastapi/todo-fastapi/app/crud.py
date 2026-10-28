from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas


def get_todos(db: Session, done: Optional[bool] = None, search: Optional[str] = None):
    query = db.query(models.Todo)
    if done is not None:
        query = query.filter(models.Todo.done == done)
    if search:
        query = query.filter(models.Todo.title.ilike(f"%{search}%"))
    return query.order_by(models.Todo.created_at.desc()).all()


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def create_todo(db: Session, data: schemas.TodoCreate):
    todo = models.Todo(**data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo: models.Todo, data: schemas.TodoUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: models.Todo):
    db.delete(todo)
    db.commit()