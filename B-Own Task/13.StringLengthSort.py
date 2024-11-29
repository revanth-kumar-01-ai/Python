#  Sort a List of Strings by Length
listData = ["apple", "bat", "cat", "elephant"]

# find the max length
max_length = max(len(s) for s in listData)

# create bucket(list) for each possible length
buckets = [[] for _ in range(max_length + 1)] # output -> [[], [], [], [], [], [], [], [], []]

# Distribute the data corresponding buckets
for iter in listData:
    buckets[len(iter)].append(iter) # [[], [], [], ['bat', 'cat'], [], ['apple'], [], [], ['elephant']]

# Combine the buckets using the extend method 
sortedString = []
for bucket in buckets:
    sortedString.extend(bucket)

print(sortedString)
# ['bat', 'cat', 'apple', 'elephant']


# short method

# strings = ["apple", "bat", "carrot", "dog"]
# sorted_strings = sorted(strings, key=len)
# print(sorted_strings)