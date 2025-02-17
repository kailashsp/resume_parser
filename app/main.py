from fastapi import FastAPI
from app.routers import ranking_criteria, resume_scoring 

app = FastAPI(
    title="Resume Ranking API",
    description="API for extracting ranking criteria and scoring resumes",
    version="1.0.0",
)

app.include_router(ranking_criteria.router)
app.include_router(resume_scoring.router)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint that welcomes users to the Resume Parser API.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to Resume Parser!"}