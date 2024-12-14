listData = [1, 2, 3, 4, 5]

target = 4
flag = False
for i in range(len(listData)):
    if listData[i] == target:
        flag = True
        break
    
if flag:
    print("having")
else:
    print("not having")