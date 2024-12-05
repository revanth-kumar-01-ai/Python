def ReverseArray(array, start, end):
    if start < end:
        array[start], array[end] = array[end], array[start]
        ReverseArray(array, start + 1, end - 1)
     

array = [5,4,3,2,1]
n = len(array)
res = ReverseArray(array, 0, n - 1)

print(res)


# 0 < 4 [1, 4, 3, 2, 5]

# 1 < 3 [1, 2, 3, 4, 5]

# 2 < 2 False


