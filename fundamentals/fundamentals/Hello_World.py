# 1. TASK: print "Hello World"
from ast import Num


print("Hello World!")
# 2. print "Hello Noelle!" with the name in a variable
name = "Brad"
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 7
print("Hello", number)	# with a comma
print("Hello " + str(number))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

fave_food1 = "sushi"
fave_food2 = "PIZZA"
print(fave_food1.upper())
print(fave_food2.lower())
print(fave_food2.isupper())
print(fave_food2.islower())
print(fave_food1.islower())
print(fave_food1.isupper())

fave_food1 = "sushi"

fave_food2 = "PIZZA"

statement = "pizza is the best food"
print(statement.split())

