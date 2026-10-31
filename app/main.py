
from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import auth, notes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Notes API",
    description="""
    A secure REST API for managing personal notes.

    """,
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/", tags=["General"], summary="Check API status")
def home():
    return {
        "message": "Secure Notes API is running!",
        "status": "healthy",
        "version": "1.0.0"
    }
