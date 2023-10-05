from user_data_mockdb import people

class User:
    
    all_users = [] # * ClASS ATTRIBUTES
    
    def __init__(self, some_list): # Set Attributes
        self.first_name = some_list['first_name']
        self.last_name = some_list['last_name']
        self.age = some_list['age']
        User.all_users.append(self)
    
    
    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}.")
        return self
    
    def change_first_name(self, new_name):
        self.first_name = new_name
        return self
    
    def birthday(self):
        self.age += 1
        print(f"You are now {self.age} years old!")
        return self
    
    def adopt_pet(self, adopted_pet):
        adopted_pet.owner = self
        print(f"Yay! {adopted_pet.name} was adopted!")
        return self
    
    # * CLASS METHOD
    @classmethod
    def display_all_users(cls):
        for user in cls.all_users:
            print(user.first_name)
    
    # * How about importing an already existing collection of data?
    @classmethod
    def create_user(cls, some_list):
        # It will use the constructor as the basis of how the object is instantiated.
        for user in some_list:
            # print(user) #? prints user as dictionary object
            cls(user) #? converts dict_obj into User instance

User.create_user(people)
"""Output (as dictionary)
{'first_name': 'Mark', 'last_name': 'Brown', 'age': 26}
{'first_name': 'Justina', 'last_name': 'Gray', 'age': 34}
{'first_name': 'Eliza', 'last_name': 'Myers', 'age': 28}
"""
User.display_all_users()

class Pet: 
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.owner = None
    


# # New User Instances
# user_1 = User("Ada", "Lovelace", 47)
# jdoe = User("Jane", "Doe", 35)
# smithy = User("John", "Smithy", 26)

# # * Invoking a classMethod:
# User.display_all_users()

# # * Chaining Methods:
# user_1.introduce().change_first_name("Test").introduce().change_first_name("Anabelle").introduce()
# user_1.birthday().birthday().birthday()

# # New Pet Instance
# jake = Pet('Jake', 'Dog')
# user_1.adopt_pet(jake)
# print(jake.owner.first_name)
