from utils.database import DBConnection
from typing import Generator
from sqlalchemy.orm import Session
from models import User

def get_db() -> Generator:
    db = DBConnection().getSession()
    try:
        yield db
    finally:
        db.close()


def get_current_user_id(current_user,db:Session):
    user = db.query(User).filter(User.username == current_user).first()
    if not user:
        return None
    return user