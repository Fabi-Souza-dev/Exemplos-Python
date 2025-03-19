print("-=-=-=-=-=-=-=-= Ano Bissexto -=-=-=-=-=-=-=-=")
ano = int(input("Digite o ano: ")

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("Ano Bissexto")
else:
    print("Este ano não é Bissexto")