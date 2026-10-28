from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])

@router.delete("/completed")
def clear_completed(db: Session = Depends(get_db)):
    return {"deleted": crud.clear_completed(db)}


@router.get("/", response_model=List[schemas.TodoOut])
def list_todos(done: Optional[bool] = None, search: Optional[str] = None,
               db: Session = Depends(get_db)):
    return crud.get_todos(db, done, search)


@router.post("/", response_model=schemas.TodoOut, status_code=201)
def create(data: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, data)


@router.get("/{todo_id}", response_model=schemas.TodoOut)
def read(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=schemas.TodoOut)
def update(todo_id: int, data: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, todo, data)


@router.delete("/{todo_id}", status_code=204)
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    crud.delete_todo(db, todo)