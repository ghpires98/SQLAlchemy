from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker


# Configurações
engine = create_engine('mysql+pymysql://root:Neosaldina2021@172.20.0.2:3306/sys_ceu')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)

    def __repr__(self):
        return f"Usuario [id={self.nome}, data_nacimento{self.data_nascimento})"

# SQL

# Insert

data_insert = Usuario(nome='Caroline', data_nascimento=('15/05/1990'))
session.add(data_insert)
session.commit()

# delete

session.query(Usuario).filter(Usuario.nome== "Gustavo").delete()
session.commit()

# update

session.query(Usuario).filter(Usuario.nome == "Gustavo").update({"nome": "Henrique"})

# Select
data = session.query(Usuario).all()
print(data)

session.close