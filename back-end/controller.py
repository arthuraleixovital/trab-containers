from fastapi import APIRouter, Depends, status
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

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    await task_service.delete_task(db, task_id)

@router.patch("/{task_id}", response_model=schemas.TaskResponse)
async def update_task(task_id: int, data: schemas.TaskUpdate, db: AsyncSession = Depends(get_db)):
    return await task_service.update_task(db, task_id, data)