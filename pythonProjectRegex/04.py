https = str(input("Digite a URL para validação: "))

if (https.startswith("https://") and https.endswith(".com")):
    print("URL válida")
else:
    print("URL inválida")


