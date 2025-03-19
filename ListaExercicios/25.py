print("-=-=-=-=-=-=-=-=-= Triângulo -=-=-=-=-=-=-=-=-=")

while True:
    t1 = int(input("\nDigite o Lado 1: "))
    t2 = int(input("Digite o Lado 2: "))
    t3 = int(input("Digite o Lado 3: "))
    if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
        print("Pode formar um triângulo")
    else:
        print("Não pode formar um triângulo")

    s = input("\nDeseja continuar ? [S/N]").strip().lower()
    if s == "n":
        print("Encerrado...")
        break
