print("==== #1 Update Values in Dictionaries ====")

print("A1:") #1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
print(f"Before change: {x}")

x[1][0] = 15
print(f"After change: {x}")


print("\nA2:") #2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(f"Before change: {students[0]}")

students[0]['last_name'] = "Bryant"
print(f"After change: {students[0]}")


print("\nA3:") #3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(f"Before change: {sports_directory['soccer']}")

sports_directory['soccer'][0] = "Andres"
print(f"After change: {sports_directory['soccer']}")


print("\nA4:") #4 Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
# print(z)        # [{'x': 10, 'y': 20}]
print(f"Before change: {z[0]}")     # {'x': 10, 'y': 20}

z[0]['y'] = 30
print(f"After change: {z[0]}")


print("\n==== #2 Iterate Through a List of Dictionaries ====")
print("\nA5:")
#5 Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary( incoming_list ):
    for i in range(0, len(incoming_list)):
        output = ""
        for key, val in incoming_list[i].items():
            output += f"{key} - {val},"
        print(output)

iterateDictionary(students)
"""Output:
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""


print("\n==== #3 Get Values From a List of Dictionaries ====")
print("\nA6:")
#todo 6 Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2( key_name, incoming_list ):
    for i in range(0, len(incoming_list)):
        for key, val in incoming_list[i].items():
            if key == key_name:
                print(f"{val}")
iterateDictionary2('last_name', students) 
"""Output
Michael
John
Mark
KB
"""


print("\n==== #4 Iterate Through a Dictionary with List Values ====")
print("\nA7:") #7
#3 Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info( incoming_dict ):
    for key, val in incoming_dict.items():
        print("\n---------------")
        print(f"{ len(val) } { key.upper() }")
        print("---------------")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)
"""Output:
---------------
7 LOCATIONS
---------------
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

---------------
8 INSTRUCTORS
---------------
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""