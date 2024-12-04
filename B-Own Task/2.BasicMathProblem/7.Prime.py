N = 60

if N in [1, 2]:
    print("prime")
else:
    flag = False
    for i in range(2, (N // 2)):
        if N % i == 0:
            flag = True
            break
        
    if not flag:
        print("Prime")
    else:
        print("Not Prime")