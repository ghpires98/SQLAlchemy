from infra.configs.connection import DBConnectionHandler
from infra.entities.usuarios import Usuario

class UsuarioRepository():
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Usuario).all()
            return data
    
    def insert(self, nome, data_nascimento):
            with DBConnectionHandler() as db:                 
                data_insert = Usuario(nome=nome, data_nascimento=data_nascimento)
                db.session.add(data_insert)
                db.session.commit()

    def delete(self, nome):
            with DBConnectionHandler() as db:                 
                db.session.query(Usuario).filter(Usuario.nome == nome).delete()
                db.session.commit()

    def update(self, nome):
            with DBConnectionHandler() as db:                 
                db.session.query(Usuario).filter(Usuario.nome == nome).update({"nome": nome})
                db.session.commit()
                                