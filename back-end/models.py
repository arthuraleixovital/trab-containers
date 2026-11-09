from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP
from database import Base
import datetime

class Task(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text)
    concluida = Column(Boolean, default=False)
    data_criacao = Column(TIMESTAMP, default=datetime.datetime.now().timestamp())
    data_conclusao = Column(TIMESTAMP)
