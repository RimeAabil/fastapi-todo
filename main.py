from typing import List, Optional
from enum import IntEnum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


api = FastAPI()

# GET, POST, PUT, DELETE

# GET: to get information from the server
# POST: to submit something new to the server
# PUT: change something in the server


# Synchronous vs asynchronous

'''
Synchronous API

How it works: The client sends a request and waits (is "blocked") until the server finishes processing and sends back a response.

Analogy: Imagine you’re at a coffee shop. You order a latte and stand at the counter waiting until the barista finishes making it before you do anything else.

Use case: When you need an immediate result, like fetching user details or verifying a password.

Downside: If the server takes too long, the client is stuck waiting and can’t move on to other tasks.

Asynchronous API

How it works: The client sends a request but doesn’t wait for the server to respond. Instead, it continues doing other work, and when the response is ready, the server notifies the client (via a callback, event, or polling).

Analogy: At the coffee shop, you order your latte, get a buzzer, and go sit down. When your coffee is ready, the buzzer rings — you don’t just stand and wait.

Use case: Long-running tasks like file uploads, video processing, or data analytics.

Benefit: The client stays responsive and efficient because it’s not blocked.
'''


# Defining pydantic schemas

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name : str = Field(..., 
                            min_lenght=3, 
                            max_length=512,
                            description='Name of the todo'
                            )
    
    todo_description : str = Field(...,
                                   description = 'Description of the todo'
                                   )

    priority : Priority = Field (default=Priority.LOW,
                                 description='Priority of the todo'
                                 )
    

class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    todo_id: int = Field(...,
                         description = 'Unique identifier of the Todo'
                         )


# Optional: the fields are not all mandatory, we can update the name or the description without changing the other fields
class TodoUpdate(BaseModel):
    todo_name : Optional[str] = Field(None, 
                            min_lenght=3, 
                            max_length=512,
                            description='Name of the todo'
                            )
    
    todo_description : Optional[str] = Field(None,
                                   description = 'Description of the todo'
                                   )

    priority : Optional[Priority] = Field (None,
                                 description='Priority of the todo'
                                 )

    




all_todos = [
    Todo(
        todo_id=1,
        todo_name="Workout",
        todo_description="Complete a 1-hour gym session focusing on strength and cardio",
        priority=Priority.MEDIUM
    ),
    Todo(
        todo_id=2,
        todo_name="Reading",
        todo_description="Read 10 pages of a personal development or technical book",
        priority=Priority.LOW
    ),
    Todo(
        todo_id=3,
        todo_name="Grocery Shopping",
        todo_description="Buy weekly groceries including fruits, vegetables, and essentials",
        priority=Priority.HIGH
    ),
    Todo(
        todo_id=4,
        todo_name="Exam Preparation",
        todo_description="Review key chapters and solve past exam papers for 2 hours",
        priority=Priority.HIGH
    ),
    Todo(
        todo_id=5,
        todo_name="Meditation",
        todo_description="Practice guided meditation for 20 minutes to relax and refocus",
        priority=Priority.LOW
    )
]




@api.get('/')  # @api.get('path to endpoint')
def index():
    return {"message": "Hello world"}


# localhost: 9999/todos/2

@api.get('/todos/{todo_id}', response_model = Todo)   # @api.get('path parameter') 
def get_todo(todo_id : int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    
    raise HTTPException(status_code=404, detail='To do not found')


@api.get('/todos', response_model= List[Todo])    
def get_todos():
    return all_todos


# Query parameter : localhost:9999/todos?first_n=3

@api.get('/todos', response_model = List[Todo])    
def get_top_n(first_n : int):  # gotta specify the types 
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    

@api.post('/todos', response_model= Todo)
def create_todo(todo : TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1

    new_todo = Todo(
                    todo_id = new_todo_id,
                    todo_name = todo.todo_name,
                    todo_description = todo.todo_description,
                    priority= todo.priority)

    all_todos.append(new_todo)

    return new_todo


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id : int , updated_todo : TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    
    raise HTTPException(status_code=404, detail='To do not found')  # 404 -> not found


@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id : int):
    for index, todo in enumerate(all_todos): 
        if todo.todo_id== todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
        
    raise HTTPException(status_code=404, detail='To do not found')