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
