print("=== FOR LOOP : BASICS I ===")

print('\n=== Basic For Loop')
for i in range(0, 151):
    print(i)

print('\n=== Multiples of 5')
for x in range(5, 1001, 5):
    print(x)

print('\n=== Counting, The Dojo Way')
for int in range(1, 101):
    if int % 10 == 0:
        print("Coding Dojo")
    elif int % 5 == 0:
        print("Coding")
    else:
        print(int)

print('\n=== Whoa. That Sucker\'s Huge')
sum = 0
for num in range(0, 500001,2):
    sum += num
print(sum) # output: 62500250000

print('\n=== Countdown by Fours')
for this_int in range(2018, 0, -4):
    print(this_int)

print('\n=== Flexible Counter')
low_num = 2
high_num = 9
mult = 3
for this_num in range( low_num, high_num + 1 ):
    if this_num % mult == 0:
        print(this_num)