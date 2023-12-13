from infra.repository.usuario_repository import UsuarioRepository

repo = UsuarioRepository()

repo.insert('Henrique','10/10/2023')

data = repo.select()

print(data)