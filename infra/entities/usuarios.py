from infra.configs.base import Base
from sqlalchemy import Column, String

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)

    def __repr__(self):
        return f"Usuario [id={self.nome}, data_nacimento{self.data_nascimento})"
