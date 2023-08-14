n = int(input())
fib = [-1] * 92
fib[0] = 0
fib[1] = 1
for i in range(0, n - 2):
    fib[i + 2] = fib[i] + fib[i + 1]
print(fib)
print(fib[n - 1])
