from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    fk_genero = Column(Integer, ForeignKey=("genero.id"))

    def __repr__(self):
        return f"Usuario [id={self.nome}, data_nacimento{self.data_nascimento})"
