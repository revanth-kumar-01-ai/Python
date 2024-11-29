# Find the Missing Number in a Range
listData = [1, 2, 4, 5]

# Expected value 
expectedValue = listData[-1] * (listData[-1] + 1) / 2 
actualValue = sum(listData)
print(f'Missing value: {int(expectedValue - actualValue)}' ) 