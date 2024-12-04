import math
divisors = []
num = 36 

# first 
# for i in range(1, num + 1):
#     if num % i == 0:
#         divisors.append(i)

# print(divisors)

# second 
sqrtN = int(math.sqrt(num))
for i in range(1, sqrtN + 1):
    if num % i == 0:
        divisors.append(i)
    
        if i != num // i:
            divisors.append(num // i)
            
print(divisors)