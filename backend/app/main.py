from fastapi import FastAPI
from app.routes import tracker

app = FastAPI(title="GPS Tracker API")

# Register routes
app.include_router(tracker.router, prefix="/tracker", tags=["tracker"])

@app.get("/")
def home():
    return {"msg": "Welcome to GPS Tracker API"}
