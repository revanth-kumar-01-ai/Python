listData = [4,1,2,1,2]

# dict = {}
# for i in listData:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# for i in dict.keys():
#     if dict[i] == 1:
#         print(i)

xorr = 0
for num in listData:
    xorr ^= num

print(xorr)

