num1 = 42 # variable declaration, numbers
num2 = 2.3 # variable declaration, numbers
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declataion, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declatation, initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # log statement, dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # log statement, access value

if num1 > 45: # conditional if
    print("It's greater") # log statement
else: # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if
    print("It's a long word!") # log statement
else: # conditional else
    print("Just right!") # log statement

for x in range(5): # for loop sequence
    print(x) # log statement
for x in range(2,5): # for loop sequence
    print(x) # log statement
for x in range(2,10,3): # for loop sequence
    print(x) # log statement
x = 0 # variable declaration, numbers
while(x < 5): # while loop increment
    print(x) # log statement
    x += 1 # variable declaration, numbers

pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list delete value

print(person) # log statement
person.pop('eye_color') # dictionary delete value
print(person) # log statement

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # for loop break

def print_hello_ten_times(): # function
    for num in range(10): # for loop sequence
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x): # function parameter
    for num in range(x): # for loop sequence
        print('Hello') # log statement

print_hello_x_times(4) # log statement, function argument

def print_hello_x_or_ten_times(x = 10): # function parameter
    for num in range(x): # for loop sequence
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4)# log statement


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'