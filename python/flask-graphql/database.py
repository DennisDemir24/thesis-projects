from sqlalchemy.orm import Session
from model import Character
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "sqlite:///./characters.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


def fetch_all_characters():
    with get_db() as db:
        characters = db.query(Character).all()
        return characters
