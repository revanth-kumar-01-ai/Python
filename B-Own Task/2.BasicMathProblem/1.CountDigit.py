import math

# First solution 
# For loop O(n)
number = int(input("Enter the number: "))
count = 0
for i in str(number):
    count += 1

print(f'First Solution the number {number} has {count} digits.')

# Second solution
# Log O(n)
count = int(math.log(number, 10) + 1)
print(f'Second Solution the number {number} has {count} digits.')

