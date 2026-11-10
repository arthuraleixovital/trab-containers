from pydantic import BaseModel
from typing import Optional
import datetime

class TaskCreate(BaseModel):
    titulo: str
    descricao: str

class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None
    data_conclusao: Optional[datetime.datetime] = None

class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool
    data_criacao: datetime.datetime
    data_conclusao: Optional[datetime.datetime]
    class Config:
        from_attributes = True