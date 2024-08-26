from fastapi import FastAPI
from app.interfaces.controllers.post_controller import router as post_router
from app.interfaces.controllers.user_controller import router as user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(post_router)
