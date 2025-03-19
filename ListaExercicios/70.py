n = 0
fib = 1

for _ in range(10):
    fib, n = n, fib + n # n recebe o valor de fib, depois fib recebe a soma de fib + n
    print('A sequência de Fibonacci é: ', fib) 
    