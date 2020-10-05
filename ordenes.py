from typing import List


class Permiso(object):
    pass


class Usuario(object):
    pass


class Cliente(str):
    def __init__(self):
        super().__init__()


class Peticion:
    def __init__(self, ip: str = "", usuario: Usuario = None, cliente: Cliente = ""):
        self.ip: str = ip
        self.usuario = usuario
        self.cliente = cliente

    def __enviar(self):
        pass

    def enviar(self, validaciones: List[int]):
        """
            Autenticacion: 0\n
            IP: 1\n
            Cache: 2\n
            Saneador: 3\n
        """
        v = ConfiguracionValidacion.obtener_validador(validaciones)
        if v.validar(self):
            self.__enviar()


class Validacion:
    def validar(self, peticion: Peticion) -> bool:
        raise NotImplementedError


class ValidacionAutenticacion(Validacion):
    def validar(self, peticion: Peticion) -> bool:
        pass


class ValidacionSaneador(Validacion):
    def validar(self, peticion: Peticion) -> bool:
        pass


class ValidacionCache(Validacion):
    def validar(self, peticion: Peticion) -> bool:
        pass


class ValidacionIP(Validacion):
    def validar(self, peticion: Peticion) -> bool:
        pass


class Validador:
    def __init__(self, validaciones: [Validacion] = None):
        self.__validaciones = validaciones

    def validar(self, peticion: Peticion) -> bool:
        for v in self.__validaciones:
            if not v.validar(peticion):
                return False
        return True


class ConfiguracionValidacion:
    __validaciones_existentes = [ValidacionAutenticacion(),
                                 ValidacionIP(),
                                 ValidacionCache(),
                                 ValidacionSaneador()]

    @staticmethod
    def obtener_validador(validadores: List[int]) -> Validador:
        """
            Autenticacion: 0\n
            IP: 1\n
            Cache: 2\n
            Saneador: 3\n
        """
        validador_lista = []
        for v in validadores:
            validador_lista.append(ConfiguracionValidacion.__validaciones_existentes[v])
        return Validador(validador_lista)


