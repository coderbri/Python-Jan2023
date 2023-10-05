my_list = [1, 2, 3, 4]
for i in range( 0, len(my_list) ):
    print(f"Index: {i} = [{my_list[i]}].")
"""Output:
print(i, my_list[i]) # ? prints index, value at index
Index: 0 = [1].
Index: 1 = [2].
Index: 2 = [3].
Index: 3 = [4].
"""

my_new_list = [1, 2, 3, 4] # ? for val in list, print the val at each loop
for i in my_new_list:
    print(i)
# Output: 1, 2, 3, 4

my_str = 'hello'
for char in my_str:
    print(char)
# Output: h, e, l, l, o

hero = { 'first_name': 'Buzz', 'last_name': 'Lightyear' }
for key in hero:
    print(key)
# Output: first_name, last_name

for key in hero:
    print(hero[key])
# Output: Buzz Lightyear #? prints whatever is at that key

this_list = [1, 2, 3, 4]
print(this_list[len(this_list) - 1])
# Output: 4

# ! print(this_list[len(this_list)])
# ? list index out of range

person = { 'first_name': 'Jessie', 'lottery_nums': [2, 14, 50, 55] }
print(person['lottery_nums'])
# Output: [2, 14, 50, 55]