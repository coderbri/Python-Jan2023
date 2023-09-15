# Identigying Data Types in Python
# * 1) Variable Declaration - Primitive Data-Type
num1 = 42 # number
num2 = 2.3  # float
boolean = True # boolean
string = 'Hello World' # string

# * 2) Variable Declaration - Composite Data-Type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list - initializing
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary - initializing
fruit = ('blueberry', 'strawberry', 'banana') # tuple - initializing

# * print() = Log Statements to Terminal
print(type(fruit)) # accessing value in tuple # output: <class 'tuple'>
print(pizza_toppings[1]) # accessing value in list # output: Sausage
pizza_toppings.append('Mushrooms') # adding value to list
print(person['name']) # accessing value in the 'name' idx of dictionary
person['name'] = 'George' # reassigning value in dictionary idx of 'name'
person['eye_color'] = 'blue' # adding this idx:val to dictionary
print(fruit[2]) # accessing the 3rd idx of tuple

# * 3) Conditional Statements - If Statements
if num1 > 45: # if statement
    print("It's greater")
else: # else statement
    print("It's lower")

if len(string) < 5: # if statement
    print("It's a short word!")
elif len(string) > 15: # else if statement
    print("It's a long word!")
else: # else statement
    print("Just right!")

# * 4) Conditional Statements - For & While Loops
for x in range(5): # start for loop at 0, count to 4
    print(x) # output: 0,1,2,3,4

print('---')

for x in range(2,5): # start for loop at 2, count to 4
    print(x) # output: 2,3,4

print('---')

for x in range(2,10,3): # start for loop at 2, count to 10, count by 3s
    print(x)
x = 0 # variable declaration

print('---')

while(x < 5): # start while loop, and count loop until its been 5x
    print(x) # increment x by 1
    x += 1

print('---')

# * 4) Functions
pizza_toppings.pop() # delete last value of the list
pizza_toppings.pop(1) # delete value at idx of 1

print(person) # print dictionary to terminal
person.pop('eye_color') # delete key:val pair at this idx
print(person) # print UPDATED dictionary to terminal

for topping in pizza_toppings: # start for loop, initializing for each idx in the list
    if topping == 'Pepperoni': # if idx at this val is the same as "this" values...
        continue # ...then keep going through the list
    print('After 1st if statement') # once idx is not 'Pepperoni', go to next condition
    if topping == 'Olives': # if topping is 'Olives'...
        break # ...then stop and exit for loop

def print_hello_ten_times(): # declare function
    for num in range(10): # start for loop to count 10x
        print('Hello') # for each loop, log to console 'Hello'
print_hello_ten_times() # call the function

def print_hello_x_times(x): # declare function with parameter, x
    for num in range(x): # if parameter is x value...
        print('Hello') # ...then loop value x times
print_hello_x_times(4) # call the function

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # call function
print_hello_x_or_ten_times(4) # set argument, call the function


"""
Bonus section
"""

# print(num3) #! NameError: name <variable name> is not defined
# num3 = 72 #! NameError: name <variable name> is not defined
# fruit[0] = 'cranberry' #! TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #! IndexError: list index out of range
# print(pizza_toppings[7]) #! IndexError: list index out of range
#   print(boolean) #! IndentationError: unexpected indent
# fruit.append('raspberry') #! AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #! AttributeError: 'tuple' object has no attribute 'pop'


