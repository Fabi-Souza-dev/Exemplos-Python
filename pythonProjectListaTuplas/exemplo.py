"""" SLICING

    permite o fatiamneto, determinando o seu inicio, fim, passo
    estrutura do slicing
    [inicio:fim:passo]

    neste caso o valor do fim, sera o valor anterior ele na lista
    em python o último valor a ser pego, é o antecessor a ele

    """
print("SLICING")
lista = [10, 20, 30, 40]
print(lista[1:3])

tupla = (10, 20, 30, 40)
print(tupla[1:3])
print("\n")

"""" OPERADOR IN

    permite a verificar se um elemento esta presente em uma lista ou tupla,
    retornando TRUE ou False

"""

print("OPERADOR IN")
lista = [10, 20, 30, 40]
print(20 in lista) # TRUE
print(40 in lista) # TRUE

tupla = (10, 20, 30)
print(20 in tupla) # TRUE
print(40 in tupla) # FALSE
print("\n")

""" MANIPULACAO DE LISTA

    método .pop()
    remove e torna o elemento da posiçao indicada
    
    neste caso o item removido será o 2
"""
print("MANIPULACAO DE LISTA")
lista = [1, 2, 3]
print(lista.pop(1))
print(lista)
print("\n")

""" ITERAÇÃO SOBRE ELEMENTOS

    Outra ação que podemos fazer tanto com tuplas quanto com listas é 
    percorrer todos os elementos para verificar quais são.
    
"""
print("ITERAÇÃO SOBRE ELEMENTOS")
lista = [1, 2, 3, 4]
for item in lista: # o for esta percorrendo a lista e a partir disso, todos os item que tem na lista passa para o item
    print(item, end="") # o end=" " serve para formatar a saída, e deixar em formato de lista horizontal


print("\n")
""" DESEMPACOTAMENTO

    desempacotamento é uma técnica que permite atribuir os valores de uma tuplas ou 
    lista a variáveis de forma mais prática 
"""
print("DESEMPACOTAMENTO")
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)

lista = [10, 20, 30]
x, y, z = lista # atribuindo valores a cada variável
print(x, y, z) # uma variável para cada valor
print("\n")