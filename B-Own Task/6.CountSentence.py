# Count Words in a Sentence 
stringData = "This is a test"
splitWords = stringData.split(" ")
if len(splitWords) == 0:
    print("Empty")
else:
    print("Total number of sentence is: ", len(splitWords))