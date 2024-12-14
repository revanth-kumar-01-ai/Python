# Left rotate
listData = [3,7,8,9,10,11]

k = 3
for i in range(k):
    temp = listData[0]
    del listData[0]
    listData.append(temp)

print("left rotate ",listData)

# Right rotate 

listData = [1,2,3,4,5,6,7]

k = 2
for i in range(k):
    temp = listData[len(listData) - 1]
    listData.pop()
    listData.insert(0, temp)

print("right rotate:", listData)