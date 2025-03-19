def media(n1,n2):
    return (n1 + n2) / 2

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

md = media(nota1, nota2)

if md >= 7:
    print(f"A Média é {md}, 'Aprovado' ")
elif md >= 4:
    print(f"A Média é {md}, 'RECUPERÇÃO'")
else:
    print(f"A Média é {md}, 'REPROVADO'")
