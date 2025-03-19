'''
n = 0
fib = 1

for _ in range(10):
    fib, n = n, fib + n # n recebe o valor de fib, depois fib recebe a soma de fib + n
    print('A sequência de Fibonacci é: ', fib) 
    
 
    '''
fib = 1  
n = 0
num = int(input("Digite o valor: "))
print(f'Fibonacci {num}\n')
for i in range(1,num+1):
    fib, n = n, fib + n
    print(fib, end=" ")