from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from database import get_db
import todo
import schema
from typing import List
from starlette import status
import database

app = FastAPI()
router = APIRouter(prefix='/todos', tags=['Todos'])

todo.Base.metadata.create_all(bind=database.engine)


@app.get("/", name="Hello World")
def root():
    return {"message": "Hello World"}



@router.post('/', name="Add a todo", status_code=status.HTTP_201_CREATED, response_model=schema.GetTodo)
def add_a_todo(new_todo:schema.AddTodo, db:Session = Depends(get_db)):
    
    temp_todo = todo.Todo(**new_todo.model_dump())
    db.add(temp_todo)
    db.commit()
    db.refresh(temp_todo)
    
    return temp_todo



@router.put('/todos/{id}', name="Update a todo by id", response_model=schema.GetTodo)
def update_a_todo(update_post:schema.AddTodo, id:int, db:Session = Depends(get_db)):

    temp_todo =  db.query(todo.Todo).filter(todo.Todo.id == id)

    if temp_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    temp_todo.update(update_post.model_dump(), synchronize_session=False)
    db.commit()


    return  temp_todo.first()



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_a_todo(id:int, db:Session = Depends(get_db)):

    temp_todo = db.query(todo.Todo).filter(todo.Todo.id == id)


    if temp_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    temp_todo.delete(synchronize_session=False)
    db.commit()




@router.get("/", name="Get all todos", response_model=List[schema.GetTodo])
def get_all_todos(db:Session = Depends(get_db)):
    
    return db.query(todo.Todo).all()



@router.get("/{id}", name="Get a todo by id", response_model=schema.GetTodo)
def get_one_todo(id:int, db:Session = Depends(get_db)):
    temp_todo = db.query(todo.Todo).filter(todo.Todo.id == id).first()
    
    if temp_todo is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    return temp_todo


app.include_router(router)