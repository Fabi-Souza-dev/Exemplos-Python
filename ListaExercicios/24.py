print("-=-=-=-=-=-=-=-=-= Passagens  -=-=-=-=-=-=-=-=-=")

ticket = float(input("Digite a distância a ser percorrida: "))

if (ticket <= 200):
    print(f"O valor da passagem será R$ {ticket * 0.50}")
else:
    print(f"O valor da passagem será R$ {ticket * 0.45}")

