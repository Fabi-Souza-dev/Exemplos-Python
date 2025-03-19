print('-=-=-=-=-=-=-=-=-=-=- Repetição -=-=-=-=-=-=-=-=-=-=-')

#n = int(input('Digite um valor: '))

for i in range(30, 0, -1):
    if i % 4 == 0:
        print(f"[{i}]", end=" ")
    else:
        print(i, end=" ")