import random

print("-=-=-=- Bem-vindo ao JoKenPo! -=-=-=-")

while True:
    text = ("pedra", "papel", "tesoura")
    resp = str(input("\nEscolha entre Pedra, Papel ou Tesoura: ")).strip().lower()
    aleatorio = random.choice(text)

    if resp not in text:
        print("Opção Inválida")
        continue

    if resp == aleatorio:
        print(aleatorio)
        print("Empate !!!")

    elif (resp == "pedra" and aleatorio == "tesoura") or (resp == "papel" and aleatorio == "pedra") or (resp == "tesoura" and aleatorio == "papel"):
        print(aleatorio)
        print("Você Ganhouu !!")

    else:
        print(aleatorio)
        print("Você perdeu !!!")

    cont = input("\nDeseja continuar [S/N]?\n").strip().lower()
    if (cont == "n"):
        print("Encerrado !!!")
        break