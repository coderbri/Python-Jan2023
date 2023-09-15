import random

print('=== Welcome to Python! ===')

print('\nThis is a loop printing 5 times:')  # The "\n" adds a line break
for x in range(1, 6):
    print(f'x is {x}')
"""Output:
    x is 1
    x is 2
    x is 3
    x is 4
    x is 5
"""

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays) #? randomly selects a day
print(f'Today is {day}')

print('\nWhat day of the week is it? Let\'s see...')
if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print("Woohoo, time for the weekend!")
else:
    print('Not quite there yet.')