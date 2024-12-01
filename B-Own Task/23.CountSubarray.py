#  Count Sub arrays with a Given Sum 
listData = [1, 2, 3]

sumOne = 0
listDataTwo = []
k = 3
count = 0
y = 0
for i in range(len(listData)):
    sumOne = sumOne + listData[i]
    listDataTwo.append(sumOne)
    y = sumOne - k
    if sumOne == k:
        count += 1
    elif y in listData:
        count += 1

print(count)
    