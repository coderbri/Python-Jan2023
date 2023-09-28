# Nested Dictionaries & Lists

This repository contains Python code to solve various algorithms. Below are explanations and solutions for each algorithm.

## Part I: Update Values in Dictionaries

### A1: Change the value 10 in x to 15.

1. Start with the initial list `x = [ [5,2,3], [10,8,9] ]`.
2. Access the element at index `[1][0]` in `x` and set it to 15.
3. The updated `x` is now `[ [5,2,3], [15,8,9] ]`.

### A2: Change the last_name of the first student from 'Jordan' to 'Bryant'

1. Start with the initial list of dictionaries `students`.
2. Access the first dictionary using `students[0]`.
3. Change the value associated with the key `'last_name'` to 'Bryant'.
4. The updated first dictionary is now `{'first_name': 'Michael', 'last_name': 'Bryant'}`.

### A3: In the sports_directory, change 'Messi' to 'Andres'

1. Start with the initial dictionary `sports_directory`.
2. Access the list associated with the key `'soccer'`.
3. Access the first element of the list and set it to 'Andres'.
4. The updated list for 'soccer' is now `['Andres', 'Ronaldo', 'Rooney']`.

### A4: Change the value 20 in z to 30

1. Start with the initial list of dictionaries `z`.
2. Access the first dictionary using `z[0]`.
3. Access the value associated with the key `'y'` and set it to 30.
4. The updated dictionary is now `{'x': 10, 'y': 30}`.


## Part II: Iterate Through a List of Dictionaries

### A5: Create a function `iterateDictionary(some_list)`

1. Define a function `iterateDictionary` that takes a list of dictionaries as input.
2. Loop through each dictionary in the list.
3. For each dictionary, loop through its keys and values, printing them in the format `key - value`.

Example Output:
```
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
```

## Part III: Get Values From a List of Dictionaries

### A6: Create a function `iterateDictionary2(key_name, some_list)`

1. Define a function `iterateDictionary2` that takes a key name and a list of dictionaries as input.
2. Loop through each dictionary in the list.
3. For each dictionary, check if the key exists and print its corresponding value.

Example Output (with `key_name` set to `'last_name'`):
```
Jordan
Rosales
Guillen
Tonel
```

## Part IV: Iterate Through a Dictionary with List Values

### A7: Create a function `printInfo(some_dict)`

1. Define a function `print_info` that takes a dictionary as input.
2. Loop through each key-value pair in the dictionary.
3. Print the name of the key in uppercase and the size of its associated list.
4. Print the elements within the list.

Example Output:
```
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
```

---
<p align="right">Completed: ２０２３年０９月２７日（水）</p>