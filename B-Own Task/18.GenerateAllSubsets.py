# Generate All Subsets of a String
string = "abc"
length = len(string) # 3

for i in range(length):

    for j in range(i, length):

        print(string[i:j+1])

