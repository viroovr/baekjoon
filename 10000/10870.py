fib = [-1] * 21
fib[0] = 0
fib[1] = 1


def fibonacci(n):
    if fib[n] != -1:
        return fib[n]
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]


print(fibonacci(int(input())))
