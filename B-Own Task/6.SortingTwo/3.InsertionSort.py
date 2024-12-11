# 3.InsertionSort.py
def insertSort(arr, n):
    if n <= -1:
        return 0
    insertSort(arr, n - 1)
    j = n
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
    return arr
    
    

listData = [4,3,1,0,2,5]
arr = insertSort(listData, len(listData) - 1)
print(arr)