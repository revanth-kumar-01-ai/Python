# Calculate GCD (Greatest Common Divisor)
firstNum = 48
secondNum = 18

def GCD(x, y):
    if y == 0:
        return x 
    else:
        return GCD(y, x%y)

num = GCD(firstNum, secondNum)

# 48 18
# 18 12
# 12 6
# 6 0

print(num)
