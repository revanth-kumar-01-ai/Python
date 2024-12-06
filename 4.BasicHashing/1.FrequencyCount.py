listData = [10,5,10,15,10,5]
dist = {}
for i in listData:
    if i in dist:
        dist[i] += 1
    else:
        dist[i] = 1

for i in dist.keys():
    print(f"{i} {dist[i]}")

