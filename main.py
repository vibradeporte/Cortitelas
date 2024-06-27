from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.transcribe import transcribe_app
from routers.userlog import userlog_router

app = FastAPI()
app.title = "Cortitelas API"
app.version = "0.0.1"


app.include_router(transcribe_app)
app.include_router(userlog_router)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Universal Learning API Cortitelas</h1>')
