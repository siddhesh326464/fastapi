from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def user_login(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.post("/login")
def login(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.get("/")
def employeelist(request:Request):
    return templates.TemplateResponse("employeelist.html",{"request":request})