# 1) Print all numbers from 1 255.
def iterate_by_one():
    for i in range(1, 256):
        print(i)
# iterate_by_one()

# 2) Print odd numbers between 1 to 255.
def iterate_odd():
    for i in range(1,256):
        if i % 2 != 0:
            print(i)
# iterate_odd()

# 3) Print the sum of all numbers from 1 to 255.
def sum_of_num():
    sum = 0
    for i in range(1,256):
        sum += i
    print(sum)
# sum_of_num() # 32640

# 4) Given an array (ex: [1, 3, 5, 7, 9, 13]), write a function that would iterate through each number if the array and print each value
arr = [1, 3, 5, 7, 9, 13]
def iterate_array(incoming_arr):
    for i in incoming_arr:
        print(i)
# iterate_array(arr)

# 13)