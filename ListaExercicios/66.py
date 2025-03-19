while True:
    num = int(input("Digite um valor: "))

    for i in range(11):
        print(f"{num} X {i} = {num * i}")
        
    cont = str(input("\nDeseja continuar: [S/N]")).casefold()
    if cont == 'n':
        print("\nPrograma Encerrado !")
        break