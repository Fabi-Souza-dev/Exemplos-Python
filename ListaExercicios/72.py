lista = []


for i in range(10):
    lista.append(i*5)
    #print(lista)
    
print(lista)
print(*range(10), end= '  ')