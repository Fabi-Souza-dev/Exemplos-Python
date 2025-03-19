lista_idade = []
maior_18 = []
menor_5 = []

for i in range(10):
    idade = int(input(f"Digite a {i}: "))
    lista_idade.append(idade)
    
    if idade > 18:
        maior_18.append(idade)
    
    if idade < 5:
        menor_5.append(idade)

maior = max(lista_idade)

print("\033[0;30;45m -=-=-=-=-=-=-=-=-=-=-=-=-=- Idade -=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m")
print("\nLista de idades: ")
print(lista_idade, end=" ")
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"\nIdades maior que 18")
print(maior_18, end=" ")
print(f"\nIdades menor que 5")
print(menor_5, end=" ")
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"\nA maior idade digitada é {maior}")