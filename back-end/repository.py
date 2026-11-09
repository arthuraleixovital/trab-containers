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