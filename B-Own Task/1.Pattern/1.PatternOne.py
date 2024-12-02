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
    iterTwo = 1
    decreaseTwo = n * 2 - 1
    for i in range(1, n+1):

        for j in range(decreaseTwo, 0, -2):
            print(" ", end="")

        for j in range(1, iterTwo + 1):
            print("*", end="")

        iterTwo += 2
        decreaseTwo -= 2
        print()


def patternEight(n):
    iterTwo = 1
    decreaseTwo = n * 2 - 1
    for i in range(1, n+1):

        for j in range(1, iterTwo, 2):
            print(" ", end="")

        for j in range(1, decreaseTwo + 1):
            print("*", end="")

        iterTwo += 2
        decreaseTwo -= 2
        print()

# def patternNine(n):
#     F = True
#     i = 1
#     while F:
#         if n <= i:
#             return 0
#         print(i)
#         i += 1     


#1 2, 3, 4, 5 - 5 4 3 2 1

# patternOne(5)
# patternTwo(5)
# patternThree(5)
# patternFour(5)
# patternFive(5)
# patternSix(5)
# patternSeven(5)
# patternEight(5)
# patternNine(5 + 1)

