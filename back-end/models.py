from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, func
from database import Base

class Task(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text)
    concluida = Column(Boolean, default=False)
    data_criacao = Column(TIMESTAMP, server_default=func.now())
    data_conclusao = Column(TIMESTAMP)
