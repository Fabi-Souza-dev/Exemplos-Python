from exs.banco import Banco

class Agencia(Banco):
    def __init__(self,nome,endereco,numero):
        super().__init__(nome, numero)
        self._numero = numero 