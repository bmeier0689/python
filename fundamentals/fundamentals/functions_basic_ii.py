# #1
def countdown(num):
    newList = []
    for i in range(num,-1,-1):
        newList.append(i)
    return newList

print(countdown(5))

# #2
def printAndReturn(list):
    print(list[0])
    return list[1]

print(printAndReturn([1,2]))

# #3
def firstPlusLength(list):
    sum = list[0] + len(list)
    return sum

print(firstPlusLength([1,2,3,4,5]))

# #4
def greaterThanSecond(list):
    if len(list) < 2:
        return False
    newList = []
    greaterThanTwo = 0
    for i in list:
        if i > list[1]:
            newList.append(i)
            greaterThanTwo += 1
    print(greaterThanTwo)
    return newList

print(greaterThanSecond([5,2,3,2,1,4]))
print(greaterThanSecond([3]))

# #5
def lengthAndValue(size,value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList

print(lengthAndValue(4,7))
print(lengthAndValue(6,2))