from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import schemas
from service import TaskService

router = APIRouter(prefix="/api", tags=["Tasks"])
task_service = TaskService()

@router.get("/", response_model=list[schemas.TaskResponse], status_code=201)
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    return await task_service.get_all_tasks(db)

@router.post("/", response_model=schemas.TaskResponse, status_code=201)
async def create_task(data: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_service.create_task(db, data)