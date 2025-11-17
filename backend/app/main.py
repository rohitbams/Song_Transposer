from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for audio download
app.mount("/ytdl_audio", StaticFiles(directory="/tmp/ytdl_audio"), name="ytdl_audio")

# Root endpoint
@app.get("/")
def root():
    return {"message": "API running"}

# Include API routes
app.include_router(api_router, prefix="/api")
