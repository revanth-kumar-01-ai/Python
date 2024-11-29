#  Find Second Largest Number
listData = [10, 20, 4, 45, 99]
largeNumber = 0
pervious = 0
for iter in listData:
    pervious = largeNumber
    if iter > largeNumber:
        largeNumber = iter

print(pervious)
