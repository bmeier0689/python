# Number 1
for i in range(151):
    print(i)

# Number 2
for i in range(5,1005,5):
    print(i)

# Number 3
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Number 4
sum = 0
for i in range(0,500000):
    if i % 3 == 0:
        sum += i

print(sum)

# Number 5
for i in range(2018,0,-4):
    print(i)

# Number 6
lowNum = 4
highNum = 200
mult = 5

for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)