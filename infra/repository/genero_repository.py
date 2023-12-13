from infra.configs.connection import DBConnectionHandler
from infra.entities.usuarios import Usuario

class UsuarioRepository():
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Usuario).all()
            return data