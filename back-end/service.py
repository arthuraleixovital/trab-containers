from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models import Task
from schemas import TaskCreate
from repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    async def get_all_tasks(self, db: AsyncSession):
        return await self.repository.get_all_tasks(db)

    async def create_task(self, db: AsyncSession, data: TaskCreate):
        if data.titulo.strip() == "":
            raise HTTPException(status_code=422, detail="O título da task não pode ser vazio.")
        new_task = Task(titulo=data.titulo, descricao=data.descricao)
        return await self.repository.create_task(db, new_task)