import math
num = 153
num1 = num
NumLen = int(math.log(num, 10) + 1)
res = 0
while num != 0:
    a = num % 10 
    res = res + (a ** NumLen)
    num = num // 10

print(res == num1)
