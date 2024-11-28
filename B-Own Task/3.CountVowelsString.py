# Count Vowels in a String
import re 
stringData = input("Enter the string ")
CountNumber = len(re.findall(r'[aeiou|AEIOU]', stringData))
if CountNumber == 0:
    print("There is no vowels in the string")
else:
    print(f'Count vowels in string is: ', CountNumber)