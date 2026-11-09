from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Task

class TaskRepository:
    async def get_all_tasks(self, db: AsyncSession) -> list[Task]:
        response = await db.execute(select(Task))
        return list(response.scalars().all())

    async def create_task(self, db: AsyncSession, data: Task) -> Task:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    async def delete_task(self, db: AsyncSession, id: int) -> bool:
        response = await db.execute(select(Task).where(Task.id == id))
        task_row = response.scalars().first()
        if task_row:
            await db.delete(task_row)
            await db.commit()
            return True
        return False