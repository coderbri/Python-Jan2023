class User: # 1 Declare a class
    
    all_users = [] # * ClASS ATTRIBUTES
    
    # Constructor
    def __init__(self, f_name, l_name, age): # Set Attributes
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        
        # * This new instance of User self will be appended to the all_users class attribute.
        User.all_users.append(self)
    
    # Methods
    def introduce(self): # ? Use self to access attributes of User class.
        print(f"Hello, my name is {self.first_name} {self.last_name}.")
        return self
    
    def change_first_name(self, new_name):
        self.first_name = new_name
        return self
    
    def birthday(self):
        self.age += 1
        print(f"You are now {self.age} years old!")
        return self
    
    # ? Linking a method to affect another class:
    def adopt_pet(self, adopted_pet):
        adopted_pet.owner = self # assigning owner will change None to user object
        print(f"Yay! {adopted_pet.name} was adopted!")
        return self
    
    # * CLASS METHOD
    @classmethod
    def display_all_users(cls): #? cls represents the whole User class where we can access anything within it.
        # ! The following will not work: print(cls.all_users)
        # ? We need to loop through each User in the list.
        for user in cls.all_users:
            print(user.first_name)

class Pet: 
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.owner = None
    
    def speak(self):
        pass


# New User Instances
user_1 = User("Ada", "Lovelace", 47)
jdoe = User("Jane", "Doe", 35)
smithy = User("John", "Smithy", 26)

# * Invoking a classMethod:
User.display_all_users()

# * Chaining Methods:
user_1.introduce().change_first_name("Test").introduce().change_first_name("Anabelle").introduce()
user_1.birthday().birthday().birthday()

# New Pet Instance
jake = Pet('Jake', 'Dog')
user_1.adopt_pet(jake)
print(jake.owner.first_name)
