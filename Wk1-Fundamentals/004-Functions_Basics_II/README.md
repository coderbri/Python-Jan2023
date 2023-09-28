# Function Basics II

Certainly! Here's a GitHub README explaining what each function does based on the provided code with your changes:

## Function 1: Countdown

```python
def countdown(input_num):
    countdown_list = []
    for i in range(input_num, -1, -1):
        countdown_list.append(i)
    return countdown_list
```
- **Description:** This function, `countdown`, takes an integer `input_num` as input and generates a list that counts down from `input_num` to `0`. The list starts with `input_num` as the first element and ends with `0` as the last element.
    - **Example:** `countdown(5)` would return `[5, 4, 3, 2, 1, 0]`, counting down from 5 to 0.


## Function 2: Print and Return

```python
def print_and_return(numbers):
    if len(numbers) == 2:
        print(numbers[0])
        return numbers[1]
    else:
        raise ValueError("Input list must contain exactly two numbers.")
```
- **Description:** This function, `print_and_return`, takes a list `numbers` as input. It prints the first value in the list and returns the second value.
    - **Example:** `print_and_return([1, 2])` would print `1` and return `2`. If the input list contains more or fewer than two numbers, it raises a `ValueError`.


## Function 3: First Plus Length

```python
def first_plus_length(numbers_list):
    if len(numbers_list) > 0:
        return numbers_list[0] + len(numbers_list)
    else:
        raise ValueError("Numbers list must not be empty.")
```
- **Description:** This function, `first_plus_length`, takes a list `numbers_list` as input. It calculates and returns the sum of the first value in the list plus the length of the list.
    - **Example:** `first_plus_length([1, 2, 3, 4, 5])` would return `6` (1 + 5). If the input list is empty, it raises a `ValueError`.


## Function 4: Values Greater than Second

```python
def values_greater_than_second(input_list):
    if len(input_list) < 2:
        return False
    output = []
    for i in range(0, len(input_list)):
        if input_list[i] > input_list[1]:
            output.append(input_list[i])
    print(len(output))
    return output
```
- **Description:** This function, `values_greater_than_second`, takes a list `input_list` as input. It generates a new list containing only values greater than the second value in the input list. It also prints how many values meet this condition. If the input list has less than 2 elements, it returns `False`.
    - **Example 1:** `values_greater_than_second([1, 2, 3, 4, 5, 6])` would print `4` (4 values greater than `2`) and return `[3, 4, 5, 6]`.
    - **Example 2:** `values_greater_than_second([])` would return `False` since the input list is empty.


## Function 5: This Length, That Value

```python
def this_length_that_value(size, value):
    returned_list = []
    for i in range(0, size):
        returned_list.append(value)
    return returned_list
```
- **Description:** This function, `this_length_that_value`, takes two integers as input: `size` and `value`. It generates and returns a list of length `size`, where all values in the list are equal to `value`.
    - **Example 1:** `this_length_that_value(4, 7)` would return `[7, 7, 7, 7]`, a list of length 4 with all values as `7`.
    - **Example 2:** `this_length_that_value(6, 2)` would return `[2, 2, 2, 2, 2, 2]`, a list of length 6 with all values as `2`.

---
<p align="right">Completed: ２０２３年０９月２１日（木）</p>