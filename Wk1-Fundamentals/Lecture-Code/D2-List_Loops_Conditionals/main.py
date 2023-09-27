nums = [1, 2, 3, 4, 5]
print(nums) # [1, 2, 3, 4, 5]

nums.reverse()
print(nums) # [5, 4, 3, 2, 1]

f_name = "jane"
l_name = "doe"

my_name = "hello, my name is abcdef"
print(f"hello my name is {f_name} {l_name}.".title()) # Hello My Name Is Jane Doe.
#? capitalizes each word in the string.

#* LIST MANIPULATION

print(len(my_name)) # 24 #? prints string length

some_list = [1, 2, 3, 4, 5]
print(some_list) # [1, 2, 3, 4, 5]
some_list[2] = 8
print(some_list) # [1, 2, 8, 4, 5]

print(some_list[2]) # 8 #? accesses idx of list

some_list.append(6) #? adds another element to list
print(some_list)  # [1, 2, 8, 4, 5, 6]

some_list.pop() #? deletes LAST element of list
print(some_list)  # [1, 2, 8, 4, 5]

some_list.remove(some_list[2]) #? removes value at this idx
print(some_list)  # [1, 2, 4, 5]


#* FUNCTIONS
'''
Functions consists of the following:
1. Declaration and initializing loop control variable
2. Checking condition.
3. Incrementing loop control value.
'''
for index in range(0, 5, 1):
    print(index)
# (per line) 0, 1, 2, 3, 4
print("")

for num in range(0, len(some_list), 1):
    print(num)
"""
#? prints however many indexes
output:     0  1  2  3
some_list= [1, 2, 4, 5]
"""

#* CONDITIONALS
is_student = 1 # this is the same as `= True`
if is_student:
    print("화이팅")

print("")
def fizz_buzz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
fizz_buzz()
"""Output
Fizz Buzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
"""

