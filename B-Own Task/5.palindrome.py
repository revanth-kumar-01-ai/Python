# Palindrome Checker 
stringData = input("Enter the string Data ")
if stringData == stringData[::-1]:
    print("Its palindrome")
else:
    print("Its not palindrome")