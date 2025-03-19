import datetime

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

#print(f"Sua idade é {idade} anos")

if idade > 18:
    print(f"Com a {idade} você já pode votar")
else:
    print(f"Com a {idade} você não pode votar")
