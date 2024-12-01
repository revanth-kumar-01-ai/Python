listData = [2, 4, 3, 3, 1, 2,]

L = 0
R = 0
X = 0
target = 7
res = []
minimum = float('inf')
for i in range(len(listData)):
    X = X + listData[R]
    while X > target:
        X = X - listData[L]
        if X == target and (R-L) < minimum:
            minimum = R - L
            res = listData[L+1:R+1]
        L = L + 1
       
    R = R + 1
print(f'minimum length = {minimum} {res}')