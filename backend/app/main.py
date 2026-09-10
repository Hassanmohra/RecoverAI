from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

APP_NAME = "RecoverAI"
VERSION = "0.1.0"

app = FastAPI(
    title=APP_NAME,
    description="AI-Powered Mobile Data Recovery & Digital Forensics Platform",
    version=VERSION,
)

# Allow the frontend to communicate with the backend.
# During production, replace "*" with the actual frontend origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": APP_NAME,
        "version": VERSION,
    }
