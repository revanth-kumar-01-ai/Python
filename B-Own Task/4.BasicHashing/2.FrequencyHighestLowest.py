listData = [2,2,3,4,4,2]
dist = {}
for i in listData:
    if i in dist:
        dist[i] += 1
    else:
        dist[i] = 1

highest = 0
low = dist[listData[0]]
maxKey = 0 
lowKey = 0
for i in dist:
    if dist[i] > highest:
        highest = dist[i]
        maxKey = i
    if low > dist[i]:
        low = dist[i]
        lowKey = i


print(f'{maxKey} {lowKey}')
