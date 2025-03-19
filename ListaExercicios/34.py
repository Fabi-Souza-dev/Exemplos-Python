print("\033[0;30;46m-=-=-=-=-=-=-=-=-=-=-=-=-= IMC -=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")

nome = str(input("Nome: "))
peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobre Peso")
elif imc >= 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")



