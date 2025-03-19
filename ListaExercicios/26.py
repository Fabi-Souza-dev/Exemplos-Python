print("-=-=-=-=-=-=-=-=- ATIVIDADE 26 -=-=-=-=-=-=-=-=-")
##maior = int
while True:
    n1 = int(input("\nDigite um valor: "))
    n2 = int(input("Digite outro valor: "))

    if (n1 > n2):
        print("O primeiro número maior é: ",n1,"\nO segundo maior é: ",n2)
    elif n1 == n2 or n2 == n1:
        print("Não existe número maior. \n",n1," é igual a ",n2 )
    else:
        print("O primeiro número maior é: ",n2, "\nO segundo maior é: ",n1)

    s = input("\nDigite se deseja continuar: " + "[S/N]").strip().lower()
    if s == 'n':
        print("Encerrado...")
        break