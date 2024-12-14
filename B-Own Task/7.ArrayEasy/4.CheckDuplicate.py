listData = [1,1,2,2,2,3,3]

collect = []
count = 0
for i in listData:
    if i not in collect:
        collect.append(i)
    else:
        count = count + 1

for i in range(count):
    collect.append("_")

print(collect)
