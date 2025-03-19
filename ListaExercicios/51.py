lista_prod = []

for i in range(3):
    produto = float(input(f"Qual o valor {i}: "))
    
    lista_prod.append(produto)
    
maior = max(lista_prod)
menor = min(lista_prod)

print(f"\nO maior valor digitado {maior}")
print(f"O menor valor digitado {menor}")