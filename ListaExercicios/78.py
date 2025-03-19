lista = [] # declarei a lista
nao_multiplos = [] 
multiplos = []


for i in range(8): # for  para determinar o final
    num = int(input(f"Digite os número {i}: ")) # criei uma nova variável para o usuario usar para inserir o valor
    lista.append(num) # adicionando o valor digitado nos num e na lista
    
    if num % 10 != 0: # condição para verificar se não é multiplo de 10
        nao_multiplos.append(num)
    else:
        multiplos.append(num)        
    
print(f"\nOs números digitados {lista}")
print(f"Números não multiplos : {nao_multiplos}")
print(f"Números multiplos : {multiplos}")