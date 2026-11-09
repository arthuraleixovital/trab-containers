from pydantic import BaseModel
import datetime

class TaskCreate(BaseModel):
    titulo: str
    descricao: str

class TaskDelete(BaseModel):
    id: int

class TaskUpdate(BaseModel):
    titulo: str
    descricao: str
    concluida: bool
    data_conclusao: datetime.datetime | None

class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool
    data_criacao: datetime.datetime
    data_conclusao: datetime.datetime | None
    class Config:
        from_attributes = True