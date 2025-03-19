lista = ["arroz, feijão, bolacha"]

adicionar = input("Digite o item que você quer verificar: ")

if adicionar in lista:
    print(f"O item {adicionar}já está disponível na despensa.")
else:
    print(f"O item {adicionar} precisa ser comprado.")


