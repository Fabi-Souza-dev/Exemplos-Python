num = [10,5,8,3,7]
soma = 0
try:
    for numero in num:
        soma += numero
        print(f'A soma de todos o valor é {numero}')
    
    print(f'\nA soma dos valores é {soma}')
        
except Exception as e:
    print('Valor Inválido!')