def Factorial(n):
    if n <= 1:
        return n
    return n * Factorial(n - 1) 

fact = Factorial(5)
print(fact)


