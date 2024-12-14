# Maximum One 
listData = [1, 0, 1, 1, 0, 1]

count = 0
pervious = 0
for i in listData:
    if i != 0:
        count += 1
    else:
        pervious = count
        count = 0

store = count if count > pervious else pervious
print(store)