#  en222yu

from fastapi import FastAPI, HTTPException

from model import Character

from database import (
    fetch_one_character,
    # fetch_all_characters,
    # create_character,
    # update_character,
    # remove_character,
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# @app.get("/characters/")
# async def get_character():
#     response = await fetch_all_characters()
#     return response

@app.get("/character/{id}", response_model=Character)
async def get_character_by_id(id):
    response = await fetch_one_character(id)
    if response:
        return response
    raise HTTPException(404, f"There is no character with the id {id}")

# @app.post("/character/", response_model=Character)
# async def post_character(todo: Todo):
#     response = await create_character(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")

# @app.put("/character/{id}/", response_model=Character)
# async def put_character(id: str, desc: str):
#     response = await update_character(id, desc)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no character with the id {id}")

# @app.delete("/character/{id}")
# async def delete_character(id):
#     response = await remove_character(id)
#     if response:
#         return "Successfully deleted todo"
#     raise HTTPException(404, f"There is no character with the id {id}")



