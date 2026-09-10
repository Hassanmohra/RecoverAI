from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router

APP_NAME = "RecoverAI"
VERSION = "0.1.0"

app = FastAPI(
    title=APP_NAME,
    description="AI-Powered Mobile Data Recovery & Digital Forensics Platform",
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "name": APP_NAME,
        "version": VERSION,
        "status": "running",
        "message": "RecoverAI backend is online",
    }


@app.get("/api")
async def api_info():
    return {
        "name": APP_NAME,
        "version": VERSION,
        "api": "v1",
        "status": "operational",
    }
