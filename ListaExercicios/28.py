print("-=-=-=-=-=-=-=-=- Calculo da Área -=-=-=-=-=-=-=-=-")

while True:
    larg = float(input("\nDigite a Largura: "))
    comp = float(input("Digite o Comprimento: "))

    area = larg * comp

    if area > 500:
        print("TERRENO VIP")
        print(f"A área é {area:.2f}")
    elif 100 <= area <= 500:
        print("TERRENO MASTER")
        print(f"A área é {area:.2f}")
    else:
        print("TERRENO POPULAR")
        print(f"A área é {area:.2f}")

    s = input("\nDeseja continuar: [S/N]").strip().lower()
    if s == 'n':
        print("Encerrado....")
        break
