def patternOne(n):
    for i in range(n):
        print(n * "*")


def patternTwo(n):
    for i in range(n + 1):
        print(i * "*")

def patternThree(n):
    x = " "
    for i in range(1, n+1):
        x = x + str(i)
        print(x)

def patternFour(n):
    for i in range(1, n+1):
        print(i * (str(i)))

def patternFive(n):
    for i in range(n, 0, -1):
        print(i * "*")


def patternSix(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()

def patternSeven(n):
    for i in range(1, n+1):
        print(((n - i) * " "), ((2 * i - 1)  * "*"))


def patternEight(n):
    for i in range(n-1, 0, -1):
        print(" " * (n - i - 1), ((2 * i - 1) * "*"))


def patternNine(n):
    for i in range(1, n+1):
        print(((n - i) * " "), ((2 * i - 1)  * "*"))
    n = n + 1
    for i in range(n-1, 0, -1):
        print(" " * (n - i - 1), ((2 * i - 1) * "*"))

def patternTen(n):
    i = 1
    direction = 1
    while i >= 1:
        print(i * "*")
        if i == n:
            direction = -1
        i += direction

def patternEleven(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j%2, end= " ")
        print()

def patternTwelve(n):
    gap = ((n - 1) * 2) - 2
    for i in range(1, n):
        for i in range(1, i+1):
            print(i, end ="")
        
        print(" " * gap, end="")

        for i in range(i, 0, -1):
            print(i, end ="")
        
        gap -= 2

        print()

def patternThirteen(n):
    iterNum = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(iterNum, end=" ")
            iterNum += 1
        print()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def patternFourteen(n):
    if n <= len(alphabet):
        for i in range(n):
            print(alphabet[0:i+1])
    else:
        print("Invalid")

def patternFifteen(n):
    if n <= len(alphabet):
        for i in range(n-1, -1, -1):
            print(alphabet[0:i+1])
    else:
        print("Invalid")
        
def patternSixteen(n):
    if n <= len(alphabet):
        for i in range(n):
            print(" " + alphabet[i] * (i+1))
    else:
        print("Invalid")

def patternSeventeen(n):
    if n <= len(alphabet):
        for i in range(n):
            print(((n - i) * " "), alphabet[0:i+1]+alphabet[0:i][::-1])
    else:
        print("Invalid")   

def patternEighteen(n):
    for i in range(n-1, -1, -1):
        print(alphabet[i:n])

def patternNineteen(n):
    gap = 0
    for i in range(n, 0, -1):
        print(("*" * i) + (" " * gap) + ("*" * i))
        gap += 2

    for i in range(1, n+1):
        gap -= 2
        print(("*" * i) + (" " * gap) + ("*" * i))
        

def patternTwenty(n):
    i = 1
    direction = 1
    gap = (n * 2) - 2
    gapIter = -2
    while i >= 1:
        print(("*" * i) + (" " * gap) + ("*" * i))
        if i == n:
            direction = -1
            gapIter = 2
        i += direction
        gap += gapIter


def patternTwentyOne(n):
    for i in range(n):
        if i == 0 or i == (n - 1):
            print("*" * n)
        else:
            print("*" + (" " * (n - 2)) + "*")


def patternTwentyTwo(n):
    size = (n - 1) + n
    for i in range(size):
        for j in range(size):
            distance = min(i, j, size - 1 - i, size - 1 - j)
            value = n - distance
            print(value, end="")
        print()


# patternOne(5)
# patternTwo(5)
# patternThree(5)
# patternFour(5)
# patternFive(5)
# patternSix(5)
# patternSeven(5)
# patternEight(5)
# patternNine(5)
# patternTen(5)
# patternEleven(5)
# patternTwelve(5)
# patternThirteen(5)
# patternFourteen(5)
# patternFifteen(5)
# patternSixteen(5)
# patternSeventeen(5)
# patternEighteen(5)
# patternNineteen(5)
# patternTwenty(5)
# patternTwentyOne(5)
# patternTwentyTwo(5)


#  patternOne 



# *****
# *****
# *****
# *****
# *****


#  patternTwo 

# *
# **
# ***
# ****
# *****


#  patternThree 


#  1
#  12
#  123
#  1234
#  12345


#  patternFour 


# 1
# 22
# 333
# 4444
# 55555


#  patternFive


# *****
# ****
# ***
# **
# *


#  patternSix


# 12345
# 1234
# 123
# 12
# 1


#  patternSeven


#      *
#     ***
#    *****
#   *******
#  *********


#  patternEight


#  *******
#   *****
#    ***
#     *


#  patternNine


#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *


#  patternTen


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


#  patternEleven


# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


#  patternTwelve


# 1      1
# 12    21
# 123  321
# 12344321


#  patternThirteen


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

#  patternFourteen


# A
# AB
# ABC
# ABCD
# ABCDE


#  patternFifteen


# ABCDE
# ABCD
# ABC
# AB
# A


#  patternSixteen


#  A
#  BB
#  CCC
#  DDDD
#  EEEEE


#  patternSeventeen


#       A
#      ABA
#     ABCBA
#    ABCDCBA
#   ABCDEDCBA


#  patternEighteen


# E
# DE
# CDE
# BCDE
# ABCDE


#  patternNineteen


# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


#  patternTwenty


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


#  patternTwentyOne


# *****
# *   *
# *   *
# *   *
# *****


#  patternTwentyTwo


# 555555555
# 544444445
# 543333345
# 543222345
# 543212345
# 543222345
# 543333345
# 544444445
# 555555555








