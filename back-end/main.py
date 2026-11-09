from fastapi import FastAPI
from database import engine, Base
from controller import router as task_router

app = FastAPI(title="API de tasks")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(task_router)