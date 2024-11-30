import sys
# 1. Find the Maximum Sub array Sum

# [1, 2, 3]
# 1, 2, 3, (1, 2), (2, 3), (1, 2, 3)

# listData = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# resultData = []
# for i in range(len(listData)):
#     for j in range(i, len(listData)):
#         resultData.append(sum(listData[i:j+1]))

# print(max(resultData))


listData = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = 0
maxValue = -(sys.maxsize)
for i in range(len(listData)):
    temp = current + listData[i]
    if current < listData[i]:
        current = listData[i]
    else:
        current = temp
    
    if maxValue < current:
        maxValue = current

print(maxValue)
