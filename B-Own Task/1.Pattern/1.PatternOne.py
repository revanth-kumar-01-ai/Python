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

def patternTwenty(n):
    for i in range(n):
        pass

# patternOne(5)
# patternTwo(5)
# patternThree(5)
# patternFour(5)
# patternFive(5)
# patternSix(5)
# patternSeven(5)
# patternEight(6)
# patternNine(5)
# patternTen(6)
# patternEleven(5)
# patternTwelve(9)
# patternThirteen(5)
# patternFourteen(29)
# patternFifteen(5)
# patternSixteen(5)
# patternSeventeen(5)
# patternEighteen(15)
patternTwenty(5)





