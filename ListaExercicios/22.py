import  datetime

print("-=-=-=-=-=-=-=-= Alistamento -=-=-=-=-=-=-=-=")
nome = str(input("Digite seu nome: "))
ano = int(input("Digite o ano que nasceu: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade >= 18:
    print(f"\n{nome} com a idade {idade}, já tem permissão para o alistamento!")
    print(f"Já é possivel se alistar, já há {idade - 18} anos")
elif idade < 18:
    print(f"\n{nome} não tem permissão para o alistamento!")
    print(f"Faltam {18 - idade} anos para pode ser alistar!")
else:
    print("Valor inválido!")
