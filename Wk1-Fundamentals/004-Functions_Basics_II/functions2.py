print("\n==== #1 Countdown ====")
def countdown( input_num ):
    countdown_list = []
    for i in range(input_num, -1, -1):
        countdown_list.append(i)
    return countdown_list
print(countdown(5))
# The for loop iterates from n down to 0 with a step of -1 (i.e., counting down).
# In each iteration, the current number i is appended to the countdown_list.

print("\n==== #2 Print and Return ====")
def print_and_return(numbers):
    if len(numbers) == 2:
        print(numbers[0])
        return numbers[1]
    else:
        raise ValueError("Input list must contain exactly two numbers.")
print(print_and_return([1,2]))
# print(print_and_return([1,2,3])) #! ValueError: Input list must contain exactly two numbers.

print("\n==== #3 First Plus Length ====")
def first_plus_length(numbers_list):
    if len(numbers_list) > 0:
        return numbers_list[0] + len(numbers_list)
    else:
        raise ValueError("Numbers list must not be empty.")
print(first_plus_length([1,2,3,4,5]))
# print(first_plus_length([])) #! ValueError: Numbers list must not be empty.

print("\n==== #4 Values Greater than Second ====")
def values_greater_than_second(input_list):
    if len(input_list) < 2:
        return False
    output = []
    for i in range(0,len(input_list)):
        if input_list[i] > input_list[1]:
            output.append(input_list[i])
    print(len(output))
    return output
print(values_greater_than_second([1,2,3,4,5,6])) # 4; [3, 4, 5, 6]
# print(values_greater_than_second([])) #! False

print("\n==== #5 This Length, That Value ====")
def this_length_that_value(size, value):
    # result_list = [value] * size
    # return result_list
    returned_list = []
    for i in range(0, size):
        returned_list.append(value)
    return returned_list
print(this_length_that_value(4,7))
print(this_length_that_value(6,2))