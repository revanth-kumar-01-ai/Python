a = [2, 3, 5]

pre_sum_map = {}

total = 0
maxLen = 0
k = 5

for i in range(len(a)):  # Iterate over the full array
    total += a[i]

    # Check if the total equals k
    if total == k:
        maxLen = max(maxLen, i + 1)

    # Calculate the remaining sum (rem = total - k)
    rem = total - k

    # Check if the remaining sum exists in the prefix sum map
    if rem in pre_sum_map:
        length = i - pre_sum_map[rem]
        maxLen = max(maxLen, length)

    # Add the total to the prefix sum map if not already present
    if total not in pre_sum_map:
        pre_sum_map[total] = i

print(pre_sum_map)  # Output the prefix sum map
print(maxLen)       # Output the maximum length of the subarray


