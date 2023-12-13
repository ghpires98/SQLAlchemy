from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Genero(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True)
    genero = Column(String, nullable=False)    

    def __repr__(self):
        return f"Teste genero{self.genero})"