# Insertion Sort Algorithm
# The insertion sort always take the element and assign to the  correct order 
listData = [4, 3, 1, 0, 2, 5]
length = len(listData) - 1
j = 0
for i in range(0, length):
    j = i
    while (j > 0) and (listData[j - 1] > listData[j]):
        listData[j], listData[j - 1] = listData[j - 1], listData[j] 
        j -= 1

print(listData)