listData = [4, 5, 6, 7, 0, 1, 2]
length = len(listData) - 1
for i in range(0, length):
    for j in range(0, length):
        if listData[j] > listData[j + 1]:
            listData[j], listData[j + 1] = listData[j + 1], listData[j]
    length -= 1

print(listData)