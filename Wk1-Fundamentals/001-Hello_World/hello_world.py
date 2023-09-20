print("Hello World!")

name = "Bri"
print("Hello", name)
print("Hello " + name)

name = 7
print("Hello", name)  # output: Hello 7
# print("Hello " + name) #! this is supposed to create an error!
print("Hello " + str(name)) # output: Hello 7 

fave_food1 = "sushi"
fave_food2 = "salmon"
print( "I love to eat {} and {}!".format(fave_food1, fave_food2) ) # I love to eat sushi and salmon!
print( f'I love to eat {fave_food1} and {fave_food2}!' ) # I love to eat sushi and salmon!
