n = 0
fib = 1

for _ in range(17):
    fib, n = n, fib + n # n recebe o valor de fib, depois fib recebe a soma de fib + n
    print(f'[{fib}]', end=' ')
     
print('\n')   
print(*range(16), end=' ')