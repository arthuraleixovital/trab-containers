from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models import Task
from schemas import TaskCreate, TaskUpdate
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

    async def delete_task(self, db: AsyncSession, id: int):
        deleted = await self.repository.delete_task(db, id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Task não encontrada.")

    async def update_task(self, db: AsyncSession, task_id: int, data: TaskUpdate):
        data_dict = data.model_dump(exclude_unset=True)
        if not data_dict:
            raise HTTPException(status_code=422, detail="Nenhum dado enviado para atualização.")
        task_updated = await self.repository.update_task(db, task_id, data_dict)
        if not task_updated:
            raise HTTPException(status_code=404, detail="Task não encontrada.")
        return task_updated