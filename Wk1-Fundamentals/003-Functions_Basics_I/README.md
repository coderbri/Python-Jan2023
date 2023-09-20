# Function Basics I

Project **003-Function_Basics_I** contains a Python script with several functions, each with a description and, where applicable, explanations for errors if they exist. Let's go through each function:


## Function 1: Number of Food Groups
```python
def number_of_food_groups():
    return 5
```
- **Description:** This function `number_of_food_groups` returns the value `5`.
- **Output:** `5`


## Function 2: Number of Military Branches
```python
def number_of_military_branches():
    return 5
```
- **Description:** This function `number_of_military_branches` also returns the value `5`.
- **Note:** Line 11, (`print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())`), is commented out and will not be executed as that would raise a **`NameError`** due to the fact that the function `number_of_days_in_a_week_silicon_or_triangle_sides` is not defined.


## Function 3: Number of Books on Hold
```python
def number_of_books_on_hold():
    return 5
    return 10  # Ignored, only one return statement can exist to exit function
```
- **Description:** This function `number_of_books_on_hold` returns the value `5`. The second `return` statement is ignored, as only one `return` statement can be executed within a function.
- **Output:** `5`


## Function 4: Number of Fingers
```python
def number_of_fingers():
    return 5
    print(10)  # Ignored, return statement exits the function before 10 can be printed
```
- **Description:** This function `number_of_fingers` returns the value `5`. The `print(10)` statement is ignored because the `return` statement exits the function before it can be executed.
- **Output:** `5`


## Function 5: Number of Great Lakes
```python
def number_of_great_lakes():
    print(5)
```
- **Description:** This function `number_of_great_lakes` prints `5` but does not return a value.
- **Output:** `5`
- **Note:** When you call this function and assign its return value to `x`, `x` will have a value of `None`.


## Function 6: Add
```python
def add(b, c):
    print(b + c)
```
- **Description:** This function `add` prints the sum of `b` and `c` but does not return a value.
- **Note:** Line 40, (`print(add(1, 2) + add(2, 3))`), would raise a `TypeError` because you cannot add `NoneType` values together. This line is commented out and will not execute.


## Function 7: Concatenate
```python
def concatenate(b, c):
    return str(b) + str(c)
```
- **Description:** This function `concatenate` converts `b` and `c` to strings, concatenates them, and returns the result as a string.
- **Output:** `"25"`


## Function 8: Number of Oceans or Fingers or Continents
```python
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)  # Executed
    if b < 10:
        return 5  # Not executed
    else:
        return 10  # Executed
    return 7  # Invalid, only return statements in the if statement can be executed
```
- **Description:** This function `number_of_oceans_or_fingers_or_continents` sets `b` to `100`, prints it, and then has conditional `return` statements.
- **Output:** `100`
- **Note:** The last `return` statement (`return 7`) is invalid and will not be executed because the function has already returned a value.


## Function 9: Number of Days in a Week Silicon or Triangle Sides
```python
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3
```
- **Description:** This function `number_of_days_in_a_week_silicon_or_triangle_sides` compares `b` and `c` and returns `7` if `b` is less than `c`, and `14` otherwise.
- **Output Example:** 
   - `number_of_days_in_a_week_silicon_or_triangle_sides(2, 3)` returns `7`.
   - `number_of_days_in_a_week_silicon_or_triangle_sides(5, 3)` returns `14`.
   - `number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3)` returns `21`.


## Function 10: Addition
```python
def addition(b, c):
    return b + c
    return 10  # Ignored, only the first return statement is executed
```
- **Description:** This function `addition` returns the sum of `b` and `c`.
- **Output Example:** `addition(3, 5)` returns `8`.
- **Note:** The second `return` statement (`return 10`) is ignored, as only the first `return` statement is executed.

---

<p align="right">Completed: ２０２３年０９月２０日（水）</p>