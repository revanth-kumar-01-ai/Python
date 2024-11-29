# Sort a List of Dictionaries by a Key
dict = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 22}]
dict.sort(key= lambda x:x['age'])
print(dict)