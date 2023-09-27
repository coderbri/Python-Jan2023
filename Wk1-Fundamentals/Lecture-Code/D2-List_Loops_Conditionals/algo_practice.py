x = '5'
y = '8'
print(x+y) # 58
#? Both are strings so its not adding but concatenating.

m = '5'
n = 8
# print(m+n) #! TypeError: can only concatenate str (not "int") to str

print( int('10') + int('9') ) # 19
#? Typecasting strings into ints so addition is possible.

print( str(4) + str(12) ) # 412
#? Typecasting ints into strings.

print(0 == 1) # False #? Boolean check to see if ints match
print(0 == False) # True #? Boolean check; 0 means False
print(1 == True) # True #? Boolean check; 1 means True

a = '10'
if (a == 10):
    print(a)
#? Nothing will happen bc `a` is equal to the str 10, not the int 10.

b = 10
if (b == 10):
    print(b)
# 10 #? b does equal 10 so it will print

c = '10'
if (c == '10'):
    print(c)
# 10 #? c does equal '10' so it will print

"""
d = '10'
if (d === '10'): #! SyntaxError: invalid syntax 
    print(d)
"""

"""
e = 10
while (e != 0):
    print(e)
10, 10, 10, 10... #? This is an infinite loop!
"""

"""
f = 10
while (f != 0):
    f-- #! SyntaxError: invalid syntax 
    print(f)
"""

g = 10
while (g != 0):
    g -= 1
    print(g)
# 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 #? Countdown occurs.

h = 10
while (h != 0):
    print(h)
    h -= 1
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 #? Countdown occurs.

i =10
while (i > 0):
    i -= 1
    print(i)
# 9, 8, 7, 6, 5, 4, 3, 2, 1, 0