import random

print("-=-=-=- Bem-vindo ao Jogo da Sorte! -=-=-=-")
while True:
    for i in range():
        resp = int(input("\nEscolha um número de 1 a 5: "))
        pc = random.randint(1,5)

        if resp < 1 or resp > 5:
            print("Opção Inválida")
            continue

        if resp == pc:
            print("Você Acertouuu !!")
            print(pc)
        else:
            print("Você perdeu !!")
            print(pc)

        cont = input("\nDeseja Continuar [S/N]: \n")
        if (cont == "n"):
            print("Encerrado !!")
            break