listData = [8,10,5,7,9]


i = 0
j = len(listData) - 1

temp = 0
while i <= j:
    
    if listData[i] > temp:
        temp = listData[i]

    if listData[j] > temp:
        temp = listData[j]

    i += 1
    j -= 1

print(temp)