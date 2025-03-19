def somar(): # não passamos parametros
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    soma = n1 + n2
    
    return f"A soma {soma}" # o return está rsendo usado para retornar o valor da soma

resultado = somar()
print(resultado)