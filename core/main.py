from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App Startup")
    yield
    print("App Shutdown")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_routes)
