lista = []
pares = [] # guarda os numeros pares
posicao = [] # guarda as posições do indice

for i in range(2):
    num = int(input("Digite os números: "))
    lista.append(num)

    if num % 2 == 0: # condição para ver se o resto da divisão é zero
        pares.append(num) # recebe os valores da condição
        posicao.append(i) # recebe os indices do for
        
    
print(f"Números pares: {pares}")
print(f"Foram digitados na posição {posicao}")
    