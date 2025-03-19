print("-=-=-=-=-=-=-=-=-= Promoção Exclusiva -=-=-=-=-=-=-=-=-=")
print("Homens ganham 5% de desconto")
print("Mulheres ganham 13% de desconto\n")

nome = str(input("Digite o nome do cliente: "))
sexo = str(input("Digite o genêro da pessoa: "))
preco = float(input("O valor da compra: "))

if (sexo.lower() == "feminino" or sexo.upper() == "FEMININO" or sexo == "Feminino"):
    print(f"\nA cliente {nome} gastou R$ {preco} reais")
    print(f"O desconto foi de R$ {(preco * 0.13):.2f} o valor total a ser pago é de R$ {preco - (preco * 0.13)}")
elif (sexo.lower() == "masculino" or sexo.upper() == "MASCULINO" or sexo == "Masculino"):
    print(f"\nO cliente {nome} gastou {preco} reais")
    print(f"O desconto foi de R$ {(preco * 0.05):.2f} o valor total a ser pago é de R$ {preco - (preco * 0.05)}")
else:
    print("Opção inválida!")