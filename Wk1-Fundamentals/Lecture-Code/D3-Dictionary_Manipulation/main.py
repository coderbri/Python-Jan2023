# REVIEW
def name_of_function(f_name, l_name):
    print(f'Hello, my name is {f_name} {l_name}!')
    # Hello, my name is Jane Doe!

name_of_function("Jane", l_name="Doe")

some_list = [1, 2, 3, 4, 5]
print(some_list) # [1, 2, 3, 4, 5]

some_list[2] = "bananas"
print(some_list) # [1, 2, 'bananas', 4, 5]

for i in range(0, len(some_list), 1):
    print(some_list[i])
# 1, 2, bananas, 4, 5

print("")
for item in some_list:
    print(item)
# 1, 2, bananas, 4, 5


#* ==== DICTIONARY MANIPULATION ====

janedoe_profile = {
    'f_name' : 'Jane',
    'l_name' : 'Doe',
    'age' : 27,
}

print(janedoe_profile) # {'f_name': 'Jane', 'l_name': 'Doe', 'age': 27, 'dob': 'March 18th'}
print(janedoe_profile['f_name']) # Jane

janedoe_profile['f_name'] = "Janice"
print(janedoe_profile['f_name']) # Janice

janedoe_profile['dob'] = 'March 18th' # adding key:value to dictionary
print(janedoe_profile) # {'f_name': 'Janice', 'l_name': 'Doe', 'age': 27, 'dob': 'March 18th'}


# * Two ways to added a nonexistent entry:
jsmith_profile = {
    'f_name' : 'John',
    'l_name' : 'Smith',
    'age' : 34,
}

print("")
# ? "if-else" Statement:
if 'dob' in jsmith_profile:
    print(jsmith_profile['dob'])
else:
    jsmith_profile['dob'] = "May 20th"
    print(f"Entry added: {jsmith_profile['dob']}\n {jsmith_profile}")

ivyjune_profile = {
    'f_name' : 'Ivy',
    'l_name' : 'June',
    'age' : 19,
}

print("")
# ? "if not" Statement:
if not 'dob' in ivyjune_profile:
    ivyjune_profile['dob'] = "May 20th"
    print(f"Entry added: {ivyjune_profile['dob']}\n {ivyjune_profile}")

print("")

for key in ivyjune_profile:
    if ivyjune_profile[key] == "Ivy":
        print(f"This value is stored in this key: {key}")


print("")

my_characters = [ # ? a list of dictionaries:
    {
        'name' : 'Keqing',
        'vision' : 'Electro',
        'weapon' : 'Sword',
        'date_of_birth' : 'November 20th',
        'constellation' : 2
    },
    {
        'name' : 'Tartaglia',
        'vision' : 'Hydro',
        'weapon' : 'Bow',
        'date_of_birth' : 'July 20th',
        'constellation' : 0
    },
    {
        'name' : 'Xiao',
        'vision' : 'Anemo',
        'weapon' : 'Polearm',
        'date_of_birth' : 'April 17th',
        'constellation' : 0
    },
    {
        'name' : 'Shikanoin Heizou',
        'vision' : 'Anemo',
        'weapon' : 'Catalyst',
        'date_of_birth' : 'July 24th',
        'constellation' : 6
    },
    {
        'name' : 'Kaedehara Kazuha',
        'vision' : 'Anemo',
        'weapon' : 'Sword',
        'date_of_birth' : 'October 29th',
        'constellation' : 1
    }
]

print("------\n==== Accessing Dictionaries in a List ====")
print(my_characters[2]) # ? Prints whole dictionary
print(my_characters[2]['name']) # ? Prints value at key

print("------\n")
# ? Print the name of each character (per line)
for one_chara in my_characters:
    print(one_chara['name'])

print("------\n")
# ? Print key:value pair for only one character, per line.
for key, value in my_characters[1].items():
    print(key, value)

print("------\n") # Same as above. but more organized.
# ? Print each character's key:value pair as a string per line, with a space between different character stats.
for one_chara in my_characters:
    output = ''
    for key, value in one_chara.items():
        output += f"{key} : {value}\n"
    print(output)

