class Pet:
    def __init__( self, name, animal_type, tricks, noise ):
        self.name = name 
        self.animal_type = animal_type 
        self.tricks = tricks 
        self.noise = noise 
        
        self.health = 100 
        self.energy = 50  
    
    def __repr__(self):
        return "<< Pet: {} - Type: {} - Tricks: {} - Noise: \"{}\" >>".format(self.name, self.animal_type, self.tricks, self.noise)
    
    def sleep( self ):
        if self.energy < 25:
            self.energy = min(100, self.energy + 25)
            print(f'{self.name} is sleeping (.zzZ Gained 25 energy).')
        else:
            print(f"{self.name} is already well-rested.")
        return self
    
    def eat( self ):
        if self.energy < 45:
            self.energy = min(50, self.energy + 5)
            # self.health = min(100, self.energy + 10)
            print(f'(=^x^=) {self.name} is eating ( *munch* *munch* ). {self.name} just gained 5 energy and 10 health.')
        else:
            print(f"{self.name} is not hungry right now.")
        return self # will execute with .feed()
        
    def play( self ):
        if self.energy >= 25:
            self.energy = max(0, self.energy - 25)
            # self.health = min(100, self.health + 5)
            print(f'(=^x^=) {self.name} played! {self.name} just used 25 energy.')
        else:
            print(f"!!! {self.name} is too tired/weak to play right now. Try feeding or letting {self.name} sleep.")
        return self
    
    def make_noise( self ): # prints out the pet's sound
        print('(=^x^=) {}: "{}".'.format(self.name, self.noise))
        return self


class Ninja:
    def __init__( self, first_name, last_name, pet, treats, pet_food ):
        self.first_name = first_name 
        self.last_name = last_name 
        self.pet = pet 
        self.treats = treats
        self.pet_food = pet_food
    
    def __repr__(self):
        return "<< Ninja: {} {} - Pet: {} - Treats: {} - Pet Food: \"{}\" >>".format(self.first_name, self.last_name, self.pet.name, self.treats, self.pet_food)
    
    def play_with_pet( self ): # play with the ninja's pet invoking the pet play() method
        print(f'\nYou are playing with {self.pet.name}.')
        self.pet.play()
        return self
    
    def feed( self ): # feeds the ninja's pet invoking the pet eat() method
        if self.pet.energy < 45:
            if len( self.pet_food ) > 0:
                food = self.pet_food.pop()
                print(f'\nYou are feeding {self.pet.name} {food}.')
                self.pet.eat()
            else: print("\nOh no! You need more pet food!")
        else: print(f"\n{self.pet.name} is not hungry right now.")
        return self
    
    def bathe( self ): # cleans the ninja's pet invoking the pet noise() method
        print(f'\nYou are bathing {self.pet.name}.')
        self.pet.make_noise()
        return self
    
    def display_pet_status( self ):
        print('<< {}\'s Status: {} health, {} energy >>'.format( self.pet.name, self.pet.health, self.pet.energy ))
        return self


# **** Instances ****
bag_of_treats = ['Friskies', 'Temptations', 'Tuna Flakes', 'Churu']
bag_of_pet_food = ['Hill\'s', 'Arcana', 'Royal Canine']

#* Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
neko_chan = Pet('Neko-Chan', 'cat', ['Give Paw', 'Roll Over', 'Catch Mice'], 'meow meow')
jane_doe = Ninja('Jane', 'Doe', neko_chan, bag_of_treats, bag_of_pet_food)
# print(neko_chan)
# print(jane_doe)

#* Have the Ninja feed, play_with_pet, and bathe their pet.
# jane_doe.display_pet_status()
jane_doe.feed().display_pet_status()
jane_doe.play_with_pet().display_pet_status().play_with_pet().display_pet_status().play_with_pet().display_pet_status()
neko_chan.sleep()
jane_doe.display_pet_status().bathe()