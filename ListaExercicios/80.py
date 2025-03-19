''' import random

num = [random.randint(0,7) for i in range(8)]
    
print('Números sorteados: ')
print(*num)

'''

import random

lista = [random.randint(1, 15) for _ in range(5)]
print(f"Lista gerada: {lista}")

chave = int(input("Digite uma numero: "))

posicoes = [i for i, num in enumerate(lista) if num == chave]


if posicoes:
    print(f"\nO número {chave} foi encontrado na lista!")
    print(f"Ele aparece na {len(posicoes)} vezes")
else:
    print(f"\nO número {chave} não foi encontrado na lista")