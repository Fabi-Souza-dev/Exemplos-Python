num = []

while True:
    print("\nContador de Número")
    n = int(input("Digite um valor: "))
    num.append(n)
    
   
    cont = int(input("\nDigite 1111 para encerrar: "))
    if cont == 1111:
        print("\nPrograma Encerrado!")
        print(num, end=" ")
        print(f"\nO soma de é {sum(num)}")
        break
    