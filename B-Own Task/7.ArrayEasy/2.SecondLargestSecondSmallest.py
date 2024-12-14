import sys
listData = [1, 2, 7, 7, 5]

small = min(listData)
large = max(listData)

secondSmall =float("inf")
secondLargest = float("-inf")

if len(listData) == 1 or 0:
    print(-1)
else:
    for i in listData:

        if i < secondSmall and i != small:
            secondSmall = i 

        if i > secondLargest and i != large:
            secondLargest = i 
    
    print("Second largest number:",secondLargest)
    print("Second smallest number:",secondSmall)
