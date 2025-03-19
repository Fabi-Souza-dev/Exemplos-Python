
while True:
    print("\033[0;30;45m-=-=-=-=-=-=-=-=-=-=-=-=-= Aluguel de Carros -=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")
    print("\nTipos de Carros:")
    print("1 - Popular\n2 - Luxo")
    carro = int(input("\nEscolha o tipo de Carro:"))
    km = float(input("Quantos km foram percorridos: "))
    dias = int(input("Quantos dias foram alugados: "))

    if carro == 1:
        if km <= 100:
            aluguel = dias * 90
            print("\nCarro Popular")
            print(f"O valor do aluguel ficou R$ {aluguel + (km * 0.20)}, com o total de km {km} percorridos")
        else:
            aluguel = dias * 90
            print("\nCarro Popular")
            print(f"O valor do aluguel ficou R$ {aluguel + (km * 0.10)}, com o total de km {km} percorridos")
    elif carro == 2:
        if km <= 200:
            aluguel = dias * 150
            print("\nCarro de Luxo")
            print(f"O valor do aluguel ficou R$ {aluguel + (km * 0.30)}, com o total de km {km} percorridos")
        else:
            aluguel = dias * 150
            print("\nCarro de Luxo")
            print(f"O valor do aluguel ficou R$ {aluguel + (km * 0.25)}, com o total de km {km} percorridos")

    else:
        print("Opção Inválida !!")

    cont = str(input("\nDeseja Continuar?  [S/N]\n")).strip().lower()
    if cont == 'n':
        print("Encerrado....")
        break
