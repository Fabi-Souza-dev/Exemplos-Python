import random

num = [random.randint(0,7) for _ in range(8)]
    
print('Números sorteados: ')
print(*num)