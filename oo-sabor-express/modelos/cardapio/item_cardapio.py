from abc import ABC, abstractclassmethod # importadando de um pacote, um método abstrato

class ItemCardapio(ABC):
    def __init__(self, nome, preco): 
        self._nome = nome
        self._preco = preco
        
    @abstractclassmethod
    def aplicar_desconto(self):
        pass