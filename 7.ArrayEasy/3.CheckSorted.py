listData = [3, 1, 4]

temp = ""
for i in range(len(listData)-1):
    if listData[i] < listData[i + 1]:
        temp = temp + "a"
    if listData[i] > listData[i + 1]:
        temp = temp + "d"
    
if "a" in temp and "d" in temp:
    print(False)
else:
    print(True)
