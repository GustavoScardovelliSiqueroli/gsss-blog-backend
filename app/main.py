from fastapi import FastAPI
from app.interfaces.controllers.post_controller import router as post_router

app = FastAPI()
app.include_router(post_router)
