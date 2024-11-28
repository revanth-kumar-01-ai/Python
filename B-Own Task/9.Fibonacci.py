# Fibonacci Sequence

num = int(input("Enter the number: "))
first = 0
second = 1
print(0)
for i in range(0, num):
    second = first + second
    print(second)
    first, second =  second, first