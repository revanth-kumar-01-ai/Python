# Sum of the digit 
numberData = input("Enter the number ")
num = 0
try:
    if not numberData.isdigit():
        raise ValueError("Please enter the number in the correct format.")
    for i in numberData:
        num = num + int(i)
    print("The sum of the digit is: ", num)
except ValueError as e:
    print(e)



    