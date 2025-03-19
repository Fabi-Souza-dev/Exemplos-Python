inicio = int(input("Digite um valor para começar: "))
incre = int(input("Digite o incremento: "))
fim = int(input("Digite o valor do fim: "))

print(f"\nO programa inicia {inicio} indo até {fim}, incrementando de {incre}\n")
for i in range(inicio, fim+1, incre):
    print(i, end=" ")
