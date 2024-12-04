strData = "-121"

i = 0
j = len(strData) - 1
res = True

while res:
    if strData[i] != strData[j]:
        res = False
    if (i+1) == j or i == j:
        break
    i += 1
    j -= 1

if res:
    print("Palindrome")
else:
    print("Not Palindrome")