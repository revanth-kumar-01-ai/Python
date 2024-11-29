#  Remove Duplicates from a List
listData = [1, 2, 2, 3, 4, 4, 5]
dist = {}
for iter in listData:
    if iter in dist.keys():
        dist[iter] = dist[iter] + 1
    else:
        dist[iter] = 0

for iter in dist.keys():
    print(iter, end=" ")