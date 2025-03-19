while True:
    print('-=-=-=-=-=-=-=-=-=-=- Maior e Menor -=-=-=-=-=-=-=-=-=-=-')

    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))

    if n1 > n2:
        print(f"O valor {n1} é maior que {n2}")
    elif n1 == n2:
        print(f"Não há valor maior, os dois valores são iguais")
    else:
        print(f"O valor {n2} é maior que {n1}")
        
    cont = str(input("\nDeseja Continuar?  [S/N]\n")).strip().lower()
    if cont == 'n':
        print("Encerrado....")
        break
        