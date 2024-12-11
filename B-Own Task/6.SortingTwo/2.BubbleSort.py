def bubbleSort(arr, n):
    j = 1
    for i in range(n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    if n <= 1:
        return arr
    return bubbleSort(arr, n - 1)

arr = bubbleSort([3,4,2,5,1], 5-1)
print(arr)

