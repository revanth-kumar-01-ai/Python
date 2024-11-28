MAX = 20
fact = [1] * (MAX + 1)

for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i 

def getFact(n):
    if n > MAX:
        raise ValueError(f'Factorial for {n} is not precomputed MAX ={MAX}')
    return fact[n]

factorial = getFact(5)
print(factorial)