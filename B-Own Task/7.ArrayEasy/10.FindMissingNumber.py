# 10.FindMissingNumber.py

listData = [1,2,4,5]
total = sum(listData) 
n = listData[len(listData) - 1] * (listData[len(listData) - 1] + 1) // 2

missingNumber = n - total
print(missingNumber)