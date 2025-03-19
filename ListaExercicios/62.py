idades = [] # criar uma lista para armazenar as idades
while True:
    idade = int(input("\nDigite a sua idade: "))
    idades.append(idade) # adicionando o valor da idade em uma lista
    

    
    cont = str(input("\nDeseja Continuar: [S/N]")).casefold()
    if cont == 'n':
        print("Programa Encerrado!")
        break

quantidade = len(idades)
media = sum(idades) / quantidade if quantidade > 0 else 0
maior = sum(1 for idade in idades if idade >= 21) # um sum para somar a quantidade de idades, depois um for criado para percorrer a lista de idades criada no começo para identidiar as idades

print(f"\nA quatidade de idades digitadas foi: {quantidade}")
print(f"A média é das idades digitadas é: {media:.2f}")
print(f"Pessoas com 21 ou mais: {maior}")


    