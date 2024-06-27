from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.transcribe import transcribe_app
from routers.userlog import userlog_router

app = FastAPI()
app.title = "Cortitelas API"
app.version = "0.0.1"

# Configuración de CORS
origins = [
    "https://elasistenteia.com"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transcribe_app)
app.include_router(userlog_router)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Universal Learning API Cortitelas</h1>')
