import random

print("-=-=-=- Bem-vindo ao Jogo da Sorte! -=-=-=-")
for i in range(4):
    resp = int(input("\nEscolha um número de 1 a 10: "))
    pc = random.randint(1,10)

    if resp < 1 or resp > 10:
        print("Opção Inválida")
        continue

    if resp == pc:
        print("Você Acertouuu !!")
        print(pc)
    else:
        print("Você perdeu !!")
        print(pc)
