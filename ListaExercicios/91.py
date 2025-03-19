def maior():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    
    if n1 > n2:
        print(f"O {n1} é maior que {n2}")
    elif n1 == n2:
        print("Não tem valor maior, os dois são iguais")
    else:
        print(f"{n2} e maior que {n1}")
        
    return n1, n2

maior()