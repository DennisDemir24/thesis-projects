#  en222yu

from fastapi import FastAPI, HTTPException

from model import Character
from performance import PerformanceMiddleware


from database import (
    fetch_one_character,
    fetch_all_characters,
    create_character,
    update_character,
    remove_character,
)

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add performance middleware
app.add_middleware(PerformanceMiddleware)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/characters/")
def get_character():
    response = fetch_all_characters()
    return response

@app.get("/character/{id}", response_model=Character)
def get_character_by_id(id):
    response = fetch_one_character(id)
    if response:
        return response
    raise HTTPException(404, f"There is no character with the id {id}")

@app.post("/character/", response_model=Character)
def post_character(character: Character):
    response = create_character(character.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/character/{id}/", response_model=Character)
def put_character(
                        id: int,
                        status: str,
                        image: str,
                        url: str
                        ):
    response = update_character(id, status, image, url)
    if response:
        return response
    raise HTTPException(404, f"There is no character with the id {id}")

@app.delete("/character/{id}")
def delete_character(id):
    response = remove_character(id)
    if response:
        return "Successfully deleted character"
    raise HTTPException(404, f"There is no character with the id {id}")


