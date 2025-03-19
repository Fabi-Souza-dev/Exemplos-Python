class Restaurante:
    def __init__(self, nome, categoria, ativo, rodizio):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.rodizio = rodizio

restaurante_tare = Restaurante('Fruts Ninja', 'Sushi', 'Ativo', 'Sim')

print(f'Nome: {restaurante_tare.nome} | Categoria: {restaurante_tare.categoria} | Status: {restaurante_tare.ativo} | Rodízio: {restaurante_tare}')