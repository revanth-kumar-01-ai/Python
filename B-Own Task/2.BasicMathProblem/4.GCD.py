a = 12
b = 9

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

res = GCD(b, a)
print(15 % 20)


