listData = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

count = 0
i = 0
while 0 in listData:
    if listData[i] == 0:
        del listData[i]
        count += 1
        i = i - 1
    i += 1

for i in range(count):
    listData.append(0)

    
print(listData)
