def Fibonacci(n, fib1, fib2):
    if n <= 0:
        return fib1 
    print(fib1, end=" ")
    return Fibonacci(n - 1, fib1 + fib2, fib1)

res = Fibonacci(6, 0, 1)
print(res)