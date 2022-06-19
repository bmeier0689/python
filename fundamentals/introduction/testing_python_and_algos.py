from datetime import date
import random
import re

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')


print(type(24))
print(type(3.9))
print(type(3j))

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))


import random
print(random.randint(2,5)) # provides a random number between 2 and 5

name = "Zen"
print("My name is", 8)


name = "Zen"
print("My name is " + 8)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

list = [3,6,9,10]
int = 3

def divisible(listInput, intInput):
    count = 0
    for item in listInput:
        if item % intInput == 0:
            count += 1
    return count

print(divisible([3,6,9,10], 3))

def birthdayChecker(dateInput):
    today = "06/13/2022"
    birthday = ''
    if int(today[0:2]) > int(dateInput[0:2]):
        birthday = True
    elif int(today[0:2]) < int(dateInput[0:2]):
        birthday = False
    elif int(today[3:5]) >= int(dateInput[3:5]):
        birthday = True
    else:
        birthday = False
    if birthday == True:
        age = int(today[6:]) - int(dateInput[6:])
        bdaystring = "has"
    else:
        age = int(today[6:]) - int(dateInput[6:]) - 1
        bdaystring = "has not"
    return "User is currently " + str(age) + " years old and " + bdaystring + " had their birthday this year"

print(birthdayChecker("05/30/1995"))
print(birthdayChecker("11/05/1959"))

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)

print(person["first"])
full_name = person["first"] + " " + person["last"]
print(full_name)

value_removed = person.pop("age")
print(value_removed)
del person["is_organ_donor"]
print(person)

person.clear()
print(person)

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

for each_key in my_dict:
    print(my_dict[each_key])

    # List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(resume_data["skills"][1])
print(users[2]["first"])


def minimumValue(listInput):
    minValue = listInput[0]
    for value in listInput:
        if value < minValue:
            minValue = value
    return minValue

def maximumValue(listInput):
    maxValue = listInput[0]
    for value in listInput:
        if value > maxValue:
            maxValue = value
    return maxValue

def averageValue(listInput):
    sumValues = listInput[0]
    for i in range(1,len(listInput),1):
        sumValues += listInput[i]
    return sumValues/len(listInput)

def minMaxAverage(listInput):
    minValue = minimumValue(listInput)
    maxValue = maximumValue(listInput)
    avgValue = averageValue(listInput)
    return [minValue, maxValue, avgValue]

print(minMaxAverage([4,7,0,2,18]))
print(minimumValue([-3,5,6,9,12]))
print(maximumValue([4,7,2,18,0]))