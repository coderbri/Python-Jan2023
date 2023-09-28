class User: # 1 Declare a class
    # Constructor
    def __init__(self, f_name, l_name, age): # Set Attributes
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
    
    # Methods
    def introduce(self): # ? Use self to access attributes of User class.
        print(f"Hello, my name is {self.first_name} {self.last_name}.")
    
    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def birthday(self):
        self.age += 1
        print(f"You are now {self.age} years old!")

# * New User Instances
user_1 = User("Ada", "Lovelace", 47)
print(user_1.first_name) # Ada
user_1.introduce() # Hello, my name is Ada Lovelace.

user_1.change_first_name("Jane")
print(f"New Name: {user_1.first_name}")

user_1.birthday() # You are now 48 years old!



class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
    
    def drive(self):
        self.mileage += 20
        print("vroom vroom")

car1 = Car("Toyota", "Camry", 2007, "Black", 25000)
print(car1.make)

car1.drive()