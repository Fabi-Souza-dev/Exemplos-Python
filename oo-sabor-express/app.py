from modelos.restaurante import Restaurante # IMPORTA DADOS DO ARQUIVO RESTAURANTE CRIADO NA PASTA MODELOS
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# #restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
sobremesa_pudin = Sobremesa('Pudin', 3.0, 'Sobremesa', 200, 'A Melhor Sobremesa do mundo !')
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
sobremesa_pudin.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudin)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()
    
    ''''
restaurante_praca = Restaurante('Praça', 'Gourmet') # NOVA INSTÂNCIA
#restaurante_praca.nome = 'Bistrô' # ATRIBUIÇÃO DE VALOR 
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
restaurante_pizza._ativo = True
Restaurante.listar_restaurante()
'''