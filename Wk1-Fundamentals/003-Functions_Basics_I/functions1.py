#1
print("=== #1 Number of Food Groups ===")
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # output 5

#2
print("\n=== #2 Number of Military Branches ===")
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
print("NameError!") #! NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
print("\n=== #3 Number of Books on Hold ===")
def number_of_books_on_hold():
    return 5
    return 10 #! ignored, only one return statement can exist to exit function
print(number_of_books_on_hold()) # output: 5

#4
print("\n=== #4 Number of Fingers ===")
def number_of_fingers():
    return 5
    print(10) #! ignored, return statement exits the function before 10 can be printed
print(number_of_fingers()) # output: 5

#5
print("\n=== #5 Number of Great Lakes ===")
def number_of_great_lakes():
    print(5)
# output: 5
x = number_of_great_lakes()
print(x) # output: None

#6
print("\n=== #6 Add ===")
def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))
"""Output:
3
5
#! TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
"""

#7
print("\n=== #7 Concatenate ===")
def concatenate(b,c):
    return str(b) + str(c)
print(concatenate(2,5)) # output: 25

#8
print("\n=== #8 Number of Oceans or Fingers or Continents ===")
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) # executed
    if b < 10:
        return 5 # NOT executed
    else:
        return 10 # executed
    return 7 # invalid, only return statements in if statement can be executed
print(number_of_oceans_or_fingers_or_continents())
"""Output
100
10
"""

#9
print("\n=== #9 Number of Days in a Week Silicon or Triangle Sides ===")
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # output: 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # output: 14
print( number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3) ) # output: 21

#10
print("\n=== #10 Addition ===")
def addition(b,c):
    return b+c
    return 10 # ignored, bc only the first return statement is executed
print(addition(3,5)) # output: 8