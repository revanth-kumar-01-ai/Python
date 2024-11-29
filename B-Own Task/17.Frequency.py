# Count Frequency of Each Element in a List
listData =  [1, 2, 2, 3, 3, 3, 4] 
freq = {}
for iter in listData:
    if iter in freq:
       freq[iter] = freq[iter] + 1
    else:
        freq[iter] = 1
print(freq)
    