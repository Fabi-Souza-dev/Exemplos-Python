class Carros:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
carro_cross = Carros('SUV', 'Prata', 2024)


print(f'Modelo: {carro_cross.modelo} | Cor: {carro_cross.cor} | Ano: {carro_cross.ano}')