from fastapi import FastAPI, HTTPException
from model import Character
from performance import PerformanceMiddleware


from database import (
    fetch_one_character,
    fetch_all_characters
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




