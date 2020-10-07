from ordenes import Peticion, Permiso, Usuario

permissions = [Permiso()]
usuario = Usuario("Mateo")
peticion = Peticion(ip="8.8.8.8", usuario=usuario, cliente="cliente2")
peticion.enviar([3, 2, 1])

# if __name__ == '__main__':
#     pass
