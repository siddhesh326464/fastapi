from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from utils.database import DBConnection
import models
from api.emp.router import api_router
from apps.router import apps_router
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from config import settings
from fastapi.staticfiles import StaticFiles
app = FastAPI()

engine = DBConnection().getEngine()
app.mount("/static", StaticFiles(directory="static"), name="static")
models.Base.metadata.create_all(bind=engine)

    
# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return settings

# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(api_router)
app.include_router(apps_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")