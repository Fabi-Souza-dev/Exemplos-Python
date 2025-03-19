num_list = []
while True:
    num = int(input("\nDigite um valor: "))
    num_list.append(num)
        
    cont = str(input("\nDeseja Continuar: [S/N]")).casefold()
    if cont == 'n':
        print("\nPrograma Encerrado!")
        break
    
soma = sum(num_list)
quantidade = len(num_list)
media = sum(num_list) / quantidade
pares = sum(1 for num in num_list if num % 2 == 0)
menor = min(num_list) if num_list else "Nenhum número foi digitado"


print(f"\nA soma de números digitados: {soma}")
print(f"A média é de : {media:.2f}")
print(f"O menor número digitado foi: {menor}")
print(f"A quantidade de números pares é {pares}")
