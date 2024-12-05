def Palindrome(data, start, end):
    if start < end:
        if (data[start] == data[end]):
            return Palindrome(data, start + 1, end - 1)
        else:
            return False
    else:
        return True

data = "ABC"
res = Palindrome(data, 0, len(data) - 1)
print(res)
