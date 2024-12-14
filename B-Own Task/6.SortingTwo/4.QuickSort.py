def quick_sort(arr):
    if len(arr) <= 1:  
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
sorted_data = quick_sort(data)
print("Sorted Array:", sorted_data)