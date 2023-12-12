from infra.repository.usuario_repository import UsuarioRepository

repo = UsuarioRepository()

data = repo.select()

print(data)