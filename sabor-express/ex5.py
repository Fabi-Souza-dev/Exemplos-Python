n = int(input('Digite o numero que quer ver a tabuada: \n'))
print(f'\n\033[0;0;44m-=-=-=-=-=-=-=-= Tabuada {n} -=-=-=-=-=-=-=-=\033[m')
for tab in range(1,11):
    mult = n * tab
    print(f'{n} x {tab} = {mult}')