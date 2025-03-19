print("-=-=-=-=-=-=-=-=-= Triângulo -=-=-=-=-=-=-=-=-=")

while True:
    t1 = int(input("\nDigite o Lado 1: "))
    t2 = int(input("Digite o Lado 2: "))
    t3 = int(input("Digite o Lado 3: "))
    if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
        print("Pode formar um triângulo")
        if t1 == t2 and t2 == t3:
            print("Equilátero")
        elif t1 != t2 and t2 != t3 and t1 != t3:
            print("Escaleno")
        else:
            print("Isósceles")
    else:
        print("Não pode formar um triângulo")

    s = input("\nDeseja continuar ? [S/N]\n").strip().lower()
    if s == "n":
        print("Encerrado...")
        break
