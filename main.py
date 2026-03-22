from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from google.api_core.exceptions import Redirection
from starlette.responses import HTMLResponse, RedirectResponse

from models import  Base
from database import engine
from routers.auth import router as auth_router
from routers.todo import router as todo_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url="/todo/todo-page", status_code=302)

app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)
