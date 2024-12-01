# Sub array with 0 sum

listData = [-2, -1, 1]

listDataOne = []
sum1 = 0
res = False
for i in range(len(listData)):
    sum1 += listData[i]
    if sum1 in listDataOne:
        res = True
        break
    else:
        listDataOne.append(sum1)

print(res)