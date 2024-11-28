# Find Prime Numbers in a Range
startNum = 10
endNum = 20

def prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return True
    return False

for i in range(startNum, endNum+1):
    if not(prime(i)):
         print(i)
         

