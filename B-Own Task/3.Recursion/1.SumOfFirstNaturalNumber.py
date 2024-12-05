def NaturalNumber(n):
    if n <= 1:
        return n
    return n + NaturalNumber(n - 1)

res = NaturalNumber(5) 
print(res)