def merge(arr, low, mid, high):
    # Create temporary arrays for left and right subarrays
    left_part = arr[low:mid + 1]
    right_part = arr[mid + 1:high + 1]
    
    i, j, k = 0, 0, low  # Pointers for left, right, and merged arrays
    
    # Merge the two subarrays into the main array
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)


arr = [3, 4, 2, 5, 1]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:",arr)