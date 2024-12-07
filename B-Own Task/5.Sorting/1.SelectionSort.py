# Selection Sort Algorithm

listData = [13,46,24,13,8,52,20,9]

for i in range(0, len(listData)):
    for j in range(0, len(listData)):
        if listData[i] < listData[j]:
            listData[i], listData[j] = listData[j], listData[i]


print(listData)   

