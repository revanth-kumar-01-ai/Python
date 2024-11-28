# Check for Armstrong Number
num = "153"
power = len(num)
armstrongNumber = 0
for i in num:
    armstrongNumber = armstrongNumber + (int(i) ** power)

if armstrongNumber == int(num):
    print("Is a armstrong number")
else:
    print("Is not a armstrong number")