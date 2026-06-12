from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    auth,
    resume,
    job_match,
    skills,
    roadmap,
    interview,
    dashboard,
)

app = FastAPI(
    title="AI Placement Copilot API",
    description="Your Personal AI Career Coach",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(
    resume.router,
    prefix="/resume",
    tags=["Resume"],
)

app.include_router(
    job_match.router,
    prefix="/job-match",
    tags=["Job Match"],
)

app.include_router(
    skills.router,
    prefix="/skills",
    tags=["Skills"],
)

app.include_router(
    roadmap.router,
    prefix="/roadmap",
    tags=["Roadmap"],
)

app.include_router(
    interview.router,
    prefix="/interview",
    tags=["Interview"],
)

app.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"],
)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "AI Placement Copilot API running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }