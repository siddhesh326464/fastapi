from pydantic import AnyHttpUrl, EmailStr, validator
from typing import List, Optional, Union
from pydantic import BaseSettings

class Settings(BaseSettings):
    MSG_DATA_EXISTS = "User is already exist"
    DB_NAME : str 
    DB_HOST : str
    DB_USER : str
    DB_PASSWORD : str
    DB_PORT : str
    authjwt_secret_key: str 
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False
    MSG_DATA_DEPT_EXISTS = "Department for this name does not exist"
    class Config:
        env_file = ".env"

settings = Settings()