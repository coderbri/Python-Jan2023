#* Python Syntax
# Variables & Data Types
name = "Bri"
my_age = 22.9
is_student = True
hobbies = []

# janesBio = {
#     'first_name': 'Jane',
#     'last_name': 'Doe'
# }

'''
if (condition) {
    ...then code here...
}
'''
if my_age == 22:
    print("You're old!")


#* Strings
f_name = "John"
l_name = "Smith"
print(f"Hello, my name is {f_name} {l_name}!") #? f string
print(f_name, l_name)
print(f_name + " " + l_name)
#                                   MUST BE IN ORDER!
print( "Hello, my name is {} {}!".format(f_name, l_name) )