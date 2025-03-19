import random
print("\033[0;30;45m -=-=-=-=-=-=-=-=-=-=-=-=-=- SORTEADOS -=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m")

maior5 = []
div = []
print("Sorteados")
for i in range(20):
    num = random.randint(0,10)
    print(num, end=" ")
    
    if num > 5:
        maior5.append(num)
        
    if num % 3 == 0:
        div.append(num)
    
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\nMaior que 5")    
print(maior5, end=" ")
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\nDivisivel por 3")
print(div, end=" ")

    







    
    


