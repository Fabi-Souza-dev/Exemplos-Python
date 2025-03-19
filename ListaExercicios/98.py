def superSomador():
    n1 = int(input("Digite um valor para começar: "))
    n2 = int(input("Digite outro valor para finalizar: "))
    for i in range(n1, n2+1):
        print(i, end=" ")
           
    soma = sum(range(n1, n2+1))
    print(f"\nA soma é {soma}")
        
superSomador()