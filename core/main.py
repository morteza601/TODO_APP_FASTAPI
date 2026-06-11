from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes
from users.routes import router as users_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App Startup")
    yield
    print("App Shutdown")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_routes)
app.include_router(users_routes)
